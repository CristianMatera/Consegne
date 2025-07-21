import requests

# !! MODIFICA QUI !! Inserisci l'IP corretto della tua macchina Metasploitable.
url = "http://192.168.60.101/phpMyAdmin/index.php?token=037681c51c6a735398f7dc880b33caa3"

# Lista dei metodi da provare
metodi = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']

print(f"[*] Sto testando i metodi HTTP su: {url}\n")

# Prova ogni metodo 
for metodo in metodi:
    try:
        # Invia la richiesta e ottieni la risposta
        risposta = requests.request(metodo, url, timeout=3)
        
        # [cite_start]Stampa il risultato in modo chiaro [cite: 48]
        print(f"Metodo {metodo.ljust(8)} ---> Status Code: {risposta.status_code}")
        
    except requests.exceptions.RequestException:
        print(f"Metodo {metodo.ljust(8)} ---> ERRORE DI CONNESSIONE (controlla l'IP e la rete)")
