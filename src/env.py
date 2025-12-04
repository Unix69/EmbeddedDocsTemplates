import os
from dotenv import load_dotenv

from exception import ChatbotException


class EnvironmentException(ChatbotException): pass
class EnvironmentCheckException(EnvironmentException): pass
class EnvironmentUnmatchedVariableTypeException(EnvironmentException): pass
class EnvironmentMissingRequiredVariableException(EnvironmentException): pass


class Env:
    def __init__(self, env_file: str = "chatbot.env"):
        load_dotenv(env_file)

        
        self.APP_NAME: str = self._get_str("APP_NAME")
        self.APP_KEY: str = self._get_str("APP_KEY")
        self.HF_TOKEN: str = self._get_str("HF_TOKEN", required=False)
        self.COHERE_API_KEY: str = self._get_str("COHERE_API_KEY", required=False)
        self.GPT_API_KEY: str = self._get_str("GPT_API_KEY")

        
        self.NGROK_PATH: str = self._get_str("NGROK_PATH")
        self.NGROK_PORT: int = self._get_int("NGROK_PORT")
        self.NGROK_PROTO: str = self._get_str("NGROK_PROTO")
        self.NGROK_HOST: str = self._get_str("NGROK_HOST")
        self.NGROK_URL_VISIBILITY: str = self._get_str("NGROK_URL_VISIBILITY")
        self.NGROK_TUNNELS_API: str = f"{self.NGROK_PROTO}://{self.NGROK_HOST}:{self.NGROK_PORT}/tunnels"

        
        self.COMMON_LOG_DIR: str = self._get_str("COMMON_LOG_DIR")
        self.MAIN_LOGGER_LEVEL: str = self._get_str("MAIN_LOGGER_LEVEL")
        self.MAIN_LOGGER_MAX_SIZE: int = self._get_int("MAIN_LOGGER_MAX_SIZE")
        self.MAIN_LOGGER_MAX_FILES: int = self._get_int("MAIN_LOGGER_MAX_FILES")
        self.MAIN_LOGGER_HANDLER: str = self._get_str("MAIN_LOGGER_HANDLER", required=False)
        self.MAIN_LOGGER_ENC: str = self._get_str("MAIN_LOGGER_ENC")

        
        self.TELEGRAM_API_SERVER_PROTO: str = self._get_str("TELEGRAM_API_SERVER_PROTO")
        self.TELEGRAM_API_SERVER: str = self._get_str("TELEGRAM_API_SERVER")
        self.TELEGRAM_BOT_PATH: str = self._get_str("TELEGRAM_BOT_PATH")
        self.TELEGRAM_TOKEN: str = self._get_str("TELEGRAM_TOKEN")
        self.TELEGRAM_BOT: str = f"{self.TELEGRAM_API_SERVER_PROTO}://{self.TELEGRAM_API_SERVER}{self.TELEGRAM_BOT_PATH}"
        self.TELEGRAM_BOT_SEND_MESSAGE_API: str = f"{self.TELEGRAM_BOT}{self.TELEGRAM_TOKEN}/sendMessage"
        self.TELEGRAM_BOT_SET_WEBHOOK_API: str = f"{self.TELEGRAM_BOT}{self.TELEGRAM_TOKEN}/setWebhook"
        self.TELEGRAM_BOT_WEBHOOK_METHOD: str = self._get_str("TELEGRAM_BOT_WEBHOOK_METHOD")

        self.FACEBOOK_API_SERVER_PROTO: str = self._get_str("FACEBOOK_PROTO")
        self.FACEBOOK_API_SERVER: str = self._get_str("FACEBOOK_API_SERVER")
        self.FACEBOOK_BOT_PATH: str = self._get_str("FACEBOOK_BOT_PATH")
        self.FACEBOOK_TOKEN: str = self._get_str("FACEBOOK_TOKEN")
        self.FACEBOOK_BOT: str = f"{self.FACEBOOK_API_SERVER_PROTO}://{self.FACEBOOK_API_SERVER}{self.FACEBOOK_BOT_PATH}"
        self.FACEBOOK_BOT_SEND_MESSAGE_API: str = f"{self.FACEBOOK_BOT}/messages"
        self.FACEBOOK_BOT_WEBHOOK_METHOD: str = self._get_str("FACEBOOK_BOT_WEBHOOK_METHOD")

       
        self.WHATSAPP_TOKEN: str = self._get_str("WHATSAPP_TOKEN")
        self.WHATSAPP_PHONE_NUMBER_ID: str = self._get_str("WHATSAPP_PHONE_NUMBER_ID")
        self.WHATSAPP_API_SERVER_PROTO: str = self._get_str("WHATSAPP_PROTO")
        self.WHATSAPP_API_SERVER: str = self._get_str("WHATSAPP_API_SERVER")
        self.WHATSAPP_BOT_PATH: str = self._get_str("WHATSAPP_BOT_PATH")
        self.WHATSAPP_BOT: str = f"{self.WHATSAPP_API_SERVER_PROTO}://{self.WHATSAPP_API_SERVER}{self.WHATSAPP_BOT_PATH}"
        self.WHATSAPP_BOT_SEND_MESSAGE_API: str = f"{self.WHATSAPP_BOT}/messages"
        self.WHATSAPP_BOT_WEBHOOK_METHOD: str = self._get_str("WHATSAPP_BOT_WEBHOOK_METHOD")

       
        self.SERVER_PORT: int = self._get_int("SERVER_PORT")
        self.SERVER_HOST: str = self._get_str("SERVER_HOST")
        self.SERVER_PROTO: str = self._get_str("SERVER_PROTO")
        self.SERVER_MODE: str = self._get_str("SERVER_MODE")
        self.SERVER_EVENT_INFO_METHOD: str = self._get_str("SERVER_EVENT_INFO_METHOD")
        self.SERVER_RESERVATION_METHOD: str = self._get_str("SERVER_RESERVATION_METHOD")
        self.SERVER_SHUTDOWN_METHOD: str = self._get_str("SERVER_SHUTDOWN_METHOD")
        self.BOT_MANAGER_RUN_TIMEOUT: int = self._get_int("BOT_MANAGER_RUN_TIMEOUT")

   
    def _get_str(self, key: str, required: bool = True) -> str:
        value = os.getenv(key)
        if required and (value is None or value.strip() == ""):
            raise EnvironmentMissingRequiredVariableException(f"Missing required environment variable: {key}")
        return value.strip() if value else None

    def _get_int(self, key: str, required: bool = True) -> int:
        value = self._get_str(key, required=required)
        if value is None:
            return None
        try:
            return int(value)
        except ValueError:
            raise EnvironmentUnmatchedVariableTypeException(f"Environment variable {key} must be an integer. Got: {value}")


    def check_env(self):
        required_vars = [
            "APP_NAME", "APP_KEY", "GPT_API_KEY",
            "NGROK_PATH", "NGROK_PORT", "NGROK_PROTO",
            "TELEGRAM_TOKEN", "WHATSAPP_TOKEN", "WHATSAPP_PHONE_NUMBER_ID",
            "FACEBOOK_TOKEN"
        ]
        missing = [var for var in required_vars if getattr(self, var, None) is None]
        if missing:
            raise EnvironmentCheckException(f"Missing required environment variables: {missing}")

environ = Env()
environ.check_env()
