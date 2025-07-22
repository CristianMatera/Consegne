import requests

# !! MODIFICA QUI !! Inserisci l'IP corretto della tua macchina Metasploitable.
url = "http://192.168.60.101/phpMyAdmin/"

# Lista dei metodi da provare
metodi = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']

print(f"[*] Sto testando i metodi HTTP su: {url}\n")

# [cite_start]Prova ogni metodo [cite: 44]
for metodo in metodi:
    try:
        # Invia la richiesta e ottieni la risposta
        risposta = requests.request(metodo, url, timeout=3)

        """Stampa il risultato in maniera chieda lasciando 8 spazi dal metodo specificato, gli status errori possibili sono:
            200 OK: È la risposta standard per le richieste andate a buon fine.
            204 No Content: Il server ha processato la richiesta con successo, ma non restituisce alcun contenuto. È una risposta di successo, ma la "pagina" è volutamente vuota.
            301 Moved Permanently: La risorsa che cerchi è stata spostata permanentemente a un nuovo indirizzo.
            302 Found: La risorsa è stata trovata, ma si trova temporaneamente a un altro indirizzo. Questo è il codice che ricevi da phpMyAdmin quando non sei autenticato e vieni reindirizzato alla pagina di login.
            400 Bad Request: Il server non ha capito la tua richiesta a causa di una sintassi non valida. È raro ottenerlo con la libreria requests a meno che tu non stia manipolando gli header in modo errato.
            401 Unauthorized: Non sei autorizzato ad accedere alla risorsa. Devi fornire delle credenziali di autenticazione valide. Simile al 403, ma specificamente legato all'autenticazione.
            403 Forbidden: Sei stato "capito" dal server, ma non hai i permessi per accedere a quella risorsa, anche se fossi autenticato. È una questione di autorizzazione, non di autenticazione.
            404 Not Found: La risorsa richiesta non esiste sul server. Hai semplicemente digitato un URL sbagliato.
            405 Method Not Allowed: Il metodo HTTP che hai usato (GET, POST, PUT, etc.) non è consentito per la risorsa che hai richiesto. Ad esempio, potresti ricevere questo errore tentando di usare DELETE su una pagina che accetta solo GET. Questo è un codice molto comune che vedrai durante i tuoi test.
            500 Internal Server Error: Un errore generico che indica un problema imprevisto sul server. Potrebbe essere un crash dell'applicazione web (es. un errore nel codice PHP di phpMyAdmin).
            501 Not Implemented: Il server non supporta la funzionalità richiesta. Ad esempio, il server potrebbe non aver mai implementato il metodo TRACE.
            ERRORE DI CONNESSIONE: Questo messaggio appare quando il tuo programma non riesce nemmeno a contattare il server. Le cause più comuni sono un indirizzo IP sbagliato, la macchina virtuale spenta, o problemi di configurazione della rete tra Kali e Metasploitable.        
        """
        print(f"Metodo {metodo.ljust(8)} ---> Status Code: {risposta.status_code}")
        
    except requests.exceptions.RequestException:
        print(f"Metodo {metodo.ljust(8)} ---> ERRORE DI CONNESSIONE (controlla l'IP e la rete)")