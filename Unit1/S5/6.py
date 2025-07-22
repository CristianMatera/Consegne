# Programma semplice per testare i verbi HTTP
# Importiamo la libreria per fare richieste web
import requests

# L'indirizzo del server da testare - CAMBIA QUESTO!
url = "http://192.168.60.101/phpMyAdmin/"  # Sito di test che funziona sempre

print("=== TEST DEI VERBI HTTP ===")
print(f"Server da testare: {url}")
print()

# TEST 1: GET (leggere dati)
print("1. Test GET (leggere dati):")
try:
    # Facciamo una richiesta GET
    risposta = requests.get(url + "/get")
    # Stampiamo il risultato
    print(f"   Codice: {risposta.status_code}")
    if risposta.status_code == 200:
        print("   ✓ GET funziona!")
    else:
        print("   ✗ GET ha problemi")
except:
    print("   ✗ Errore nella richiesta GET")

print()

# TEST 2: POST (inviare dati)
print("2. Test POST (inviare dati):")
try:
    # Dati da inviare
    dati = {"nome": "test", "messaggio": "ciao"}
    # Facciamo una richiesta POST
    risposta = requests.post(url + "/post", data=dati)
    print(f"   Codice: {risposta.status_code}")
    if risposta.status_code == 200:
        print("   ✓ POST funziona!")
    else:
        print("   ✗ POST ha problemi")
except:
    print("   ✗ Errore nella richiesta POST")

print()

# TEST 3: PUT (aggiornare dati)
print("3. Test PUT (aggiornare dati):")
try:
    # Dati da aggiornare
    dati = {"id": 1, "nome": "test_nuovo"}
    risposta = requests.put(url + "/put", data=dati)
    print(f"   Codice: {risposta.status_code}")
    if risposta.status_code == 200:
        print("   ✓ PUT funziona!")
    else:
        print("   ✗ PUT ha problemi")
except:
    print("   ✗ Errore nella richiesta PUT")

print()

# TEST 4: DELETE (cancellare dati)
print("4. Test DELETE (cancellare dati):")
try:
    risposta = requests.delete(url + "/delete")
    print(f"   Codice: {risposta.status_code}")
    if risposta.status_code == 200:
        print("   ✓ DELETE funziona!")
    else:
        print("   ✗ DELETE ha problemi")
except:
    print("   ✗ Errore nella richiesta DELETE")

print()
print("=== TEST COMPLETATI ===")
print("Nota: Usa httpbin.org per i test, oppure cambia 'url' con il tuo server")