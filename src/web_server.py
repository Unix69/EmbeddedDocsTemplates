import atexit
from collections import defaultdict
import queue
import sys
import threading
from typing import Optional, Union

from datetime import datetime
import requests
from flask import Flask, request
from flask import render_template_string
from sqlalchemy import func


import bot
from bot import bot_manager

from exception import ChatbotException
import llm
import env
from env import environ
import configurator
from configurator import config, ConfigurationVerifyNgrokException, ConfigurationStopNgrokException, ConfigurationCheckNgrokException, ConfigurationStartNgrokException, ConfigurationException
import database
import web_client
import bot
from bot import bot

import logger
from logger import Logger, main_logger



class WebAppException(ChatbotException): pass
class WebAppConfigurationException(WebAppException): pass
class WebAppVerifyException(WebAppException): pass
class WebAppRunException(WebAppException): pass
class WebAppStartException(WebAppException): pass
class WebAppStopException(WebAppException): pass



class WebApp:
    def __init__(self, tg_bot_webhook_method: str, fb_bot_webhook_method: str, wp_bot_webhook_method: str, srv_reservation_method: str, srv_event_info_method: str, srv_shutdown_method: str, 
                 srv_proto="https", srv_name="ChatbotApp", srv_host="127.0.0.1", srv_port=5000, debug=True):
        self.srv_host = srv_host
        self.srv_port = srv_port
        self.srv_proto = srv_proto
        self.webApp = Flask(srv_name)

        self.tg_bot_webhook_method = tg_bot_webhook_method
        self.fb_bot_webhook_method = fb_bot_webhook_method
        self.wp_webhook_method = wp_bot_webhook_method
        self.srv_reservation_method = srv_reservation_method
        self.srv_event_info_method = srv_event_info_method
        self.srv_shutdown_method = srv_shutdown_method
        self.srv_shutdown_api = f"{self.srv_proto}://{self.srv_host}:{self.srv_port}/{self.srv_shutdown_method}"

        self.webapp_thread = None
        
        self.webapp_logger = Logger(name="webapp", enable_file_handler=True, enable_syslog_handler=True)
        self.webapp_logger.config()
        
        self._register_routes()

    def _register_routes(self):
        @self.webApp.route(self.tg_bot_webhook_method, methods=["POST"])
        def telegram_webhook():
            if request.method == 'POST':
                
                update = request.json  # Ricezione dei dati via webhook
                chat_id = update["message"]["chat"]["id"]
                user_id = update["message"]["from"]["id"]
                received_message = update["message"]["text"]  # Messaggio ricevuto

                # Ottieni la data e l'ora corrente
                current_datetime = datetime.now()
                current_date = current_datetime.strftime("%A, %d %B %Y")  # Giorno, data (es. Lunedì, 26 Aprile 2025)
                current_time_str = current_datetime.strftime("%H:%M:%S")  # Ora in formato HH:MM:SS

                bot = bot_manager.create_if_not_exist_and_start_bot("telegram", id=chat_id)
                bot_manager.get_bot("telegram", chat_id).receive_message(payload=received_message, datetime=current_datetime)

                session = database.Session()  # <<--- crea la sessione
                eventi = session.query(database.Event).all()
                eventi_str = ""
                for evento in eventi:
                    eventi_str += f"Evento: {evento.name}\n"
                    eventi_str += f"Descrizione: {evento.description}\n"
                    eventi_str += f"Data e Ora: {evento.date_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    eventi_str += f"Location: {evento.location}\n"
                    eventi_str += f"Posti Totali: {evento.total_sits}\n"
                    eventi_str += f"Posti Disponibili: {evento.available_sits}\n"
                    eventi_str += "---------------------------\n" 
            
                # event_str = database.get_events()
                # respose = ai.process_message(received_message, event_str)

                # TODO fare una funzione AI che accetta come parametro la event_str e tutti quelli necessari da request (contenuto in weebhok) e torna il messaggio al webhook, da ioltrare, 
                prompt2=f'''Se l'utente sta prenotando uno degli eventi in "{eventi_str}" nel suo messaggio: "{received_message}", estrai le informazioni che ti fornisce e se non le dà tutte, omettile. Foriscile nella forma:
                nome: ..., 
                evento: ..., 
                numero posti: .... 
                In questo messaggio fornisci SOLO le info che ti sono state fornite in "{received_message}" senza altre parole in una unica riga.'''
                booking_state = llm.ask_llm3(user_id, prompt2)
                info_message = f"{booking_state}"
                print(f"Stato prenotazione utente {user_id}: {booking_state}")
                user_info = llm.info_extraction(user_id, info_message)
                print(f"Stato prenotazione utente {user_id}: {user_info}")

                if all([user_info['name'], user_info['event'], user_info['number_sits']]):
                    database.db.salva_prenotazione(user_info['name'], user_info['event'], user_info['number_sits'])
                    #uil
                    # Genera la risposta finale con GPT
                    prompt_finale = f"Conferma la prenotazione per {user_info['name']} all'evento {user_info['event']} con {user_info['number_sits']} posti."
                    #standard_text = f"{prompt_finale}"
                    bot.send_message(chat_id, prompt_finale)
                else:
                    prompt = f'''L'utente ha scritto: "{received_message}", il giorno è "{current_date}" e l'ora è "{current_time_str}".
                    Per prenotare l'utente deve fornire nome, cognome, evento e numero posti, non necessariamente in un unico messaggio, fino a riempire tutti i campi del dizionario "{user_info}". 
                    Questa è la tabella degli eventi "{eventi_str}".
                    Se il numero di posti richiesti per uno degli eventi disponibili in "{eventi_str}" è maggiore dei posti disponibili, rispondi con "Posti non disponibili" e dicendo quanti posti disponibili rimangono. 
                    Se l'utente chiede informazioni sugli eventi disponibili in "{eventi_str}", forniscigliele dando SOLO le info che ti sta chiedendo e includendo qualche emoji.
                    Solo al primo messaggio presentati come Chat CPI, il chatbot ufficiale del circolo Peppino Impastato. 
                    Usa un linguaggio inclusivo con la schwa (ə).
                    Rendi la risposta il più sintentica possibile.
                    Non dare MAI il messaggio di prenotazione effettuata.
                    Se l'utente vuole cancellare una prenotazione, devi dire di rivolgersi al numero 3276233773
                    '''
                    answer = llm.ask_llm(user_id, prompt)
                    
                    bot_manager.get_bot("telegram", chat_id).send_message(payload=f"{answer}")

                session.close()    
                return "ok", 200
            
        @self.webApp.route(self.fb_bot_webhook_method, methods=['GET', 'POST'])
        def messenger_webhook():
            if request.method == 'GET':
                #print("Token ricevuto da Facebook:", request.args.get('hub.verify_token'))
                if request.args.get('hub.verify_token') == env.environ.FACEBOOK_TOKEN:
                    return request.args.get('hub.challenge'), 200
                message = "Benvenuto nella pagina di esempio Flask!"
                return render_template_string(web_client.html_home, message=message)

            elif request.method == 'POST':
                
                #bot_manager.create_if_not_exist_bot("messenger", id="user1")
                
                data = request.get_json()
                #print("Dati ricevuti da Facebook:", data)  # <-- LOG IMPORTANTE
                session = database.Session()  # <<--- crea la sessione

                # Ottieni la data e l'ora corrente
                current_datetime = datetime.now()
                current_date = current_datetime.strftime("%A, %d %B %Y")  # Giorno, data (es. Lunedì, 26 Aprile 2025)
                current_time_str = current_datetime.strftime("%H:%M:%S")  # Ora in formato HH:MM:SS
                            
                eventi = session.query(database.Event).all()
                eventi_str = ""
                for evento in eventi:
                    eventi_str += f"Evento: {evento.name}\n"
                    eventi_str += f"Descrizione: {evento.description}\n"
                    eventi_str += f"Data e Ora: {evento.date_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    eventi_str += f"Location: {evento.location}\n"
                    eventi_str += f"Posti Totali: {evento.total_sits}\n"
                    eventi_str += f"Posti Disponibili: {evento.available_sits}\n"
                    eventi_str += "---------------------------\n" 
                
                # Messaggio di risposta
                if data.get('object') == 'page':
                    for entry in data.get('entry', []):
                        for messaging_event in entry.get('messaging', []):
                            sender_id = messaging_event['sender']['id']
                            bot = bot_manager.create_if_not_exist_and_start_bot("telegram", id=sender_id)
                            if 'message' in messaging_event and 'text' in messaging_event['message']:
                                received_message = messaging_event['message']['text']
                                # Messaggio di risposta
                                bot_manager.get_bot("facebook", sender_id).receive_message(payload=received_message, datetime=current_datetime)
                                prompt2=f'''Se l'utente sta prenotando uno degli eventi in "{eventi_str}" nel suo messaggio: "{received_message}", estrai le informazioni che ti fornisce e se non le dà tutte, omettile. Foriscile nella forma:
                                nome: ..., 
                                evento: ..., 
                                numero posti: .... 
                                In questo messaggio fornisci SOLO le info che ti sono state fornite in "{received_message}"  senza altre parole in una unica riga.'''
                                booking_state = llm.ask_llm3(sender_id, prompt2)
                                info_message = f"{booking_state}"
                                print(f"Stato prenotazione utente {sender_id}: {booking_state}")
                                user_info = database.db.info_extraction(sender_id, info_message)
                                print(f"Stato prenotazione utente {sender_id}: {user_info}")

                                if all([user_info['name'], user_info['event'], user_info['number_sits']]):
                                    database.db.salva_prenotazione(user_info['name'], user_info['event'], user_info['number_sits'])
                    
                                    # Genera la risposta finale con GPT
                                    prompt_finale = f"Conferma la prenotazione per {user_info['name']} all'evento {user_info['event']} con {user_info['number_sits']} posti."
                                    #standard_text = f"{prompt_finale}"
                                    bot_manager.get_bot("facebook", sender_id).send_message(payload=prompt_finale, datetime=current_datetime)
                                else:
                                    prompt = f'''L'utente ha scritto: "{received_message}", il giorno è "{current_date}" e l'ora è "{current_time_str}".
                                    Per prenotare l'utente deve fornire nome, cognome, evento e numero posti, non necessariamente in un unico messaggio, fino a riempire tutti i campi del dizionario "{user_info}". 
                                    Questa è la tabella degli eventi "{eventi_str}".
                                    Se il numero di posti richiesti per uno degli eventi disponibili in "{eventi_str}" è maggiore dei posti disponibili, rispondi con "Posti non disponibili" e dicendo quanti posti disponibili rimangono. 
                                    Se l'utente chiede informazioni sugli eventi disponibili in "{eventi_str}", forniscigliele dando SOLO le info che ti sta chiedendo e includendo qualche emoji.
                                    Solo al primo messaggio presentati come Chat CPI, il chatbot ufficiale del circolo Peppino Impastato. 
                                    Usa un linguaggio inclusivo con la schwa (ə).
                                    Rendi la risposta il più sintentica possibile.
                                    Non dare MAI il messaggio di prenotazione effettuata.
                                    Se l'utente vuole cancellare una prenotazione, devi dire di rivolgersi al numero 3276233773
                                    '''
                                    answer = llm.ask_llm(sender_id, prompt)
                                    bot_manager.get_bot("facebook", sender_id).send_message(payload=f"{answer}", datetime=current_datetime)

                                session.close()    
                            
                return 'EVENT_RECEIVED', 200

        @self.webApp.route(self.wp_webhook_method, methods=['GET', 'POST'])
        def whatsapp_webhook():
            
            if request.method == 'GET':
                if request.args.get('hub.verify_token') == env.environ.WHATSAPP_TOKEN:
                    return request.args.get('hub.challenge'), 200
                return 'Invalid verification token', 403

            elif request.method == 'POST':
                data = request.get_json()
                #print("Messaggio ricevuto da WhatsApp:", data)
                session = database.Session()  # <<--- crea la sessione

                # Ottieni la data e l'ora corrente
                current_datetime = datetime.now()
                current_date = current_datetime.strftime("%A, %d %B %Y")  # Giorno, data (es. Lunedì, 26 Aprile 2025)
                current_time_str = current_datetime.strftime("%H:%M:%S")  # Ora in formato HH:MM:SS
                
                #bot_manager.get_bot("whatsapp", chat_id, client_id).receive_message(received_message, chat_id, client_id, current_time, current_date)

                eventi = session.query(database.Event).all()
                eventi_str = ""
                for evento in eventi:
                    eventi_str += f"Evento: {evento.name}\n"
                    eventi_str += f"Descrizione: {evento.description}\n"
                    eventi_str += f"Data e Ora: {evento.date_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    eventi_str += f"Location: {evento.location}\n"
                    eventi_str += f"Posti Totali: {evento.total_sits}\n"
                    eventi_str += f"Posti Disponibili: {evento.available_sits}\n"
                    eventi_str += "---------------------------\n" 

                if data.get("object") == "whatsapp_business_account":
                    for entry in data.get("entry", []):
                        for change in entry.get("changes", []):
                            value = change.get("value", {})
                            messages = value.get("messages", [])
                            for message in messages:
                                sender_id = message["from"]  # ← questo è il numero WhatsApp del mittente
                                bot = bot_manager.create_if_not_exist_and_start_bot("telegram", id=sender_id)
                                if message.get("text"):
                                    received_message = message["text"]["body"]
                                    bot.receive_message(payload=received_message, datetime=current_datetime)
                                    prompt2=f'''Se l'utente sta prenotando uno degli eventi in "{eventi_str}" nel suo messaggio: "{received_message}", estrai le informazioni che ti fornisce e se non le dà tutte, omettile. Foriscile nella forma:
                                    nome: ..., 
                                    evento: ..., 
                                    numero posti: .... 
                                    In questo messaggio fornisci SOLO le info che ti sono state fornite in "{received_message}" senza altre parole in una unica riga.
                                    Se l'utente sta chidendo informazioni sugli eventi o sta chiedendo di cancellare una prenotazione rispondi con: 
                                    nome: ..., 
                                    evento: ..., 
                                    numero posti: ....  
                                    ma lasciando tutti i campi vuoti.'''
                                    booking_state = llm.ask_llm3(sender_id, prompt2)
                                    info_message = f"{booking_state}"
                                    print(f"Stato prenotazione utente {sender_id}: {booking_state}")
                                    user_info = database.db.info_extraction(sender_id, info_message)
                                    print(f"Stato prenotazione utente {sender_id}: {user_info}")

                                    if all([user_info['name'], user_info['event'], user_info['number_sits']]):
                                        database.db.salva_prenotazione(user_info['name'], user_info['event'], user_info['number_sits'])
                    
                                        # Genera la risposta finale con GPT
                                        prompt_finale = f"Conferma la prenotazione per {user_info['name']} all'evento {user_info['event']} con {user_info['number_sits']} posti."
                                        #standard_text = f"{prompt_finale}"
                                        
                                        bot.send_message(payload=prompt_finale, datetime=current_datetime)
                                    else:
                                        prompt = f'''L'utente ha scritto: "{received_message}", il giorno è "{current_date}" e l'ora è "{current_time_str}".
                                        Per prenotare l'utente deve fornire nome, cognome, evento e numero posti, non necessariamente in un unico messaggio, fino a riempire tutti i campi del dizionario "{user_info}". 
                                        Questa è la tabella degli eventi "{eventi_str}".
                                        Se il numero di posti richiesti per uno degli eventi disponibili in "{eventi_str}" è maggiore dei posti disponibili, rispondi con "Posti non disponibili" e dicendo quanti posti disponibili rimangono. 
                                        Se l'utente chiede informazioni sugli eventi disponibili in "{eventi_str}", forniscigliele dando SOLO le info che ti sta chiedendo e includendo qualche emoji.
                                        Solo al primo messaggio presentati come Chat CPI, il chatbot ufficiale del circolo Peppino Impastato. 
                                        Usa un linguaggio inclusivo con la schwa (ə).
                                        Rendi la risposta il più sintentica possibile.
                                        Non dare MAI il messaggio di prenotazione effettuata.
                                        Se l'utente vuole cancellare una prenotazione, devi dire di rivolgersi al numero 3276233773
                                        '''
                                        answer = llm.ask_llm(sender_id, prompt)
                                        bot.send_message(payload=f"{answer}", datetime=current_datetime)

                            session.close()    

                return 'EVENT_RECEIVED', 200

        @self.webApp.route('/')
        def home():
            return render_template_string(web_client.html_home)

        # Route che gestisce le operazioni sulla stessa pagina
        @self.webApp.route(self.srv_reservation_method, methods=['GET', 'POST'])
        def reservate():
            session = database.Session()  
            prenotazione = None
            somma_posti = None
            messaggio = None

            if request.method == 'POST':
                azione = request.form.get('azione')

                if azione == 'verifica':  # Verifica prenotazione
                    nome_verifica = request.form['nome_verifica']
                    session = database.Session()
                    prenotazione = session.query(database.Booking).filter(database.Booking.name.ilike(nome_verifica)).all()
                    session.close()

                    if not prenotazione:
                        messaggio = f"Non è stata trovata nessuna prenotazione per il nome «{nome_verifica}»."
                    else:
                        # Costruiamo un messaggio riepilogativo di tutte le prenotazioni
                        lines = [f"Prenotazioni trovate per «{nome_verifica}»:"]
                        for p in prenotazione:
                            lines.append(f"- {p.name} → evento «{p.event}», {p.number_sits} posti")
                        messaggio = "\n".join(lines)

                elif azione == 'cancella':  # Cancellazione prenotazione
                    nome_cancellazione = request.form['nome_cancellazione']
                    session = database.Session()
                    prenotazione = session.query(database.Booking).filter_by(name=nome_cancellazione).first()

                    if prenotazione:
                        session.delete(prenotazione)
                        session.commit()
                        messaggio = f"La prenotazione per {nome_cancellazione} è stata cancellata con successo."
                    else:
                        messaggio = f"Non è stata trovata nessuna prenotazione per il nome {nome_cancellazione}."

                    session.close()

                elif azione == "inserisci":
                    nome = request.form.get("nome_inserimento")
                    evento = request.form.get("evento_inserimento")
                    posti = request.form.get("posti_inserimento")
                    session = database.Session()

                    try:
                        posti = int(posti)
                        nuova_prenotazione = database.Booking(name=nome, event=evento, number_sits=posti)
                        session.add(nuova_prenotazione)
                        event = session.query(database.Event).filter_by(name=evento).first()
                        event.available_sits -= posti
                        session.commit()
                        messaggio = f"Prenotazione per {nome} all'evento '{evento}' aggiunta con successo."

                    except Exception as e:
                        session.rollback()
                        messaggio = f"Errore durante l'inserimento: {e}"

                    session.close()            

                elif azione == 'somma_posti':  # Somma dei posti prenotati per evento
                    session = database.Session()
                    try:
                        somma_posti = (
                        session.query(database.Booking.event, func.sum(database.Booking.number_sits).label('total_posti'))
                        .group_by(database.Booking.event)
                        .all()
                        )
                    finally:
                        session.close()

            #Recupera tutte le prenotazioni per visualizzarle sempre
            prenotazioni_per_evento = defaultdict(list)
            for p in session.query(database.Booking).order_by(database.Booking.event).all():
                prenotazioni_per_evento[p.event].append(p)
            session.close()

            return render_template_string(web_client.html_reservation, prenotazione=prenotazione, somma_posti=somma_posti, messaggio=messaggio,prenotazioni_per_evento=prenotazioni_per_evento )


        @self.webApp.route(self.srv_event_info_method, methods=["GET", "POST"])
        def get_event_info():
            session = database.Session()  # <<--- crea la sessione
            messaggio = None

            if request.method == "POST":
                nome_evento = request.form.get("nome_evento")  
                descrizione = request.form.get("descrizione_evento")
                luogo = request.form.get("location_evento")
                posti_disponibili = request.form.get("posti_disponibili")
                posti_totali = request.form.get("posti_totali")
                data_evento = request.form.get("data_evento")

                print(nome_evento)
                print(descrizione)
                print(data_evento)

                try:
                    # Conversione robusta della data
                    data_evento = data_evento.strip().replace(":", "-", 2)
                    data_evento = datetime.strptime(data_evento, "%Y-%m-%d %H:%M:%S")
                    posti_disponibili = int(posti_disponibili)
                    posti_totali = int(posti_totali)
            
                    try:
                        nuovo_evento = database.Event(
                            name=nome_evento,
                            description=descrizione,
                            location=luogo,
                            available_sits=posti_disponibili,
                            total_sits=posti_totali,
                            date_time=data_evento,
                        )
                    except Exception as e:
                        session.rollback()
                        messaggio = f"Exception: {e}"
                        print(messaggio)

                    session.add(nuovo_evento)
                    session.commit()
                    messaggio = f"Evento '{nome_evento}' aggiunto con successo."
                    print(messaggio)
                except ValueError as ve:
                    session.rollback()
                    messaggio = f"Errore nel formato della data: {ve}"
                    print(messaggio)
                except SQLAlchemyError as se:
                    session.rollback()
                    messaggio = f"Errore nel salvataggio sul database: {se}"
                    print(messaggio)
                except Exception as e:
                    session.rollback()
                    messaggio = f"Exception: {e}"
                    print(messaggio)


            # Recupera sempre tutti gli eventi (anche dopo errori)
            eventi = session.query(database.Event).all()
            session.close()

            return render_template_string(web_client.html_events, eventi=eventi, messaggio=messaggio)
        
        @self.webApp.route("/__shutdown__", methods=["GET"])
        def shutdown():
            shutdown_func = request.environ.get("werkzeug.server.shutdown")
            if shutdown_func is None:
                raise RuntimeError("Not running with the Werkzeug Server")
            shutdown_func()
            return "Server shutting down..."

    def start(self, **kwargs):
        if self.webapp_thread and self.webapp_thread.is_alive():
            main_logger.warning("Flask già in esecuzione")
            return

        def run_app():
            main_logger.info(f"Starting App on http://{self.srv_host}:{self.srv_port}")
            self.webApp.run(host=self.srv_host, port=self.srv_port, use_reloader=False, **kwargs)
            main_logger.info("App stopped")

        self.webapp_thread = threading.Thread(target=run_app, daemon=True)
        self.webapp_thread.start()

    
    def configure(self):
        try:
            main_logger.info("Configuring App")
            
            config.configure()
            self.webapp_logger.config(min_level="DEBUG", encoding="utf-8")
            
            main_logger.info("Configuring App complete successfully")
        except ConfigurationException as ce:
            main_logger.critical(msg=ce, exc_info=True)
            raise ce
        except Exception as e:
            main_logger.critical(msg=e, exc_info=True)
            raise e

    def verify(self):
        try:
            main_logger.info("Verifing App")
            config.verify_ngrok()
            main_logger.info("Verify App complete successfully")
        except ConfigurationVerifyNgrokException as vne:
            main_logger.critical("Verify Ngrok failed")
            raise vne
        except ConfigurationException as ce:
            main_logger.critical(msg=ce, exc_info=True)
        except Exception as e:
            main_logger.critical(msg=e, exc_info=True)
            raise e
        
    def stop(self):
        try:
            requests.get(self.srv_shutdown_api)
        except Exception:
            pass

        if self.webapp_thread:
            self.webapp_thread.join(timeout=5)
            






'''


class Network:
        network_queue = queue.Queue()
        network_stop_event = threading.Event()
        network_condition = threading.Condition()
        network_thread: Optional[threading.Thread] = None

        def __init__(self):
            self._configured = False

        def config(self):
            if self._configured:
                return

            try:
                self._configured = True

            except Exception as e:
                raise e
        
        def verifyUrl(self, url: str) :
            try:
                return True
            except Exception as e:
                raise e
        


        def verifyConnection(self) -> bool:
            try:
                return True
            except Exception as e:
                raise e

        @classmethod
        def network_manager_run(cls):
            while not cls.network_stop_event.is_set():
                with cls.network_condition:
                    try:
                        pass
                    except Exception as e:
                        print(f"{e}", file=sys.stderr)

        @classmethod
        def start_network_manager(cls, thread_name: str = "NetworkThread", daemon: bool = True, **thread_kwargs):
            try:
                if cls.network_thread is None or not cls.network_thread.is_alive():
                    cls.network_stop_event.clear()
                    cls.network_thread = threading.Thread(
                        target=cls.network_manager_run,
                        name=thread_name,
                        daemon=daemon,
                        **thread_kwargs
                    )
                    cls.network_thread.start()
                print(f"Networking Thread '{thread_name}' Started")
            except Exception as e:
                raise e


        @classmethod
        def shutdown_network_manager(cls):
            cls.network_stop_event.set()
            with cls.network_condition:
                cls.network_condition.notify_all()

            if cls.network_thread and cls.network_thread.is_alive():
                cls.network_thread.join()
            else:
                raise Exception("Unable to close NetworkThread at Shutdown")

'''




if __name__ == "__main__":
    app = WebApp(tg_bot_webhook_method=environ.TELEGRAM_BOT_WEBHOOK_METHOD,
                 fb_bot_webhook_method=environ.FACEBOOK_BOT_WEBHOOK_METHOD,
                 wp_bot_webhook_method=environ.WHATSAPP_BOT_WEBHOOK_METHOD,
                 srv_reservation_method=environ.SERVER_RESERVATION_METHOD,
                 srv_event_info_method=environ.SERVER_EVENT_INFO_METHOD,
                 name="ChatbotApp", host="0.0.0.0", port=5000, debug=True)
    app.configure()
    app.verify()
    app.start()

    