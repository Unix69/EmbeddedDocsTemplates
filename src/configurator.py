import subprocess
import time
import requests
import atexit

from exception import ChatbotException
from logger import LogConfigurationException, Logger
from env import environ
from enum import Enum, auto


class ConfigurationExceptionCode(Enum):
    NO_ERROR = auto()

    HTTP_METHOD_ERROR = auto()
    HTTP_REQUEST_TIMEOUT = auto()
    HTTP_TIMEOUT = auto()

    NGROK_START_FAILED = auto()
    NGROK_NOT_READY = auto()
    NGROK_STOP_FAILED = auto()
    NGROK_CHECK_FAILED = auto()
    NGROK_VERIFY_FAILED = auto()

    TELEGRAM_WEBHOOK_HTTP_ERROR = auto()
    TELEGRAM_WEBHOOK_METHOD_ERROR = auto()
    TELEGRAM_WEBHOOK_UNEXPECTED_ERROR = auto()

    CONFIG_LOGGER_FAILED = auto()
    CONFIG_UNEXPECTED_ERROR = auto()


class ConfigurationException(ChatbotException): pass
class ConfigurationStartNgrokException(ConfigurationException): pass
class ConfigurationVerifyNgrokException(ConfigurationException): pass
class ConfigurationCheckNgrokException(ConfigurationException): pass
class ConfigurationStopNgrokException(ConfigurationException): pass
class ConfigurationSetTelegramWebhookException(ConfigurationException): pass

class ConfigurationHTTPRequestExcpetion(ConfigurationException): pass
class ConfigurationHTTPRequestMethodExcpetion(ConfigurationException): pass
class ConfigurationHTTPRequestTimeoutExcpetion(ConfigurationException): pass
class ConfigurationHTTPRequestRetryExcpetion(ConfigurationException): pass


class Configurator:
    def __init__(self, ngrok_path: str, ngrok_port: int, ngrok_host: str, ngrok_proto: str,
                 ngrok_tunnels_api: str, ngrok_endpoint_visibility: str,
                 tg_bot_webhook_method: str, tg_bot_set_webhook_api: str):

        self.ngrok_path = environ.NGROK_PATH
        self.ngrok_port = environ.NGROK_PORT
        self.ngrok_host = environ.NGROK_HOST
        self.ngrok_proto = environ.NGROK_PROTO
        self.ngrok_tunnels_api = environ.NGROK_TUNNELS_API
        self.ngrok_endpoint_visibility = environ.NGROK_URL_VISIBILITY
        self.ngrok_endpoint = None
        self.ngrok_process = None
        self.tg_bot_set_webhook_api = environ.TELEGRAM_BOT_SET_WEBHOOK_API
        self.tg_bot_webhook_method = environ.TELEGRAM_BOT_WEBHOOK_METHOD

        self.conf_logger = Logger("configurator", enable_file_handler=True,
                                  enable_stream_handler=False, enable_syslog_handler=False)


    def http_request_with_retry(self, method: str, url: str, max_retries: int = 5, delay: float = 1.0, **kwargs):
        for attempt in range(1, max_retries + 1):
            try:
                if method.lower() == "get":
                    response = requests.get(url, timeout=5, **kwargs)
                elif method.lower() == "post":
                    response = requests.post(url, timeout=5, **kwargs)
                else:
                    raise ConfigurationHTTPRequestMethodExcpetion(
                        f"Unsupported HTTP method: {method}",
                        code=ConfigurationExceptionCode.HTTP_METHOD_ERROR
                    )
                response.raise_for_status()
                return response

            except requests.Timeout as e:
                if attempt == max_retries:
                    raise ConfigurationHTTPRequestTimeoutExcpetion(
                        f"HTTP {method.upper()} timeout after {max_retries} attempts",
                        code=ConfigurationExceptionCode.HTTP_TIMEOUT,
                        cause=e
                    )

            except requests.RequestException as e:
                self.conf_logger.warning(f"HTTP {method.upper()} failed (attempt {attempt}/{max_retries}): {e}")
                if attempt == max_retries:
                    raise ConfigurationHTTPRequestRetryExcpetion(f"HTTP {method.upper()} failed after {max_retries} attempts", code=ConfigurationExceptionCode.HTTP_REQUEST_TIMEOUT, cause=e)
            time.sleep(delay)

    def start_ngrok(self, max_retries: int = 5, delay: float = 1.0) -> str:
        try:
            self.ngrok_process = subprocess.Popen(
                [self.ngrok_path, self.ngrok_proto, f"{self.ngrok_host}:{self.ngrok_port}"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT
            )

            for attempt in range(max_retries):
                try:
                    response = self.http_request_with_retry("get", self.ngrok_tunnels_api, max_retries=3, delay=delay)
                    tunnels = response.json().get("tunnels", [])
                    for tunnel in tunnels:
                        if tunnel.get("proto") == self.ngrok_proto:
                            self.ngrok_endpoint = tunnel[self.ngrok_endpoint_visibility]
                            atexit.register(self.stop_ngrok)
                            return self.ngrok_endpoint

                except ConfigurationHTTPRequestMethodExcpetion as me:
                    raise ConfigurationStartNgrokException(
                        f"Ngrok tunnel check failed: invalid HTTP method ({me})",
                        code=ConfigurationExceptionCode.HTTP_METHOD_ERROR,
                        cause=me
                    )

                except ConfigurationHTTPRequestTimeoutExcpetion as te:
                    raise ConfigurationStartNgrokException(
                        f"Ngrok tunnel check failed: timeout ({te})",
                        code=ConfigurationExceptionCode.HTTP_TIMEOUT,
                        cause=te
                    )

                except ConfigurationHTTPRequestRetryExcpetion as re:
                    self.conf_logger.warning(f"Ngrok tunnel API not reachable (attempt {attempt+1}/{max_retries}): {re}")
                    if attempt == max_retries - 1:
                        raise ConfigurationStartNgrokException(
                            "Ngrok tunnel API unreachable after retries",
                            code=ConfigurationExceptionCode.NGROK_NOT_READY,
                            cause=re
                        )
                    time.sleep(delay)

                except requests.RequestException as re:
                    self.conf_logger.warning(f"Ngrok not ready, retrying... ({attempt+1}/{max_retries})")
                    if attempt == max_retries - 1:
                        raise ConfigurationStartNgrokException(
                            "Ngrok did not respond within retries",
                            code=ConfigurationExceptionCode.NGROK_NOT_READY,
                            cause=re
                        )
                    time.sleep(delay)

            raise ConfigurationStartNgrokException(
                "Unable to start ngrok service after retries",
                code=ConfigurationExceptionCode.NGROK_NOT_READY
            )

        except ConfigurationStartNgrokException:
            raise
        except Exception as e:
            self.conf_logger.critical("Failed to start ngrok")
            raise ConfigurationStartNgrokException(
                "Ngrok start failure",
                code=ConfigurationExceptionCode.NGROK_START_FAILED,
                cause=e
            )

    def stop_ngrok(self):
        try:
            if self.ngrok_process:
                self.conf_logger.info("Stopping ngrok service")
                self.ngrok_process.terminate()
                self.ngrok_process = None
                self.conf_logger.info("Ngrok process terminated")
        except Exception as e:
            self.conf_logger.critical("Failed to stop ngrok")
            raise ConfigurationStopNgrokException(
                "Ngrok stop failure",
                code=ConfigurationExceptionCode.NGROK_STOP_FAILED,
                cause=e
            )

    def check_ngrok(self) -> tuple[bool, str | None]:
        try:
            response = self.http_request_with_retry("get", self.ngrok_tunnels_api)
            tunnels = response.json().get("tunnels", [])
            for tunnel in tunnels:
                if tunnel.get("proto") == self.ngrok_proto:
                    self.ngrok_endpoint = tunnel["public_url"]
                    return True, self.ngrok_endpoint
            return False, None

        except ConfigurationHTTPRequestMethodExcpetion as me:
            raise ConfigurationCheckNgrokException(
                f"Ngrok check failed: invalid HTTP method ({me})",
                code=ConfigurationExceptionCode.HTTP_METHOD_ERROR,
                cause=me
            )

        except ConfigurationHTTPRequestTimeoutExcpetion as te:
            raise ConfigurationCheckNgrokException(
                f"Ngrok check failed: timeout ({te})",
                code=ConfigurationExceptionCode.HTTP_TIMEOUT,
                cause=te
            )

        except ConfigurationHTTPRequestRetryExcpetion as re:
            raise ConfigurationCheckNgrokException(
                f"Ngrok check failed after retries: {re}",
                code=ConfigurationExceptionCode.NGROK_CHECK_FAILED,
                cause=re
            )

        except requests.RequestException as re:
            self.conf_logger.warning(f"Ngrok connection failed: {re}")
            return False, None

        except Exception as e:
            self.conf_logger.critical("Unexpected error during ngrok check")
            raise ConfigurationCheckNgrokException(
                "Unexpected error during ngrok check",
                code=ConfigurationExceptionCode.NGROK_CHECK_FAILED,
                cause=e
            )

    def verify_ngrok(self) -> bool:
        try:
            self.conf_logger.info("Verify ngrok connection")
            alive, endpoint = self.check_ngrok()
            if alive:
                self.conf_logger.info(f"Ngrok is alive: {endpoint}")
                return True
            else:
                raise ConfigurationVerifyNgrokException(
                    "Ngrok is NOT alive",
                    code=ConfigurationExceptionCode.NGROK_VERIFY_FAILED
                )

        except ConfigurationCheckNgrokException as ccne:
            raise ConfigurationVerifyNgrokException(
                f"Verification failed due to check error: {ccne}",
                code=ConfigurationExceptionCode.NGROK_VERIFY_FAILED,
                cause=ccne
            )

        except Exception as e:
            raise ConfigurationVerifyNgrokException(
                "Unexpected error during ngrok verification",
                code=ConfigurationExceptionCode.NGROK_VERIFY_FAILED,
                cause=e
            )

    def set_telegram_webhook(self, ngrok_endpoint: str):
        try:
            self.conf_logger.info("Set telegram webhook")
            webhook_api = f"{ngrok_endpoint}{self.tg_bot_webhook_method}"
            self.conf_logger.info(f"Set telegram webhook api {webhook_api} by using api {self.tg_bot_set_webhook_api}")

            response = self.http_request_with_retry("post", self.tg_bot_set_webhook_api, data={"url": webhook_api})
            self.conf_logger.info("Telegram response: " + str(response.json()))

        except ConfigurationHTTPRequestMethodExcpetion as me:
            raise ConfigurationSetTelegramWebhookException(
                f"Invalid HTTP method used for webhook: {me}",
                code=ConfigurationExceptionCode.TELEGRAM_WEBHOOK_METHOD_ERROR,
                cause=me
            )

        except ConfigurationHTTPRequestTimeoutExcpetion as te:
            raise ConfigurationSetTelegramWebhookException(
                f"Webhook setup failed due to timeout: {te}",
                code=ConfigurationExceptionCode.HTTP_TIMEOUT,
                cause=te
            )

        except ConfigurationHTTPRequestRetryExcpetion as re:
            raise ConfigurationSetTelegramWebhookException(
                f"Webhook setup failed after retries: {re}",
                code=ConfigurationExceptionCode.TELEGRAM_WEBHOOK_HTTP_ERROR,
                cause=re
            )

        except requests.RequestException as re:
            raise ConfigurationSetTelegramWebhookException(
                f"Webhook setup failed due to HTTP/network error: {re}",
                code=ConfigurationExceptionCode.TELEGRAM_WEBHOOK_HTTP_ERROR,
                cause=re
            )

        except Exception as e:
            raise ConfigurationSetTelegramWebhookException(
                "Unexpected error while setting Telegram webhook",
                code=ConfigurationExceptionCode.TELEGRAM_WEBHOOK_UNEXPECTED_ERROR,
                cause=e
            )

    def configure(self):
        try:
            self.conf_logger.config()
            endpoint = self.start_ngrok()
            self.set_telegram_webhook(endpoint)
            self.verify_ngrok()

        except LogConfigurationException as lce:
            self.conf_logger.critical(f"Logger configuration failed: {lce}")
            raise ConfigurationException(
                "Logger configuration failed",
                code=ConfigurationExceptionCode.CONFIG_LOGGER_FAILED,
                cause=lce
            )

        except ConfigurationStartNgrokException as sne:
            self.conf_logger.critical(f"Ngrok start failed: {sne}")
            raise ConfigurationException(
                "Configuration failed during Ngrok start",
                code=ConfigurationExceptionCode.NGROK_START_FAILED,
                cause=sne
            )

        except ConfigurationVerifyNgrokException as vne:
            self.conf_logger.critical(f"Ngrok verification failed: {vne}")
            raise ConfigurationException(
                "Configuration failed during Ngrok verification",
                code=ConfigurationExceptionCode.NGROK_VERIFY_FAILED,
                cause=vne
            )

        except ConfigurationSetTelegramWebhookException as twe:
            self.conf_logger.critical(f"Telegram webhook setup failed: {twe}")
            raise ConfigurationException(
                "Configuration failed during Telegram webhook setup",
                code=ConfigurationExceptionCode.TELEGRAM_WEBHOOK_UNEXPECTED_ERROR,
                cause=twe
            )

        except ConfigurationException as ce:
            self.conf_logger.critical(f"Generic configuration failure: {ce}")
            raise ConfigurationException(
                "Generic configuration failure",
                code=ConfigurationExceptionCode.CONFIG_UNEXPECTED_ERROR,
                cause=ce
            )

        except Exception as e:
            self.conf_logger.critical("Unexpected error during configuration")
            raise ConfigurationException(
                "Unexpected configuration failure",
                code=ConfigurationExceptionCode.CONFIG_UNEXPECTED_ERROR,
                cause=e
            )


config = Configurator(
    ngrok_path=environ.NGROK_PATH,
    ngrok_port=environ.NGROK_PORT,
    ngrok_host=environ.NGROK_HOST,
    ngrok_proto=environ.NGROK_PROTO,
    ngrok_tunnels_api=environ.NGROK_TUNNELS_API,
    ngrok_endpoint_visibility=environ.NGROK_URL_VISIBILITY,
    tg_bot_set_webhook_api=environ.TELEGRAM_BOT_SET_WEBHOOK_API,
    tg_bot_webhook_method=environ.TELEGRAM_BOT_WEBHOOK_METHOD
)