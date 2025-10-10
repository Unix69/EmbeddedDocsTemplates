# @feature login
# name: Login
# description: Permette agli utenti di autenticarsi tramite username/password o OAuth
# versions: v1.0.0, v1.1.0, v1.2.0  
# api: auth.login, auth.oauth
# namespace: auth
# status: released




# @api auth.login
# name: Login
# method: POST
# path: /login
# description: Autentica l'utente e restituisce token JWT
# params:
#   - username: string, required
#   - password: string, required
# return: token: string
# permissions: public
# namespace: auth
# versions: v1.0.0, v1.1.0, v1.2.0  


# @namespace auth
# name: Auth 
# description: Contiene tutte le API relative all'autenticazione
# versions: v1.0.0, v1.1.0, v1.2.0  
# apis: auth.login, auth.oauth
# status: released



# @bug #1
# description: Token JWT scade troppo presto
# feature: #101
# api: auth.login
# namespace: auth
# version: v1.0.0


# @fix #1
# description: Aggiunta gestione refresh token
# related bug #1
# features: #101
# api: auth.login
# version: v1.0.1


# @version v1.0.0
# features: login
# api: auth.login, auth.logout
# namespace: auth



"""
@file main.py
@brief Modulo principale del sistema

Contiene la logica di avvio e il ciclo principale dell'applicazione.

@author
Giuseppe
@version 1.2
@date 2025-10-10
"""

import math

class Engine:
    """
    @class Engine
    @brief Rappresenta il motore del sistema.
    @details
    La classe Engine gestisce la potenza, l’avvio e l’arresto
    di un motore simulato.
    """

    def __init__(self, power: float):
        """
        @brief Costruttore del motore.
        @param power Potenza nominale del motore in Watt.
        """
        self.power = power
        self.running = False

    def start(self):
        """@brief Avvia il motore."""
        self.running = True
        print("Motore avviato.")

    def stop(self):
        """@brief Arresta il motore."""
        self.running = False
        print("Motore fermato.")

    def torque(self, rpm: float) -> float:
        """
        @brief Calcola la coppia in funzione degli RPM.
        @param rpm Giri al minuto.
        @return Valore della coppia (Nm).
        """
        if rpm <= 0:
            return 0.0
        return (self.power * 60) / (2 * math.pi * rpm)


def main():
    """
    @brief Punto di ingresso principale.
    Crea un oggetto Engine e ne testa le funzioni principali.
    """
    e = Engine(2500)
    e.start()
    print(f"Coppia a 3000 rpm: {e.torque(3000):.2f} Nm")
    e.stop()


if __name__ == "__main__":
    main()

# Added this comment
# Added this comment

# Added this comment
# Added this commen

# Added this comment
# Added this comment