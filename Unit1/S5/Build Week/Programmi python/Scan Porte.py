# Importiamo i moduli necessari
import socket  # Per la connessione di rete
import csv  # Per salvare i risultati in un file CSV
from datetime import datetime  # Per future estensioni con data/ora
from rich.console import Console  # Per stampare tabelle colorate nel terminale
from rich.table import Table
from rich.progress import track  # Per mostrare la barra di avanzamento

# Dizionario con alcune porte comuni e i servizi associati
PORT_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC"
}

# Questa funzione restituisce il nome del servizio associato a una porta
def get_service(port):
    return PORT_SERVICES.get(port, "Sconosciuto / Non standard")

# Funzione che effettua la scansione delle porte
def scan_ports(target_ip, port_range):
    results = []  # Lista dove salviamo i risultati
    print(f"\n🔍 Scansione delle porte per {target_ip}...\n")

    # Cicliamo su tutte le porte nel range
    for port in track(port_range, description="Scansione in corso..."):
        # Creiamo un socket (connessione temporanea)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)  # Impostiamo un tempo massimo per ogni porta (0.5 secondi)
            result = sock.connect_ex((target_ip, port))  # Proviamo a connetterci alla porta

            # Se riusciamo a connetterci, la porta è aperta
            status = "APERTA" if result == 0 else "CHIUSA"
            service = get_service(port)  # Cerchiamo il nome del servizio

            # Aggiungiamo un commento di sicurezza
            if status == "APERTA":
                if service in ["SSH", "FTP", "MySQL", "SMB", "HTTP"]:
                    note = "Verificare sicurezza del servizio"
                else:
                    note = "Controllare necessità del servizio"
            else:
                note = "Nessun rischio apparente"

            # Salviamo il risultato in una lista
            results.append({
                "Porta": port,
                "Stato": status,
                "Servizio": service,
                "Note di Sicurezza": note
            })

    return results  # Ritorniamo tutti i risultati

# Funzione per salvare i risultati in un file CSV
def salva_csv(risultati, filename="risultati_scansione.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=risultati[0].keys())
        writer.writeheader()  # Scriviamo la riga con i nomi delle colonne
        for r in risultati:
            writer.writerow(r)  # Scriviamo ogni riga del risultato
    print(f"\n✅ Risultati salvati in: {filename}")

# Funzione per stampare i risultati in una bella tabella nel terminale
def generate_report(results):
    console = Console()
    table = Table(title="📋 Risultati Scansione Porte")  # Titolo della tabella

    # Aggiungiamo le colonne alla tabella
    table.add_column("Porta", justify="center")
    table.add_column("Stato", justify="center")
    table.add_column("Servizio", justify="center")
    table.add_column("Note di Sicurezza", justify="center")

    # Inseriamo una riga per ogni risultato
    for r in results:
        table.add_row(str(r["Porta"]), r["Stato"], r["Servizio"], r["Note di Sicurezza"])

    console.print(table)  # Stampiamo la tabella a schermo

# Parte principale del programma (viene eseguita solo se lanciamo questo file)
if __name__ == "__main__":
    # Chiediamo all'utente un indirizzo IP o nome di dominio
    target = input("Inserisci l'indirizzo IP o hostname da scansionare: ")

    # Proviamo a risolvere il nome (hostname) in un indirizzo IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("⚠️ Hostname non valido.")
        exit()

    # Chiediamo all'utente il range di porte da scansionare
    try:
        start = int(input("Porta iniziale: "))
        end = int(input("Porta finale: "))
    except ValueError:
        print("⚠️ Inserire numeri validi.")
        exit()

    # Controlliamo se il range è valido
    if start < 1 or end > 65535 or start > end:
        print("⚠️ Range di porte non valido.")
        exit()

    # Eseguiamo la scansione
    risultati = scan_ports(target_ip, range(start, end + 1))

    # Salviamo i risultati in un file
    salva_csv(risultati)

    # Mostriamo il report nel terminale
    generate_report(risultati)
