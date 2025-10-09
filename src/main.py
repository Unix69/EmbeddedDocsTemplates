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





# Added this comment
# Added this comment

# Added this comment
# Added this commen

# Added this comment
# Added this comment