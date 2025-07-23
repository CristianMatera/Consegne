import socket                          # Libreria per la comunicazione di rete
import struct                          # Per convertire i dati binari in valori leggibili
from rich.console import Console       # Per stampare output formattato e colorato
from rich.table import Table           # Per creare tabelle esteticamente gradevoli

console = Console()                    # Istanza della console Rich per output

# Chiede all'utente l'IP da filtrare
target_ip = input("Inserisci l'IP da monitorare: ").strip()
# Chiede all'utente la porta da filtrare (opzionale)
target_port = input("Inserisci la porta da monitorare (es. 80 o lascia vuoto per tutte): ").strip()

# Se l'utente ha inserito una porta, la converte in intero, altrimenti None (tutte le porte)
target_port = int(target_port) if target_port.isdigit() else None

# Funzione che trasforma un indirizzo IP da bytes a stringa leggibile (es. b'\xc0\xa8\x01d' -> '192.168.1.100')
def ip_format(addr):
    return '.'.join(map(str, addr))    # Converte ogni byte in stringa e unisce con punti

# Creazione del socket RAW per leggere tutti i pacchetti Ethernet (richiede privilegi elevati)
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
# AF_PACKET = livello Ethernet, SOCK_RAW = pacchetti grezzi, 0x0003 = tutti i protocolli

# Stampa di conferma con i filtri scelti dall'utente
console.print(f"[bold green]In ascolto su IP: {target_ip}, Porta: {target_port if target_port else 'Tutte'}[/bold green]")

try:
    while True:
        # Riceve dati raw dal socket (massimo 65535 byte)
        raw_data, addr = s.recvfrom(65535)

        eth_length = 14  # Lunghezza standard header Ethernet in byte
        eth_header = raw_data[:eth_length]  # Estrae l'header Ethernet dal pacchetto
        eth = struct.unpack('!6s6sH', eth_header)  # Disimpacchetta MAC dest, MAC sorg, protocollo
        proto = socket.ntohs(eth[2])  # Converte il campo protocollo in host byte order

        # Controlla che il protocollo sia IPv4 (0x0800 == 8 in decimale)
        if proto == 8:
            # Estrae l'header IP dal pacchetto (subito dopo l'header Ethernet)
            ip_header = raw_data[eth_length:20 + eth_length]
            # Disimpacchetta l'header IP in vari campi (versione, lunghezza, protocollo, IP sorg, IP dest...)
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

            src_ip = ip_format(iph[8])  # IP sorgente (ultimo campo)
            dst_ip = ip_format(iph[9])  # IP destinazione (ultimo campo)
            protocol = iph[6]            # Protocollo (TCP=6, UDP=17...)

            iph_length = (iph[0] & 0xF) * 4  # Calcola la lunghezza header IP (in byte)
            offset = eth_length + iph_length  # Calcola l'offset per l'header TCP/UDP

            # Controlla se il protocollo è TCP
            if protocol == 6:
                tcp_header = raw_data[offset:offset + 20]  # Estrae header TCP
                tcph = struct.unpack('!HHLLBBHHH', tcp_header)  # Disimpacchetta campi TCP
                src_port = tcph[0]  # Porta sorgente TCP
                dst_port = tcph[1]  # Porta destinazione TCP
                proto_name = 'TCP'
            # Controlla se il protocollo è UDP
            elif protocol == 17:
                udp_header = raw_data[offset:offset + 8]  # Estrae header UDP
                udph = struct.unpack('!HHHH', udp_header)  # Disimpacchetta campi UDP
                src_port = udph[0]  # Porta sorgente UDP
                dst_port = udph[1]  # Porta destinazione UDP
                proto_name = 'UDP'
            else:
                continue  # Se protocollo non è TCP o UDP, salta al prossimo pacchetto

            # Verifica se il pacchetto coinvolge l'IP target (sorgente o destinazione)
            ip_match = (src_ip == target_ip or dst_ip == target_ip)
            # Verifica se la porta target è coinvolta (sorgente o destinazione), o tutte se None
            port_match = (target_port is None or src_port == target_port or dst_port == target_port)

            # Se entrambi i filtri corrispondono, stampa la tabella
            if ip_match and port_match:
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("Protocollo", style="cyan")
                table.add_column("IP Sorgente", style="green")
                table.add_column("Porta Sorgente", justify="right")
                table.add_column("IP Destinazione", style="green")
                table.add_column("Porta Destinazione", justify="right")

                table.add_row(proto_name, src_ip, str(src_port), dst_ip, str(dst_port))
                console.print(table)

# Gestione dell'interruzione da tastiera (CTRL+C)
except KeyboardInterrupt:
    console.print("\n[bold red]Sniffer terminato dall'utente.[/bold red]")

