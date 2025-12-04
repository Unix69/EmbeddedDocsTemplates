import inspect
import traceback
import json
from enum import Enum, auto


class ChatbotException(Exception):
    class ChatbotExceptionCode(Enum):
        NO_ERROR = auto()
        GENERIC_ERROR = auto()
        CONFIG_ERROR = auto()
        NETWORK_ERROR = auto()
        TIMEOUT_ERROR = auto()
        DB_ERROR = auto()

    class ChatbotExceptionSeverity(Enum):
        GENERIC = auto()
        DEBUG = auto()
        WARNING = auto()
        ALERT = auto()
        CRITICAL = auto()

    SEVERITY_TO_LOGGING = {
        ChatbotExceptionSeverity.DEBUG: "DEBUG",
        ChatbotExceptionSeverity.WARNING: "WARNING",
        ChatbotExceptionSeverity.ALERT: "ERROR",
        ChatbotExceptionSeverity.CRITICAL: "CRITICAL",
        ChatbotExceptionSeverity.GENERIC: "INFO"
    }

    def __init__(
        self,
        code: "ChatbotException.ChatbotExceptionCode" = None,
        message: str = None,
        severity: "ChatbotException.ChatbotExceptionSeverity" = None,
        filename: str = None,
        lineno: int = None,
        cause: Exception = None,
        include_trace: bool = True
    ):
        # Recupero file e linea chiamante se non specificati
        if filename is None or lineno is None:
            stack = inspect.stack()
            caller_frame = next(
                (f for f in stack[1:] if f.function not in ("__init__",)), None
            )
            if caller_frame:
                filename = filename or caller_frame.filename
                lineno = lineno or caller_frame.lineno

        # Default values
        code = code or self.ChatbotExceptionCode.GENERIC_ERROR
        message = message or "no message"
        severity = severity or self.ChatbotExceptionSeverity.GENERIC

        self.code = code
        self.message = message
        self.severity = severity
        self.filename = filename
        self.lineno = lineno
        self.type = self.__class__.__name__
        self.cause = cause
        self.traceback = "".join(traceback.format_stack(limit=5)) if include_trace else None

        super().__init__(f"[{code.name}] {message}")

    def __str__(self):
        base_msg = (
            f"{self.type} {self.code.name}: {self.message} "
            f"(Severity: {self.severity.name}, File: {self.filename}, Line: {self.lineno})"
        )
        if self.cause:
            base_msg += f" | Caused by: {repr(self.cause)}"
        return base_msg

    def __repr__(self):
        return (
            f"{self.type}(code={self.code}, message={repr(self.message)}, "
            f"severity={self.severity}, filename={repr(self.filename)}, "
            f"lineno={repr(self.lineno)}, cause={repr(self.cause)})"
        )

    def to_dict(self):
        return {
            "type": self.type,
            "code": self.code.name,
            "message": self.message,
            "severity": self.severity.name,
            "filename": self.filename,
            "lineno": self.lineno,
            "cause": repr(self.cause) if self.cause else None,
            "traceback": self.traceback if self.traceback else None,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)