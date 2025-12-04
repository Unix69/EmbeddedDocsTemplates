import os
import re
import time
from datetime import datetime
import requests

from env import environ

from database import db


MAX_MESSAGES = 10  # Limite massimo di messaggi nella conversazione
# Imposta la durata massima per la cronologia (1 giorno in secondi)
ONE_DAY_IN_SECONDS = 86400


conversation_history = {}  # user_id -> lista di messaggi
info_history = {}
# Dizionario per memorizzare lo stato delle prenotazioni per ogni utente
user_data = {}
user_data.clear()
conversation_history.clear()
info_history.clear()


def ask_llm(user_id, prompt):

    try:

        # Inizializza la cronologia se è la prima volta
        if user_id not in conversation_history:
            conversation_history[user_id] = {"messages": [], "timestamp": time.time()}  # Aggiungi timestamp
        
        # Controlla se è trascorso un giorno e resetta la cronologia se necessario
        if time.time() - conversation_history[user_id]["timestamp"] > ONE_DAY_IN_SECONDS:
            conversation_history[user_id] = {"messages": [], "timestamp": time.time()}  # Reset della cronologia
    
        # Aggiungi il nuovo messaggio dell'utente
        conversation_history[user_id]["messages"].append({"role": "user", "content": prompt})
        
        # Se la lista supera il limite di 10 messaggi, rimuovi il più vecchio
        if len(conversation_history[user_id]["messages"]) > MAX_MESSAGES:
            conversation_history[user_id]["messages"].pop(0)
        
        # Prepara i dati per la richiesta
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {environ.GPT_API_KEY}'
        }
        data = {
            "model": "gpt-4-turbo",  # Modello specifico, usa "gpt-4" se necessario
            "messages": conversation_history[user_id]["messages"],  # Invia tutta la conversazione
            "max_tokens": 200  # Numero massimo di token nella risposta
        }
        
        # Effettua la richiesta API
        response = requests.post(environ.OPEN_AI_URL, headers=headers, json=data)

        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]["content"]
            # Aggiungi la risposta del modello alla conversazione
            conversation_history[user_id]["messages"].append({"role": "assistant", "content": answer})
            return answer
        else:
            return f"Errore: {response.status_code} - {response.text}"

    except Exception as e:
        print("Errore:", e)
        return "Si è verificato un errore con il servizio. Per favore riprova più tardi."


# LLM che accetta stringhe
def ask_llm2(user_id, prompt):

    try:

        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {environ.GPT_API_KEY}'
    }
        data = {
        "model": "gpt-3.5-turbo-instruct",  # Modello specifico, usa "gpt-4" se necessario
        "prompt": prompt,  # Invia tutta la conversazione
        "max_tokens": 200  # Numero massimo di token nella risposta
    }

        response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)

        if response.status_code == 200:
            answer = response.json()["choices"][0]["text"]
            return answer
        else:
            return f"Errore: {response.status_code} - {response.text}"

    except Exception as e:
        print("Errore Cohere:", e)
        return "Si è verificato un errore con il servizio. Per favore riprova più tardi."
    

def ask_llm3(user_id, prompt):

    try:

        # Inizializza la cronologia se è la prima volta
        if user_id not in info_history:
            info_history[user_id] = {"messages": [], "timestamp": time.time()}  # Aggiungi il timestamp
        
        # Controlla se è trascorso un giorno e resetta la cronologia se necessario
        if time.time() - info_history[user_id]["timestamp"] > ONE_DAY_IN_SECONDS:
            info_history[user_id] = {"messages": [], "timestamp": time.time()}  # Reset della cronologia
    
        # Aggiungi il nuovo messaggio dell'utente
        info_history[user_id]["messages"].append({"role": "user", "content": prompt})
        
        # Se la lista supera il limite di 10 messaggi, rimuovi il più vecchio
        if len(info_history[user_id]["messages"]) > MAX_MESSAGES:
            info_history[user_id]["messages"].pop(0)
        
        # Prepara i dati per la richiesta
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {environ.GPT_API_KEY}'
        }
        data = {
            "model": "gpt-4-turbo",  # Modello specifico, usa "gpt-4" se necessario
            "messages": info_history[user_id]["messages"],  # Invia tutta la conversazione
            "max_tokens": 200  # Numero massimo di token nella risposta
        }
        
        # Effettua la richiesta API
        response = requests.post(environ.OPEN_AI_URL, headers=headers, json=data)

        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]["content"]
            # Aggiungi la risposta del modello alla conversazione
            info_history[user_id]["messages"].append({"role": "assistant", "content": answer})
            return answer
        else:
            return f"Errore: {response.status_code} - {response.text}"

    except Exception as e:
        print("Errore Cohere:", e)
        return "Si è verificato un errore con il servizio. Per favore riprova più tardi."    
    


def info_extraction(user_id, message):
    # Ottieni lo stato attuale dell'utente, se esiste
    if user_id not in user_data:
        user_data[user_id] = {'name': None, 'event': None, 'number_sits': None}

    # Estrai le informazioni dal messaggio e aggiorna lo stato dell'utente
    if not user_data[user_id]['name']:
        name_match = re.search(r'nome\s*[:\-]?\s*(\w+(\s\w+)*)', message, re.IGNORECASE)
        if name_match:
            user_data[user_id]['name'] = name_match.group(1).strip()

    if not user_data[user_id]['event']:
        event_match = re.search(r'evento\s*[:\-]?\s*(\w+(\s\w+)*)', message, re.IGNORECASE)
        if event_match:
            user_data[user_id]['event'] = event_match.group(1).strip()

    if user_data[user_id]['number_sits'] is None:
        number_sits_match = re.search(r'numero\s*posti\s*[:\-]?\s*(\d+)', message, re.IGNORECASE)
        if number_sits_match:
            user_data[user_id]['number_sits'] = int(number_sits_match.group(1).strip())

    return user_data[user_id]  # Restituisce lo stato attuale dell'utente    


class AI:
    """
    Classe per gestire le interazioni con i modelli LLM.
    """
    def __init__(self):
        pass