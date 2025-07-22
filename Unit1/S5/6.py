# Programma semplice per testare i verbi HTTP
# Importiamo la libreria per fare richieste web
import requests

# L'indirizzo del server da testare - CAMBIA QUESTO!
url = "http://192.168.60.101/phpMyAdmin/"  # Sito di test che funziona sempre (HTTPS per sicurezza)

print("=== TEST DEI VERBI HTTP ===")
print("Server da testare:", url)
print()

# TEST 1: GET (leggere dati)
print("1. Test GET (leggere dati):")
try:
    # Facciamo una richiesta GET
    risposta = requests.get(url + "/get", timeout=10)
    # Stampiamo il risultato
    print("   Codice:", risposta.status_code)
    if risposta.status_code == 200:
        print("   ✓ GET funziona!")
    else:
        print("   ✗ GET ha problemi")
except Exception as e:
    print("   ✗ Errore nella richiesta GET:", str(e))

print()

# TEST 2: POST (inviare dati)
print("2. Test POST (inviare dati):")
try:
    # Dati da inviare
    dati = {"nome": "test", "messaggio": "ciao"}
    # Facciamo una richiesta POST
    risposta = requests.post(url + "/post", data=dati, timeout=10)
    print("   Codice:", risposta.status_code)
    if risposta.status_code == 200:
        print("   ✓ POST funziona!")
    else:
        print("   ✗ POST ha problemi")
except Exception as e:
    print("   ✗ Errore nella richiesta POST:", str(e))

print()

# TEST 3: PUT (aggiornare dati)
print("3. Test PUT (aggiornare dati):")
try:
    # Dati da aggiornare
    dati = {"id": 1, "nome": "test_nuovo"}
    risposta = requests.put(url + "/put", data=dati, timeout=10)
    print("   Codice:", risposta.status_code)
    if risposta.status_code == 200:
        print("   ✓ PUT funziona!")
    else:
        print("   ✗ PUT ha problemi")
except Exception as e:
    print("   ✗ Errore nella richiesta PUT:", str(e))

print()

# TEST 4: DELETE (cancellare dati)
print("4. Test DELETE (cancellare dati):")
try:
    risposta = requests.delete(url + "/delete", timeout=10)
    print("   Codice:", risposta.status_code)
    if risposta.status_code == 200:
        print("   ✓ DELETE funziona!")
    else:
        print("   ✗ DELETE ha problemi")
except Exception as e:
    print("   ✗ Errore nella richiesta DELETE:", str(e))

print()

# TEST 5: HEAD (solo header, senza contenuto)
print("5. Test HEAD (solo informazioni, senza contenuto):")
try:
    risposta = requests.head(url + "/get", timeout=10)
    print("   Codice:", risposta.status_code)
    if risposta.status_code == 200:
        print("   ✓ HEAD funziona!")
        print("   Dimensione contenuto:", risposta.headers.get('content-length', 'non specificata'))
    else:
        print("   ✗ HEAD ha problemi")
except Exception as e:
    print("   ✗ Errore nella richiesta HEAD:", str(e))

print()

# TEST 6: OPTIONS (vedere che metodi sono supportati)
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
        print("   ✗ OPTIONS ha problemi")
except Exception as e:
    print("   ✗ Errore nella richiesta OPTIONS:", str(e))

print()
print("=== TEST COMPLETATI ===")
print("Tutti i 6 verbi HTTP sono stati testati!")
