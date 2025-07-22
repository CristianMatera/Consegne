import socket
import csv
from datetime import datetime

# Mappa delle porte comuni con i servizi presunti
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

def get_service(port):
    return PORT_SERVICES.get(port, "Sconosciuto / Non standard")

def scan_ports(target_ip, port_range):
    results = []
    print(f"\nScansione delle porte per {target_ip}...\n")

    for port in port_range:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            status = "APERTA" if result == 0 else "CHIUSA"
            service = get_service(port)
            
            # Descrizione base della sicurezza
            if status == "APERTA":
                if service in ["SSH", "FTP", "MySQL", "SMB", "HTTP"]:
                    note = "Verificare sicurezza del servizio"
                else:
                    note = "Controllare necessità del servizio"
            else:
                note = "Nessun rischio apparente"
            
            results.append({
                "Porta": port,
                "Stato": status,
                "Servizio": service,
                "Note di Sicurezza": note
            })

            print(f"Porta {port:<5} - {status:<6} - {service:<15} - {note}")

    return results

def salva_csv(risultati, filename="risultati_scansione.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=risultati[0].keys())
        writer.writeheader()
        for r in risultati:
            writer.writerow(r)
    print(f"\n✅ Risultati salvati in: {filename}")

if __name__ == "__main__":
    target = input("Inserisci l'indirizzo IP o hostname da scansionare: ")
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("⚠️ Hostname non valido.")
        exit()

    try:
        start = int(input("Porta iniziale: "))
        end = int(input("Porta finale: "))
    except ValueError:
        print("⚠️ Inserire numeri validi.")
        exit()

    if start < 1 or end > 65535 or start > end:
        print("⚠️ Range di porte non valido.")
        exit()

    risultati = scan_ports(target_ip, range(start, end + 1))
    salva_csv(risultati)
