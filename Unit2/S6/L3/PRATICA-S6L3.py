import socket          # Importa il modulo socket, usato per creare connessioni e inviare dati in rete
import random          # Importa il modulo random, usato per generare byte casuali
import ipaddress       # Importa il modulo ipaddress, usato per validare indirizzi IP

# Definizione di una funzione per ottenere un indirizzo IP valido dall'utente
def get_valid_ip():
    while True:  # Ciclo infinito finché non viene inserito un IP corretto
        ip_input = input("Inserisci l'indirizzo IP della macchina target: ")  # Chiede l’IP all’utente
        try:
            ip = ipaddress.ip_address(ip_input)  # Tenta di creare un oggetto IP. Se fallisce, genera un errore
            return str(ip)  # Se valido, restituisce l'indirizzo IP come stringa
        except ValueError:  # Se l'indirizzo non è valido
            print("❌ Indirizzo IP non valido. Riprova.")  # Messaggio di errore

# Definizione di una funzione per ottenere una porta UDP valida
def get_valid_port():
    while True:  # Ciclo finché l’utente non inserisce una porta valida
        try:
            port = int(input("Inserisci la porta UDP della macchina target: "))  # Chiede la porta all’utente
            if 0 <= port <= 65535:  # Controlla che sia nel range valido delle porte (0-65535)
                return port  # Se valida, la restituisce
            else:
                print("❌ La porta deve essere compresa tra 0 e 65535.")  # Messaggio d’errore
        except ValueError:  # Se l’utente inserisce un valore non numerico
            print("❌ Inserisci un numero valido.")  # Messaggio di errore

# Definizione di una funzione per ottenere il numero di pacchetti da inviare
def get_packet_count():
    while True:  # Continua finché non viene inserito un numero valido
        try:
            count = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))  # Chiede il numero di pacchetti
            if count > 0:  # Deve essere maggiore di zero
                return count  # Restituisce il numero inserito
            else:
                print("❌ Il numero deve essere maggiore di 0.")  # Messaggio d’errore
        except ValueError:  # Se l’utente inserisce qualcosa di non numerico
            print("❌ Inserisci un numero valido.")  # Messaggio di errore

# Funzione principale che esegue il programma
def main():
    # Richiama le funzioni precedenti per ottenere gli input validati
    target_ip = get_valid_ip()         # Ottiene e valida l’indirizzo IP
    target_port = get_valid_port()     # Ottiene e valida la porta
    packet_count = get_packet_count()  # Ottiene il numero di pacchetti da inviare

    # Stampa le informazioni riepilogative prima dell'invio
    print(f"\n📤 Invio di {packet_count} pacchetti da 1 KB a {target_ip}:{target_port}...\n")

    # Crea un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Crea un socket IPv4 con protocollo UDP

    # Ciclo per inviare tutti i pacchetti richiesti
    for i in range(packet_count):  # Ripete per il numero di pacchetti da inviare
        # Genera un pacchetto da 1024 byte con dati casuali
        data = bytes(random.getrandbits(8) for _ in range(1024))  # Crea 1024 byte casuali
        # Invia il pacchetto all’indirizzo e porta specificati
        sock.sendto(data, (target_ip, target_port))  # Invia il pacchetto via UDP
        # Conferma che il pacchetto è stato inviato
        print(f"✅ Pacchetto {i + 1} inviato.")  # Stampa il numero del pacchetto inviato

    # Messaggio finale al termine dell’invio di tutti i pacchetti
    print("\n✅ Tutti i pacchetti sono stati inviati.")  # Conferma finale

# Esecuzione diretta del programma
main()
