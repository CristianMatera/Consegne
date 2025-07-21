import socket

def scan_ports(target_ip, port_range):
    print(f"Scansione delle porte per {target_ip}...")
    
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Timeout per la connessione
        
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Porta {port} è APERTA")
        sock.close()

# Esempio di utilizzo
if __name__ == "__main__":
    target = input("Inserisci l'indirizzo IP o hostname da scansionare: ")
    # Esempio: range delle prime 1024 porte comuni
    scan_ports(target, range(1, 1025))
