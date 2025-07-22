#Programma semplice per testare i verbi HTTP su un'applicazione web
# Importiamo la libreria per fare richieste web
import requests

# L'indirizzo del server da testare - CAMBIA QUESTO!
# Ho cambiato l'URL per puntare alla pagina principale di phpMyAdmin, che risponderà a GET/POST.
# Gli endpoint come /get, /post, ecc., non esistono su phpMyAdmin.
url = "http://192.168.60.101/phpMyAdmin/index.php"  # URL specifico per la pagina di phpMyAdmin

print("=== TEST DEI VERBI HTTP ===")
print("Server da testare:", url)
print()

# TEST 1: GET (leggere dati)
# Per phpMyAdmin, un GET a index.php dovrebbe mostrare la pagina di login o l'interfaccia.
print("1. Test GET (leggere dati):")
try:
    # Facciamo una richiesta GET alla pagina principale di phpMyAdmin
    risposta = requests.get(url, timeout=10) # Cambiato: non aggiungiamo /get, ma richiediamo la pagina base
    # Stampiamo il risultato
    print("   Codice:", risposta.status_code)
    # Un codice 200 significa che la pagina è stata caricata correttamente.
    if risposta.status_code == 200:
        print("   ✓ GET funziona! La pagina di phpMyAdmin è stata caricata.")
    else:
        print(f"   ✗ GET ha problemi. Codice: {risposta.status_code}")
except Exception as e:
    print("   ✗ Errore nella richiesta GET:", str(e))

print()

# TEST 2: POST (inviare dati)
# Per phpMyAdmin, il POST è tipicamente usato per l'autenticazione o l'esecuzione di query.
# Qui simuleremo un tentativo di login (senza credenziali valide, quindi ci aspettiamo un reindirizzamento o errore di login).
print("2. Test POST (inviare dati):")
try:
    # Dati da inviare per un tentativo di login (es. username e password vuoti)
    # I nomi dei campi di input possono variare, 'pma_username' e 'pma_password' sono comuni.
    dati_login = {
        "pma_username": "root",  # Esempio di username
        "pma_password": "password",      # Esempio di password vuota
        "input_remember_me": "on", # Campo per "ricordami"
        "set_session": "Cerca"     # Il nome del pulsante di submit
    }
    # Facciamo una richiesta POST alla pagina di phpMyAdmin
    risposta = requests.post(url, data=dati_login, timeout=10) # Non aggiungiamo /post, ma inviamo dati alla pagina base
    print("   Codice:", risposta.status_code)
    # Un codice 200 potrebbe indicare che la pagina di login è stata ricaricata con un errore,
    # un 302/303 un reindirizzamento dopo un login riuscito (o fallito verso la stessa pagina).
    if risposta.status_code == 200 or risposta.status_code == 302:
        print("   ✓ POST funziona! (Potrebbe essere un reindirizzamento o un errore di login sulla stessa pagina)")
        # Puoi ispezionare risposta.url e risposta.text per capire cosa è successo
    else:
        print(f"   ✗ POST ha problemi. Codice: {risposta.status_code}")
except Exception as e:
    print("   ✗ Errore nella richiesta POST:", str(e))

print()

# TEST 3: PUT (aggiornare dati)
# phpMyAdmin non supporta PUT direttamente sull'interfaccia principale per aggiornare risorse.
# Un 405 è il comportamento atteso.
print("3. Test PUT (aggiornare dati):")
try:
    dati = {"id": 1, "nome": "test_nuovo"}
    risposta = requests.put(url, data=dati, timeout=10) # Non aggiungiamo /put, tentiamo sulla pagina base
    print("   Codice:", risposta.status_code)
    if risposta.status_code == 405: # Ci aspettiamo 405 Method Not Allowed
        print("   ✓ PUT funziona come previsto (Codice 405: Metodo non consentito).")
        print("     phpMyAdmin non supporta il metodo PUT direttamente per questa risorsa.")
    else:
        print(f"   ✗ PUT ha problemi. Codice: {risposta.status_code}")
except Exception as e:
    print("   ✗ Errore nella richiesta PUT:", str(e))

print()

# TEST 4: DELETE (cancellare dati)
# phpMyAdmin non supporta DELETE direttamente sull'interfaccia principale per cancellare risorse.
# Un 405 è il comportamento atteso.
print("4. Test DELETE (cancellare dati):")
try:
    risposta = requests.delete(url, timeout=10) # Non aggiungiamo /delete, tentiamo sulla pagina base
    print("   Codice:", risposta.status_code)
    if risposta.status_code == 405: # Ci aspettiamo 405 Method Not Allowed
        print("   ✓ DELETE funziona come previsto (Codice 405: Metodo non consentito).")
        print("     phpMyAdmin non supporta il metodo DELETE direttamente per questa risorsa.")
    else:
        print(f"   ✗ DELETE ha problemi. Codice: {risposta.status_code}")
except Exception as e:
    print("   ✗ Errore nella richiesta DELETE:", str(e))

print()

# TEST 5: HEAD (solo header, senza contenuto)
# HEAD dovrebbe funzionare su una risorsa esistente come index.php.
print("5. Test HEAD (solo informazioni, senza contenuto):")
try:
    risposta = requests.head(url, timeout=10) # Non aggiungiamo /get, ma richiediamo gli header di index.php
    print("   Codice:", risposta.status_code)
    if risposta.status_code == 200:
        print("   ✓ HEAD funziona! Ha recuperato gli header della pagina.")
        print("   Dimensione contenuto (dall'header):", risposta.headers.get('content-length', 'non specificata'))
    else:
        print(f"   ✗ HEAD ha problemi. Codice: {risposta.status_code}")
except Exception as e:
    print("   ✗ Errore nella richiesta HEAD:", str(e))

print()

# TEST 6: OPTIONS (vedere che metodi sono supportati)
# Questo test dovrebbe continuare a funzionare come prima sull'URL base.
print("6. Test OPTIONS (vedere metodi supportati):")
try:
    risposta = requests.options(url, timeout=10)
    print("   Codice:", risposta.status_code)
    if risposta.status_code == 200:
        print("   ✓ OPTIONS funziona!")
        # Controlliamo se ci sono i metodi supportati negli header
        metodi_supportati = risposta.headers.get('allow', 'non specificati')
        print("   Metodi supportati:", metodi_supportati)
    else:
        print(f"   ✗ OPTIONS ha problemi. Codice: {risposta.status_code}")
except Exception as e:
    print("   ✗ Errore nella richiesta OPTIONS:", str(e))

def stampa_metodi_supportati(headers):
    metodi_supportati = headers.get('Allow') or headers.get('allow')
    if metodi_supportati:
        print("   Metodi supportati dal server:", metodi_supportati)
    else:
        print("   ⚠ Nessuna informazione sui metodi supportati trovata nell'header 'Allow'.")



print()
print("=== TEST COMPLETATI ===")
print("Questi test riflettono il comportamento di una vera applicazione web come phpMyAdmin.")
