from asyncio import sleep
from datetime import datetime
import json
from threading import Condition
import threading
import requests
from env import environ
from exception import ChatbotException
from logger import Logger
import queue
from typing import Callable, Dict, Union, Optional
import atexit


class BotManagerException(ChatbotException):
    pass

class BotManagerStartException(BotManagerException):
    pass

class BotManagerStopException(BotManagerException):
    pass

class BotManagerThreadException(BotManagerException):
    pass

class BotManagerBotException(BotManagerException):
    pass

class BotManagerAliveCheckException(BotManagerException):
    pass

class BotException(ChatbotException):
    pass

class BotInitializationException(BotException):
    pass

class BotStartException(BotException):
    pass

class BotStopException(BotException):
    pass

class BotHealthCheckException(BotException):
    pass

class BotSerializationException(BotException):
    pass

class BotDeserializationException(BotException):
    pass

class BotMessageException(BotException):
    pass

class BotQueueException(BotException):
    pass

class BotThreadException(BotException):
    pass

class TelegramBotException(BotException):
    pass

class FacebookBotException(BotException):
    pass

class WhatsappBotException(BotException):
    pass

class BotQueuedMessageException(BotMessageException):
    pass

class BotQueuedMessageResultException(BotQueuedMessageException):
    pass

class BotQueuedMessageInvalidException(BotQueuedMessageException):
    pass

class BotMessageQueueException(BotMessageException):
    pass

class BotMessageQueueFullException(BotMessageQueueException):
    pass

class BotMessageQueueEmptyException(BotMessageQueueException):
    pass

class BotMessageQueueLockException(BotMessageQueueException):
    pass

class BotSendMessageException(BotMessageException):
    pass

class BotReceiveMessageException(BotMessageException):
    pass

class HTTPMessageException(BotMessageException):
    pass

class HTTPMessagePayloadException(HTTPMessageException):
    pass

class HTTPMessageParamsException(HTTPMessageException):
    pass

class HTTPMessageHeadersException(HTTPMessageException):
    pass

class BotStartThreadException(BotThreadException):
    pass

class BotStopThreadException(BotThreadException):
    pass

class TelegramBotSendMessageException(TelegramBotException):
    pass

class FacebookBotSendMessageException(FacebookBotException):
    pass

class WhatsappBotSendMessageException(WhatsappBotException):
    pass




class HTTPMessage:
    def __init__(self, payload:str , params: str = None, headers: str = None):
        self.payload = payload
        self.params = params
        self.headers = headers

class Message:
    def __init__(self, message:str , http_message: HTTPMessage, destId: str, sourceId: str, datetime: datetime):
        self.http_message = http_message 
        self.destId = destId
        self.sourceId = sourceId
        self.datetime = datetime

class QueuedMessage:
    def __init__(self, message, max_store_retries: int = 3):
        self.message = message
        self.result = None
        self.event = threading.Event()
        self.stored_ok = False
        self.store_retries = max_store_retries

    def set_result(self, result: bool):
        self.result = result
        self.event.set()

    def wait_result(self, timeout: Optional[float] = None):
        self.event.wait(timeout)
        return self.result


class OutgoingQueuedMessage(QueuedMessage):
    def __init__(self, message, max_send_retries: int = 3, max_store_retries: int = 3):
        super().__init__(message, max_store_retries)
        self.sent_ok = False
        self.send_retries = max_send_retries


class IncomingQueuedMessage(QueuedMessage):
    def __init__(self, message, max_store_retries: int = 3):
        super().__init__(message, max_store_retries)


class Bot:
    send_message_api: str = None
    token: str = None

    def __init__(self, id: str,
                 on_incoming_message: Optional[Callable[[Message], bool]] = None,
                 on_outgoing_message: Optional[Callable[[Message], bool]] = None):
        self.id = id
        self.outgoing_messages = queue.Queue(maxsize=1000)
        self.incoming_messages = queue.Queue(maxsize=1000)
        self.bot_stop_event = threading.Event()
        self.on_incoming_message = on_incoming_message
        self.on_outgoing_message = on_outgoing_message
        
        self.bot_logger = Logger(name=f"bot-{self.id}", enable_file_handler=True, enable_syslog_handler=True)
        self.bot_logger.config(log_dir=f"./logs/bot-{self.id}", min_level="DEBUG")
        self.bot_logger.info(f"Bot with id={self.id} created")

        self.consumer_out_thread = None
        self.consumer_in_thread = None

        atexit.register(self.stop)

    def start(self, consumer_out_thread_name: str = "BotConsumerOutgoingThread",
              consumer_in_thread_name: str = "BotConsumerIncomingThread",
              daemon: bool = True, **thread_kwargs):
        try:
            if self.consumer_out_thread is None or not self.consumer_out_thread.is_alive():
                self.bot_stop_event.clear()
                self.consumer_out_thread = threading.Thread(
                    target=self.consume_outgoing_queue,
                    name=consumer_out_thread_name,
                    daemon=daemon,
                    **thread_kwargs
                )
                self.consumer_out_thread.start()
                self.bot_logger.info(f"Bot Outgoing Thread '{consumer_out_thread_name}' started")
        except Exception as e:
            self.bot_logger.error(f"Failed to start outgoing thread: {e}")
            raise BotStartThreadException(f"Outgoing thread error: {e}") from e

        try:
            if self.consumer_in_thread is None or not self.consumer_in_thread.is_alive():
                self.bot_stop_event.clear()
                self.consumer_in_thread = threading.Thread(
                    target=self.consume_incoming_queue,
                    name=consumer_in_thread_name,
                    daemon=daemon,
                    **thread_kwargs
                )
                self.consumer_in_thread.start()
                self.bot_logger.info(f"Bot Incoming Thread '{consumer_in_thread_name}' started")
        except Exception as e:
            self.bot_logger.error(f"Failed to start incoming thread: {e}")
            raise BotStartThreadException(f"Incoming thread error: {e}") from e

    def stop(self):
        self.bot_logger.info(f"Stopping bot id={self.id}")
        try:
            self.bot_stop_event.set()
            if self.consumer_out_thread and self.consumer_out_thread.is_alive():
                self.consumer_out_thread.join(timeout=5)
            if self.consumer_in_thread and self.consumer_in_thread.is_alive():
                self.consumer_in_thread.join(timeout=5)
            self.bot_logger.info(f"Bot id={self.id} stopped")
        except Exception as e:
            self.bot_logger.warning(f"Error stopping bot id={self.id}: {e}")
            raise BotStopException(f"Stop failed for bot {self.id}: {e}") from e

    def http_check(self) -> bool:
        if self.bot_stop_event.is_set():
            return False
        if not (self.consumer_out_thread and self.consumer_out_thread.is_alive() and
                self.consumer_in_thread and self.consumer_in_thread.is_alive()):
            return False

        try:
            response = requests.get(self.send_message_api, timeout=5)
            return response.status_code == 200
        except requests.RequestException as e:
            self.bot_logger.error(f"HTTP health check failed: {e}")
            raise BotHealthCheckException(f"Bot HTTP health check error: {e}") from e

    def is_running(self) -> bool:
        return (not self.bot_stop_event.is_set() and
                self.consumer_out_thread and self.consumer_out_thread.is_alive() and
                self.consumer_in_thread and self.consumer_in_thread.is_alive())

    def alive(self) -> bool:
        try:
            return self.is_running() and self.http_check()
        except BotHealthCheckException:
            return False

    def consume_outgoing_queue(self):
        while not self.bot_stop_event.is_set():
            try:
                queued_msg: OutgoingQueuedMessage = self.outgoing_messages.get(block=True)
                if self.bot_stop_event.is_set():
                    break
                
                if not queued_msg.sent_ok:
                    try:
                        payload = queued_msg.message.http_message.payload
                        params = queued_msg.message.http_message.params
                        headers = queued_msg.message.http_message.headers
                        self.bot_logger.info(f"Sending HTTP: {payload}")
                        response = requests.post(self.send_message_api, json=payload, params=params, headers=headers)
                        queued_msg.sent_ok = response.status_code == 200
                    except Exception as e:
                        queued_msg.send_retries -= 1
                        self.bot_logger.error(f"HTTP send failed, retries left={queued_msg.send_retries}: {e}")
                        if queued_msg.send_retries > 0:
                            self.outgoing_messages.put(queued_msg, block=True)
                        else:
                            queued_msg.set_result(False)
                        continue

                if not queued_msg.stored_ok and self.on_outgoing_message:
                    try:
                        stored_ok = self.on_outgoing_message(queued_msg.message)
                        queued_msg.stored_ok = stored_ok
                        queued_msg.set_result(stored_ok)
                    except Exception as e:
                        self.bot_logger.error(f"Outgoing callback error: {e}")
                        queued_msg.store_retries -= 1
                        if queued_msg.store_retries > 0:
                            self.outgoing_messages.put(queued_msg, block=True)
                        else:
                            queued_msg.set_result(False)
            except Exception as e:
                self.bot_logger.error(f"Unexpected error in outgoing processing: {e}")
                raise BotMessageException(f"Outgoing queue processing failed: {e}") from e

    def consume_incoming_queue(self):
        while not self.bot_stop_event.is_set():
            try:
                queued_msg: IncomingQueuedMessage = self.incoming_messages.get(block=True)
                if self.bot_stop_event.is_set():
                    break

                stored_ok = True
                if self.on_incoming_message:
                    try:
                        stored_ok = self.on_incoming_message(queued_msg.message)
                    except Exception as e:
                        self.bot_logger.error(f"Incoming callback error: {e}")
                        stored_ok = False

                if stored_ok:
                    queued_msg.stored_ok = True
                    queued_msg.set_result(True)
                else:
                    queued_msg.store_retries -= 1
                    if queued_msg.store_retries > 0:
                        self.incoming_messages.put(queued_msg, block=True)
                    else:
                        queued_msg.set_result(False)
            except Exception as e:
                self.bot_logger.error(f"Unexpected error in incoming processing: {e}")
                raise BotMessageException(f"Incoming queue processing failed: {e}") from e


    def send_message(self, payload: str, wait: bool = False) -> Optional[bool]:
        msg = Message(http_message=HTTPMessage(payload), destId=self.id, sourceId="Chatbot", datetime=datetime.now())
        queued_msg = OutgoingQueuedMessage(msg)

        try:
            self.outgoing_messages.put(queued_msg, block=False)
        except queue.Full as qfe:
            if not wait:
                self.bot_logger.warning("Outgoing queue full, message skipped")
                raise BotMessageQueueFullException("Outgoing queue full") from qfe
            else:
                try:
                    self.outgoing_messages.put(queued_msg, block=True)
                except Exception as e:
                    self.bot_logger.error(f"Failed to enqueue message: {e2}")
                    raise BotMessageQueueException(f"Failed to enqueue outgoing message: {e2}") from e

        try:
            return queued_msg.wait_result(timeout=10.0) if wait else None
        except Exception as e:
            self.bot_logger.error(f"Failed waiting for message result: {e}")
            raise BotQueuedMessageResultException(f"Waiting result failed: {e}") from e

    def receive_message(self, payload: str, wait: bool = False):
        msg = Message(http_message=HTTPMessage(payload), destId="Chatbot", sourceId=self.id, datetime=datetime.now())
        queued_msg = IncomingQueuedMessage(msg)

        try:
            self.incoming_messages.put(queued_msg, block=False)
        except queue.Full as qfe:
            if not wait:
                self.bot_logger.warning("Incoming queue full, message skipped")
                raise BotMessageQueueFullException("Incoming queue full") from qfe
            else:
                try:
                    self.incoming_messages.put(queued_msg, block=True)
                except Exception as e:
                    self.bot_logger.error(f"Failed to enqueue incoming message: {e}")
                    raise BotQueueException(f"Failed to enqueue incoming message: {e}") from e
    
    def __del__(self):
        if not self.bot_stop_event.is_set():
            self.stop()

    @classmethod
    def deserialize(cls, data):
        if isinstance(data, (str, int, float, bool)) or data is None:
            return data

        if isinstance(data, dict):
            t = data.get("_type")

            if t == "Queue":
                q = queue.Queue(maxsize=1000)
                for item in data["items"]:
                    if item == "...":
                        continue
                    q.put(cls.deserialize(item))
                return q

            if t == "HTTPMessage":
                return HTTPMessage(
                    payload=data.get("payload"),
                    params=data.get("params"),
                    headers=data.get("headers")
                )

            if t == "Message":
                return Message(
                    message=data.get("message"),
                    http_message=cls.deserialize(data.get("http_message")),
                    destId=data.get("destId"),
                    sourceId=data.get("sourceId"),
                    datetime=datetime.fromisoformat(data.get("datetime"))
                )

            if t == "QueuedMessage":
                qm = QueuedMessage(cls.deserialize(data.get("message")))
                qm.result = data.get("result")
                return qm

            if t == "Bot":
                bot = Bot(id=data.get("id"))
                bot.send_message_api = data.get("send_message_api")
                bot.token = data.get("token")

                bot.outgoing_messages = cls.deserialize(data.get("outgoing_messages"))
                bot.incoming_messages = cls.deserialize(data.get("incoming_messages"))
                return bot
            
            return {k: cls.deserialize(v) for k, v in data.items() if k != "_type"}

        if isinstance(data, list):
            return [cls.deserialize(x) for x in data]

        raise ValueError(f"Unable to deserialize: {data}")

    def serialize(self, max_queue_items=None):
        def serialize_obj(value):
            if isinstance(value, (str, int, float, bool)) or value is None:
                return value

            if isinstance(value, queue.Queue):
                items = list(value.queue)
                if max_queue_items is not None and len(items) > max_queue_items:
                    items = items[:max_queue_items] + ["..."]
                return {
                    "_type": "Queue",
                    "size": len(list(value.queue)),
                    "items": [serialize_obj(it) for it in items]
                }

            if isinstance(value, HTTPMessage):
                return {
                    "_type": "HTTPMessage",
                    "payload": value.payload,
                    "params": value.params,
                    "headers": value.headers
                }

            if isinstance(value, Message):
                return {
                    "_type": "Message",
                    "message": getattr(value, "message", None),
                    "destId": value.destId,
                    "sourceId": value.sourceId,
                    "datetime": str(value.datetime),
                    "http_message": serialize_obj(value.http_message)
                }

            if isinstance(value, QueuedMessage):
                return {
                    "_type": "QueuedMessage",
                    "result": value.result,
                    "message": serialize_obj(value.message)
                }

            return str(value)

        return {
            "class": self.__class__.__name__,
            "attributes": {attr: serialize_obj(val) for attr, val in self.__dict__.items()}
        }





class TelegramBot(Bot):
    def __init__(self, id: str):
        super().__init__(id=id)
        

    def send_message(self, text):
        payload = {
            "chat_id": self.id,
            "text": text
        }
        return super().send_message(payload=payload)

class FacebookBot(Bot):
    def __init__(self, str, id: str):
        super().__init__(id=id)
    
    def send_message(self, text):
        payload = {
            'recipient': {'id': self.id},
            'message': {'text': text},
            'messaging_type': 'RESPONSE'
        }
        params = {'access_token': self.token}
        return super().send_message(payload=payload, params=params)

class WhatsappBot(Bot):
    def __init__(self, str, id: str):
        super().__init__(id=id)
    
    def send_message(self, text):
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        payload = {
            'messaging_product': 'whatsapp',
            'to': self.id,
            'text': {'body': text}
        }
        return super().send_message(payload=payload, headers=headers)
    


class BotManager:
    
    def __init__(self, run_cycle_time: float = 1.0):
        self.bots: Dict[str, Dict[str, Bot]] = {
            "telegram": {},
            "facebook": {},
            "whatsapp": {}
        }
        self.run_cycle_time = run_cycle_time
        self.run_thread: Optional[threading.Thread] = None
        self.bot_manager_stop_event = threading.Event()
        self.bot_manager_logger = Logger(
            name=f"bot-manager", enable_file_handler=True, enable_syslog_handler=True
        )
        self.bot_manager_logger.config(min_level="DEBUG")
        self.bot_manager_logger.info("Bot Manager created")
        atexit.register(self.stop)
    
    def start(self, thread_name: str = "BotManagerThread", daemon: bool = True, **thread_kwargs):
        try:
            if self.run_thread is None or not self.run_thread.is_alive():
                self.bot_manager_stop_event.clear()
                self.run_thread = threading.Thread(
                    target=self.run,
                    name=thread_name,
                    daemon=daemon,
                    **thread_kwargs
                )
                self.run_thread.start()
                self.bot_manager_logger.info(f"Bot Manager Thread '{thread_name}' started")
        except Exception as e:
            self.bot_manager_logger.error(f"Failed to start Bot Manager thread: {e}")
            raise BotManagerStartException(f"Bot Manager start failed: {e}") from e

    def run(self):
        while not self.bot_manager_stop_event.is_set():
            try:
                sleep(self.run_cycle_time)
                self.bot_manager_logger.debug(f"Current Bots - {self.bots_info_str()}")
                self.maintain_alive_bots()
            except Exception as e:
                self.bot_manager_logger.warning(f"Exception in Bot Manager run loop: {e}")
                raise BotManagerThreadException(f"Run loop error: {e}") from e

    def stop(self):
        self.bot_manager_logger.info("Stopping Bot Manager...")
        self.bot_manager_stop_event.set()

        if self.run_thread and self.run_thread.is_alive():
            try:
                self.run_thread.join(timeout=5)
            except Exception as e:
                self.bot_manager_logger.warning(f"Error stopping run thread: {e}")
                raise BotManagerStopException(f"Stopping run thread failed: {e}") from e

        
        self.terminate_bots()
        self.bot_manager_logger.info("Bot Manager terminated")


    def list_bots(self) -> Dict[str, Dict[str, str]]:
        return {
            bot_type: {id: bot.__class__.__name__ for id, bot in bots.items()}
            for bot_type, bots in self.bots.items()
        }

    def bots_info_json(self, max_queue_items=None):
        data = {}
        for bot_type, bots in self.bots.items():
            data[bot_type] = {}
            for bot_id, bot in bots.items():
                data[bot_type][bot_id] = bot.serialize(max_queue_items)
        return json.dumps(data, indent=2)

    def bots_info_str(self, max_queue_items=5) -> str:
        parts = []
        for bot_type, bots in self.bots.items():
            for bot_id, bot in bots.items():
                ser = bot.serialize(max_queue_items)
                attrs = ", ".join(f"{k}={v}" for k, v in ser["attributes"].items())
                parts.append(f"[BotType={bot_type}, BotId={bot_id}, Class={ser['class']}, {attrs}]")
        return " | ".join(parts)
    
    def maintain_alive_bots(self) -> bool:
        for bot_type, bots in list(self.bots.items()):
            for bot_id, bot in list(bots.items()):
                try:
                    if not bot.alive():
                        self.bot_manager_logger.warning(f"Bot {bot_id} of type {bot_type} not alive, restarting...")
                        self.terminate_and_restart_bot(bot_type, bot_id)
                except Exception as e:
                    self.bot_manager_logger.critical(f"Unable to maintain bot {bot_id} alive: {e}")
                    raise BotManagerAliveCheckException(f"Failed to maintain bot {bot_id}: {e}") from e
        return True
        
    def check_alive_bots(self) -> bool:
        for bot_type, bots in list(self.bots.items()):
            for id, bot in list(bots.items()):
                try:
                    if not bot.alive():
                        self.bot_manager_logger.warning(
                            f"Bot {id} of type {bot_type} is not alive"
                        )
                        return False
                except Exception as e:
                    self.bot_manager_logger.warning(
                        f"Unable to check bot {id} of type {bot_type} aliveness: {e}"
                    )
        return True
        
    def stop_bots(self):
        for bot_type, bots in self.bots.items():
            for id, bot in list(bots.items()):
                try:
                    bot.stop()
                except Exception as e:
                    self.bot_manager_logger.warning(
                        f"Error stopping bot {id} of type {bot_type}: {e}"
                    )
        self.bots.clear()

    def create_bot(self, bot_type: str, id: str,
                   on_incoming_message: Optional[Callable[[Message], bool]] = None,
                   on_outgoing_message: Optional[Callable[[Message], bool]] = None) -> Bot:
        bot_type = bot_type.lower()
        try:
            if bot_type == "telegram":
                bot = TelegramBot(id, on_incoming_message, on_outgoing_message)
            elif bot_type == "facebook":
                bot = FacebookBot(id, on_incoming_message, on_outgoing_message)
            elif bot_type == "whatsapp":
                bot = WhatsappBot(id, on_incoming_message, on_outgoing_message)
            else:
                raise BotManagerException(f"Unsupported bot type: {bot_type}")
            self.bots[bot_type][id] = bot
            return bot
        except Exception as e:
            self.bot_manager_logger.error(f"Failed to create bot {id} of type {bot_type}: {e}")
            raise BotManagerBotException(f"Bot creation failed: {e}") from e
        
    def create_if_not_exist_and_start_bot(self, bot_type: str, id: str) -> Bot:
        bot = self.create_if_not_exist_bot(bot_type=bot_type, id=id)
        bot.start(consumer_out_thread_name=f"BotConsumerOutgoingThread-{id}", consumer_in_thread_name=f"BotConsumerIncomingThread-{id}", daemon=False)
        return bot

    def create_if_not_exist_bot(self, bot_type: str, id: str) -> Bot:
        bot = self.bots.get(bot_type, {}).get(id)
        if not bot:
            bot = self.create_bot(bot_type=bot_type, id=id)
            return bot
        else:
            return bot

    def start_bot(self, bot_type: str, id: str,
                  on_incoming_message: Optional[Callable[[Message], bool]] = None,
                  on_outgoing_message: Optional[Callable[[Message], bool]] = None) -> Bot:
        bot = self.create_if_not_exist_bot(bot_type, id)
        if on_incoming_message:
            bot.on_incoming_message = on_incoming_message
        if on_outgoing_message:
            bot.on_outgoing_message = on_outgoing_message
        try:
            bot.start(consumer_out_thread_name=f"BotOutThread-{id}", consumer_in_thread_name=f"BotInThread-{id}", daemon=False)
            return bot
        except Exception as e:
            self.bot_manager_logger.error(f"Failed to start bot {id}: {e}")
            raise BotManagerStartException(f"Bot start failed: {e}") from e
    
    def get_bot(self, bot_type: str, id: str) -> Union[Bot, None]:
        return self.bots.get(bot_type, {}).get(id)
    
    def check_alive_bot(self, bot_type: str, id: str) -> bool:
        bot = self.bots.get(bot_type, {}).get(id)
        if not bot:
            self.bot_manager_logger.warning(f"Bot {id} of type {bot_type} not found")
            return False

        try:
            if not bot.alive():
                self.bot_manager_logger.warning(f"Bot {id} of type {bot_type} not alive")
                return False
            return True
        except Exception as e:
            self.bot_manager_logger.warning(
                f"Unable to check bot {id} of type {bot_type} aliveness: {e}"
            )
            return False
    
    def terminate_and_restart_bot(self, bot_type: str, id: str) -> Bot: 
        self.terminate_bot(bot_type, id)
        self.bot_manager_logger.info(f"Restarting bot {id} of type {bot_type}")
        return self.create_bot(bot_type, id)
    
    def terminate_bot(self, bot_type: str, id: str):
        bot = self.get_bot(bot_type, id)
        if bot:
            try:
                bot.stop()
            except Exception as e:
                self.bot_manager_logger.warning(f"Error stopping bot {id} of type {bot_type}: {e}")
            del self.bots[bot_type][id]
            self.bot_manager_logger.info(f"Terminated bot {id} of type {bot_type}")
    
    def terminate_bot_by_instance(self, bot: Bot):
        for bot_type, bots in self.bots.items():
            for id, b in list(bots.items()):
                if b is bot:
                    self.terminate_bot(bot_type, id)
                    return
    
    def send_message_on_bot(self, bot_type: str, id: str, payload: str, params: str = None, headers: str = None) -> int:
        bot = self.create_if_not_exist_bot(bot_type, id)
        try:
            return bot.send_message(payload=payload)
        except Exception as e:
            self.bot_manager_logger.error(f"Send message failed on bot {id}: {e}")
            raise BotManagerBotException(f"Send message failed: {e}") from e

    def receive_message_from_bot(self, bot_type: str, id: str, payload: str) -> int:
        bot = self.create_if_not_exist_bot(bot_type, id)
        try:
            return bot.receive_message(payload=payload)
        except Exception as e:
            self.bot_manager_logger.error(f"Receive message failed on bot {id}: {e}")
            raise BotManagerBotException(f"Receive message failed: {e}") from e
        
    def __del__(self):
        self.stop()   


TelegramBot.send_message_api = environ.TELEGRAM_BOT_SEND_MESSAGE_API
WhatsappBot.send_message_api = environ.WHATSAPP_BOT_SEND_MESSAGE_API
FacebookBot.send_message_api = environ.FACEBOOK_BOT_SEND_MESSAGE_API
TelegramBot.token = environ.TELEGRAM_TOKEN
WhatsappBot.token = environ.WHATSAPP_TOKEN
FacebookBot.token = environ.FACEBOOK_TOKEN



bot_manager = BotManager(run_cycle_time=environ.BOT_MANAGER_RUN_TIMEOUT)
bot_manager.start()


'''

bot1 = bot_manager.create_bot("telegram", id="chatid1")
bot2 = bot_manager.create_bot("telegram", id="chatid2")
bot3 = bot_manager.create_bot("telegram", id="chatid3")

status = bot_manager.send_message_on_bot("telegram", "user1", "")
print("Status Telegram user1:", status)

status = bot_manager.get_bot("telegram", "user1").send_message("")

status = bot_manager.send_message_on_bot("whatsapp", "client2", "")
print("Status WhatsApp client2:", status)

print(bot_manager.list_bots())

'''



