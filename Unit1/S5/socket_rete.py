import socket
import struct
from rich.console import Console
from rich.table import Table

console = Console()

def ethernet_frame(data):
    # Disimpacchetta frame Ethernet (solo per Linux, opzionale)
    dest_mac, src_mac, proto = struct.unpack('!6s6sH', data[:14])
    return data[14:]

def ipv4_packet(data):
    version_header_length = data[0]
    header_length = (version_header_length & 15) * 4
    src, target = struct.unpack('!4s4s', data[12:20])
    return src, target, data[header_length:]

def tcp_segment(data):
    (src_port, dest_port) = struct.unpack('!HH', data[:4])
    return src_port, dest_port

# 🌐 Crea un socket RAW (solo IPv4, TCP)
try:
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except PermissionError:
    console.print("[bold red]❌ Devi eseguire questo script come root/amministratore![/bold red]")
    exit()

console.print("[bold cyan]📡 Sniffer RAW TCP avviato... (premi Ctrl+C per fermare)[/bold cyan]")

try:
    while True:
        raw_data, addr = sniffer.recvfrom(65535)

        # Disimpacchettiamo pacchetto IP
        src_ip, dest_ip, tcp_data = ipv4_packet(raw_data)
        src_ip_str = '.'.join(map(str, src_ip))
        dest_ip_str = '.'.join(map(str, dest_ip))

        # Otteniamo porte TCP
        src_port, dest_port = tcp_segment(tcp_data)

        table = Table(title="📦 Pacchetto TCP ricevuto", show_lines=True)
        table.add_column("Campo", style="bold green")
        table.add_column("Valore", style="bold yellow")
        table.add_row("IP Sorgente", src_ip_str)
        table.add_row("Porta Sorgente", str(src_port))
        table.add_row("IP Destinazione", dest_ip_str)
        table.add_row("Porta Destinazione", str(dest_port))

        console.print(table)

except KeyboardInterrupt:
    console.print("\n[bold green]✔️ Sniffer interrotto dall'utente.[/bold green]")
