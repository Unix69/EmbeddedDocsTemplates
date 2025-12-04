import atexit
import os
import sys
import time
import queue
import threading
import inspect
import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler, SysLogHandler
from functools import wraps
from dataclasses import dataclass
from typing import Optional, Union
from exception import ChatbotException
from env import environ
import colorlog
import codecs

class LogException(ChatbotException): pass
class LogConfigurationException(LogException): pass
class LogDebugOperationException(LogException): pass
class LogInfoOperationException(LogException): pass
class LogWarningOperationException(LogException): pass
class LogErrorOperationException(LogException): pass
class LogCriticalOperationException(LogException): pass
class LogWrongAttributeException(LogConfigurationException): pass


@dataclass(frozen=True)
class DefaultLogAttributes:
    log_dir: str = "./logs"
    log_filename: str = "default.log"
    min_level: str = "INFO"
    max_files: int = 50
    max_size: int = 50
    encoding: str = "utf-8"


class Logger(logging.Logger):
    logger_queue = queue.Queue()
    logger_stop_event = threading.Event()
    logger_thread: Optional[threading.Thread] = None
    
    
    log_level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    def format_msg(func):
        @wraps(func)
        def wrapper(self, msg, *args, **kwargs):
            exc_info = None
            if isinstance(msg, BaseException):
                exc_info = (type(msg), msg, msg.__traceback__)
                msg = str(msg)
            return func(self, msg, *args, exc_info=exc_info, **kwargs)
        return wrapper

    @staticmethod
    def get_creator_class_name():
        for frame_info in inspect.stack():
            self_obj = frame_info.frame.f_locals.get('self', None)
            if self_obj and not isinstance(self_obj, Logger):
                return self_obj.__class__.__name__
        return None

    @staticmethod
    def generate_unique_filename(dir, filename):
        full_path = os.path.join(dir, filename)
        if not os.path.exists(full_path):
            return full_path
        name, ext = os.path.splitext(filename)
        timestamp = int(time.time())
        return f"{name}_{timestamp}{ext}"

    def __init__(self, name,
                 enable_file_handler: bool = True,
                 enable_stream_handler: bool = False,
                 enable_syslog_handler: bool = False):
        super().__init__(name)
        
        # Configuration flag
        self._configured = False

        # Handler flags
        self.enable_file_handler = enable_file_handler
        self.enable_stream_handler = enable_stream_handler
        self.enable_syslog_handler = enable_syslog_handler

        # Handler placeholders
        self.file_handler = None
        self.stream_handler = None
        self.syslog_handler = None

    def config(self, log_dir: Optional[str] = None,
                     log_filename: Optional[str] = None,
                     min_level: Optional[Union[str, int]] = None,
                     max_files: Optional[int] = None,
                     max_size: Optional[int] = None,
                     encoding: Optional[str] = None):
        if self._configured:
            return

        try:
            log_dir = log_dir or environ.COMMON_LOG_DIR or DefaultLogAttributes.log_dir
            log_filename = log_filename or f"{self.name}.log"
            min_level = min_level or DefaultLogAttributes.min_level
            max_files = max_files or DefaultLogAttributes.max_files
            max_size = max_size or DefaultLogAttributes.max_size
            encoding = encoding or DefaultLogAttributes.encoding

            # Validate configuration attributes
            if not isinstance(max_files, int) or max_files <= 0 or max_files > 50:
                raise LogWrongAttributeException(f"Wrong max_files attribute: {max_files}")
            if not isinstance(max_size, int) or max_size <= 0 or max_size > 50:
                raise LogWrongAttributeException(f"Wrong max_size attribute: {max_size}")
            if not isinstance(log_filename, str):
                raise LogWrongAttributeException(f"Wrong log_filename attribute: {log_filename}")
            if not isinstance(log_dir, str) or not log_dir.strip():
                raise LogWrongAttributeException(f"Wrong log_dir attribute: {log_dir!r}")
            if isinstance(min_level, str):
                min_level_up = min_level.upper()
                if min_level_up not in self.log_level_map:
                    raise LogWrongAttributeException(f"Wrong min_level attribute: {min_level}")
                log_level = self.log_level_map[min_level_up]
            elif isinstance(min_level, int):
                if min_level not in self.log_level_map.values():
                    raise LogWrongAttributeException(f"Wrong min_level attribute: {min_level}")
                log_level = min_level
            else:
                raise LogWrongAttributeException(f"Wrong min_level attribute: {min_level}")
            if not isinstance(encoding, str) or not self.is_valid_encoding(encoding):
                raise LogWrongAttributeException(f"Wrong encoding attribute: {encoding}")

            self.setLevel(log_level)
            os.makedirs(log_dir, exist_ok=True)

            # Set Formatter
            file_formatter = logging.Formatter(
                "DateTime-%(asctime)s|Proc-%(processName)s|Thread-%(threadName)s|"
                "Mod-%(module)s|Func-%(funcName)s|File-%(pathname)s|Line-%(lineno)d|"
                "Logger-%(name)s|Level-%(levelname)s: %(message)s"
            )

            stream_formatter = colorlog.ColoredFormatter(
                "%(log_color)s%(asctime)s|%(processName)s|%(threadName)s|"
                "%(module)s|%(funcName)s|%(lineno)d|%(levelname)s: %(message)s",
                log_colors={
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "red,bg_white",
                },
                style='%'
            )

            # FILE HANDLER
            if self.enable_file_handler:
                self.file_handler = RotatingFileHandler(
                    filename=os.path.join(log_dir, log_filename),
                    maxBytes=1024*1024*max_size,
                    backupCount=max_files,
                    encoding=encoding,
                    delay=True
                )
                self.file_handler.setFormatter(file_formatter)
                self.file_handler.setLevel(log_level)
                self.addHandler(self.file_handler)

            # STREAM HANDLER
            if self.enable_stream_handler:
                self.stream_handler = StreamHandler(sys.stdout)
                self.stream_handler.setFormatter(stream_formatter)
                self.stream_handler.setLevel(log_level)
                self.addHandler(self.stream_handler)

            # SYSLOG HANDLER (solo su Unix-like)
            if self.enable_syslog_handler and (sys.platform.startswith("linux") or sys.platform == "darwin"):
                self.syslog_handler = SysLogHandler(address="/dev/log")
                self.syslog_handler.setFormatter(file_formatter)
                self.syslog_handler.setLevel(log_level)
                self.addHandler(self.syslog_handler)

            self._configured = True

        except Exception as e:
            raise LogConfigurationException(f"Unable to configure logger: {e}")

    @classmethod
    def logger_run(cls):
        while not cls.logger_stop_event.is_set():
            try:
                try:
                    log = cls.logger_queue.get(timeout=0.5)
                except queue.Empty:
                    continue

                if log is None:
                    break

                logger, level, msg, args, kwargs, record_info, exc_info = log

                record = logger.makeRecord(
                    name=logger.name,
                    level=Logger.log_level_map[level.upper()],
                    fn=record_info["pathname"],
                    lno=record_info["lineno"],
                    msg=msg,
                    args=args,
                    exc_info=exc_info,
                    func=record_info["funcName"]
                )

                logger.handle(record)

            except Exception as e:
                print(f"Logger exception: {e}", file=sys.stderr)


    @classmethod
    def logger_put(cls, logger, level, msg, *args, **kwargs):
        frame_info = inspect.stack()[3]
        record_info = {
            "pathname": frame_info.filename,
            "lineno": frame_info.lineno,
            "funcName": frame_info.function
        }
        cls.logger_queue.put((logger, level, msg, args, kwargs, record_info, kwargs.get("exc_info")))

    @classmethod
    def start_logger(cls, thread_name: str = "LoggerThread", daemon: bool = True, **thread_kwargs):
        if cls.logger_thread is None or not cls.logger_thread.is_alive():
            cls.logger_stop_event.clear()
            cls.logger_thread = threading.Thread(
                target=cls.logger_run,
                name=thread_name,
                daemon=daemon,
                **thread_kwargs
            )
            cls.logger_thread.start()
        print(f"Logger Thread '{thread_name}' Started")

    @classmethod
    def shutdown_logger(cls):
        cls.logger_stop_event.set()
        cls.logger_queue.put(None)

        if cls.logger_thread and cls.logger_thread.is_alive():
            cls.logger_thread.join()

        for logger_instance in logging.root.manager.loggerDict.values():
            if isinstance(logger_instance, Logger):
                for handler in logger_instance.handlers:
                    try:
                        handler.close()
                    except Exception:
                        pass
                    logger_instance.removeHandler(handler)

    @staticmethod
    def is_valid_encoding(encoding: str):
        try:
            codecs.lookup(encoding)
            return True
        except LookupError:
            return False

    @format_msg
    def debug(self, msg, *args, **kwargs):
        try:
            print("Logger debug message " + str(msg))
            self.logger_put(self, "debug", msg, *args, **kwargs)
        except Exception as e:
            raise LogDebugOperationException(f"Unable to perform debug log operation: {e}")

    @format_msg
    def info(self, msg, *args, **kwargs):
        try:
            self.logger_put(self, "info", msg, *args, **kwargs)
        except Exception as e:
            raise LogInfoOperationException(f"Unable to perform info log operation: {e}")

    @format_msg
    def warning(self, msg, *args, **kwargs):
        try:
            self.logger_put(self, "warning", msg, *args, **kwargs)
        except Exception as e:
            raise LogWarningOperationException(f"Unable to perform warning log operation: {e}")

    @format_msg
    def error(self, msg, *args, **kwargs):
        try:
            self.logger_put(self, "error", msg, *args, **kwargs)
        except Exception as e:
            raise LogErrorOperationException(f"Unable to perform error log operation: {e}")

    @format_msg
    def critical(self, msg, *args, **kwargs):
        try:
            self.logger_put(self, "critical", msg, *args, **kwargs)
        except Exception as e:
            raise LogCriticalOperationException(f"Unable to perform critical log operation: {e}")




Logger.start_logger()
atexit.register(Logger.shutdown_logger)

main_logger = Logger(name="Chatbot", enable_file_handler=True, enable_stream_handler=True)
main_logger.config(min_level="debug", encoding="utf-8", max_files=50, max_size=50)
    