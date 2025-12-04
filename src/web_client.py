html_home = """
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pagina Principale - Associazione Peppino Impastato</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: url('/static/peppino_impastato.png') no-repeat center center fixed;
                background-size: cover;
                color: #fff;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }
            .content {
                 background-color: rgba(255, 0, 0, 0.6); /* rosso con trasparenza */
                padding: 40px;
                border-radius: 10px;
                width: 100%;
                max-width: 600px;
            }
            h1 {
                font-size: 36px;
                margin-bottom: 20px;
            }
            .btn {
                display: inline-block;
                background-color: #3498db;
                color: white;
                padding: 15px 25px;
                font-size: 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin: 15px 0;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }
            .btn:hover {
                background-color: #2980b9;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>Benvenuto nella pagina di gestione della Associazione Peppino Impastato</h1>
            <a href="/gestione_prenotazioni" class="btn">Gestione Prenotazioni</a>
            <a href="/gestione_eventi" class="btn">Gestione Eventi</a>
        </div>
    </body>
    </html>
    """

# Template HTML per la gestione delle prenotazioni
html_reservation = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestione Prenotazioni</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f7f9fc;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        form {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        input[type="text"], input[type="number"] {
            width: 80%;
            padding: 8px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 16px;
            font-size: 14px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
        .message, .result {
            background-color: #eafaf1;
            border: 1px solid #b2dfdb;
            padding: 10px;
            border-radius: 6px;
            margin: 10px 0;
            white-space: pre-line;
        }

        .accordion {
            background-color: #ecf0f1;
            color: #2c3e50;
            cursor: pointer;
            padding: 12px;
            width: 100%;
            text-align: left;
            border: none;
            outline: none;
            font-size: 16px;
            border-radius: 6px;
            margin-top: 10px;
        }

        .active, .accordion:hover {
            background-color: #d0d7de;
        }

        .panel {
            padding: 0 10px;
            display: none;
            overflow: hidden;
        }

        .panel table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }

        .panel th, .panel td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: center;
        }

        .panel th {
            background-color: #f4f6f8;
        }
    </style>
</head>
<body>
    <h1>Gestione Prenotazioni</h1>

    <!-- Inserimento Prenotazione Manuale -->
    <h2>Inserisci Nuova Prenotazione</h2>
    <form method="POST" action="/gestione_prenotazioni">
        <label for="nome_inserimento">Nome:</label><br>
        <input type="text" name="nome_inserimento" id="nome_inserimento" required><br>
        
        <label for="evento_inserimento">Evento:</label><br>
        <input type="text" name="evento_inserimento" id="evento_inserimento" required><br>
        
        <label for="posti_inserimento">Numero di posti:</label><br>
        <input type="number" name="posti_inserimento" id="posti_inserimento" min="1" required><br>
        
        <button type="submit" name="azione" value="inserisci">Aggiungi Prenotazione</button>
    </form>

    <!-- Verifica Prenotazione -->
    <h2>Verifica Prenotazione</h2>
    <form method="POST" action="/gestione_prenotazioni">
        <label for="nome_verifica">Inserisci il nome per la verifica:</label><br>
        <input type="text" name="nome_verifica" id="nome_verifica" required>
        <button type="submit" name="azione" value="verifica">Verifica</button>
    </form>
    
    <!-- Cancellazione Prenotazione -->
    <h2>Cancellazione Prenotazione</h2>
    <form method="POST" action="/gestione_prenotazioni">
        <label for="nome_cancellazione">Inserisci il nome per la cancellazione:</label><br>
        <input type="text" name="nome_cancellazione" id="nome_cancellazione" required>
        <button type="submit" name="azione" value="cancella">Cancella</button>
    </form>
    
    <!-- Somma dei posti prenotati per evento -->
    <h2>Somma dei Posti Prenotati per Evento</h2>
    <form method="POST" action="/gestione_prenotazioni">
        <button type="submit" name="azione" value="somma_posti">Visualizza Somma</button>
    </form>

    <!-- Messaggi di feedback -->
    {% if messaggio %}
    <div class="message">
        {{ messaggio }}
    </div>
    {% endif %}

    {% if somma_posti %}
    <div class="result">
        <h3>Somma dei Posti Prenotati per Evento</h3>
        <ul>
            {% for evento, totale in somma_posti %}
            <li><strong>{{ evento }}:</strong> {{ totale }} posti</li>
            {% endfor %}
        </ul>
    </div>
    {% endif %}
    
    <h2>Lista Completa delle Prenotazioni per Evento</h2>
    {% if prenotazioni_per_evento %}
        {% for evento, prenotazioni in prenotazioni_per_evento.items() %}
            <button class="accordion">{{ evento }}</button>
            <div class="panel">
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Posti</th>
                    </tr>
                    {% for p in prenotazioni %}
                    <tr>
                        <td>{{ p.id }}</td>
                        <td>{{ p.name }}</td>
                        <td>{{ p.number_sits }}</td>
                    </tr>
                    {% endfor %}
                </table>
            </div>
        {% endfor %}
        <script>
            const acc = document.getElementsByClassName("accordion");
            for (let i = 0; i < acc.length; i++) {
                acc[i].addEventListener("click", function () {
                    this.classList.toggle("active");
                    const panel = this.nextElementSibling;
                    panel.style.display = (panel.style.display === "block") ? "none" : "block";
                });
            }
        </script>
    {% else %}
        <p>Nessuna prenotazione trovata.</p>
    {% endif %}
</body>
</html>
"""

# Template HTML per la gestione degli eventi
html_events = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestione Eventi</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #fff5f5;
            color: #330000;
            margin: 0;
            padding: 20px;
        }
        h1, h2 {
            color: #b30000;
        }
        form, table {
            background-color: #ffe6e6;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 0 10px rgba(179, 0, 0, 0.1);
        }
        label {
            display: block;
            margin-top: 10px;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #cc0000;
            border-radius: 5px;
            box-sizing: border-box;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #cc0000;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #990000;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #cc0000;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #ffcccc;
        }
        tr:nth-child(even) {
            background-color: #fff0f0;
        }
        @media (max-width: 768px) {
            input, textarea, button {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <h1>Gestione Eventi</h1>

    <!-- Aggiungi nuovo evento -->
    <h2>Aggiungi un Nuovo Evento</h2>
    <form method="POST" action="/gestione_eventi">
        <label for="nome_evento">Nome Evento:</label>
        <input type="text" name="nome_evento" id="nome_evento" required>

        <label for="descrizione_evento">Descrizione Evento:</label>
        <textarea name="descrizione_evento" id="descrizione_evento" required></textarea>

        <label for="location_evento">Location:</label>
        <input type="text" name="location_evento" id="location_evento" required>

        <label for="data_evento">Data e Ora (formato: YYYY-MM-DD HH:MM:SS):</label>
        <input type="text" name="data_evento" id="data_evento" required>

        <label for="posti_totali">Posti Totali:</label>
        <input type="number" name="posti_totali" id="posti_totali" required>

        <label for="posti_disponibili">Posti Disponibili:</label>
        <input type="number" name="posti_disponibili" id="posti_disponibili" required>

        <button type="submit" name="azione" value="aggiungi_evento">Aggiungi Evento</button>
    </form>

    <h2>Eventi Esistenti</h2>
    <table>
        <tr>
            <th>Nome Evento</th>
            <th>Descrizione</th>
            <th>Location</th>
            <th>Data e Ora</th>
            <th>Posti Totali</th>
            <th>Posti Disponibili</th>
            <th>Can Be Sold Out</th>
        </tr>
        {% for evento in eventi %}
        <tr>
            <td>{{ evento.name }}</td>
            <td>{{ evento.description }}</td>
            <td>{{ evento.location }}</td>
            <td>{{ evento.date_time }}</td>
            <td>{{ evento.total_sits }}</td>
            <td>{{ evento.available_sits }}</td>
            <td>{{ evento.can_be_sold_out }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""



class WebClient:
    '''
    Classe per gestire le interazioni con il client web.
    '''
    def __init__(self, app):
        pass