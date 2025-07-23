import httpx                          # Libreria per effettuare richieste HTTP 
from bs4 import BeautifulSoup        # Libreria per il parsing HTML
from rich.console import Console     # Console avanzata per output colorato/testuale con Rich
from rich.table import Table         # Per creare tabelle formattate in Rich
from rich.progress import track      # Barra di avanzamento visuale da Rich
from urllib.parse import urljoin     # Per unire URL relativi con assoluti
import re                            # Libreria per espressioni regolari

# Inizializza la console Rich per stampe colorate
console = Console()

def chiedi_url():
    """Richiede un URL valido all'utente"""
    while True:
        url = input("🌐 Inserisci l'URL della pagina HTML: ").strip()
        # Verifica se l'input è un URL valido (http o https)
        if re.match(r'^https?://[^\s]+$', url):
            return url
        else:
            # Messaggio di errore in caso di URL non valido
            console.print("[red]❌ URL non valido. Assicurati che inizi con http:// o https:// e non contenga spazi.[/red]")

def generate_report(results):
    """Genera un report formattato dei risultati usando Rich"""
    
    # Crea tabella per visualizzare i risultati
    table = Table(title="🔍 Risultati Test Metodi HTTP")
    table.add_column("Metodo", style="cyan", no_wrap=True)           # Colonna per il metodo HTTP
    table.add_column("Status Code", justify="center")                # Codice di risposta
    table.add_column("Supportato", justify="center")                 # Se è stato accettato o no
    table.add_column("Dichiarato", justify="center")                 # Se è stato dichiarato nell’header “Allow”
    
    # Itera sui risultati per ogni metodo HTTP
    for metodo, data in results.items():
        if data['status'] == 'ERRORE':
            status_color = "red"                                     # Colore rosso per errori
            status_text = "ERRORE"
        elif 200 <= data['status_code'] <= 299:
            status_color = "green"                                   # Verde per risposte positive
            status_text = str(data['status_code'])
        elif 300 <= data['status_code'] <= 399:
            status_color = "yellow"                                  # Giallo per redirect
            status_text = str(data['status_code'])
        else:
            status_color = "red"                                     # Rosso per altri codici (es. errori 4xx o 5xx)
            status_text = str(data['status_code'])
        
        # Icone di supporto e dichiarazione
        supportato_icon = "✅" if data['status'] != 'ERRORE' else "❌"
        dichiarato_icon = "📋" if data['dichiarato'] else "❌"
        
        # Aggiunge una riga alla tabella per ogni metodo
        table.add_row(
            metodo,
            f"[{status_color}]{status_text}[/{status_color}]",
            supportato_icon,
            dichiarato_icon
        )
    
    # Stampa la tabella dei risultati
    console.print(table)
    
    # Calcolo statistiche finali
    totale = len(results)
    funzionanti = sum(1 for data in results.values() if data['status'] != 'ERRORE')
    dichiarati = sum(1 for data in results.values() if data['dichiarato'])
    
    # Stampa statistiche riepilogative
    console.print(f"\n📊 [bold]Statistiche:[/bold]")
    console.print(f"   • Metodi testati: {totale}")
    console.print(f"   • Metodi funzionanti: [green]{funzionanti}[/green]")
    console.print(f"   • Metodi dichiarati: [blue]{dichiarati}[/blue]")

# ⬇ Inizio esecuzione script

# 1. Chiedi l'URL da analizzare all'utente
html_url = chiedi_url()

try:
    # Effettua richiesta HTTP alla pagina HTML
    html_response = httpx.get(html_url)
    html_response.raise_for_status()  # Solleva eccezione se risposta non OK
    
    # Parsing HTML con BeautifulSoup
    soup = BeautifulSoup(html_response.text, "html.parser")
    
    # Cerca il tag <img> con 'logo_right.png' nel src
    img_tag = soup.find("img", src=lambda s: s and "logo_right.png" in s)
    
    if img_tag:
        # Estrae l’attributo src dell’immagine trovata
        img_src = img_tag["src"]
        # Costruisce URL assoluto dell'immagine
        img_url = urljoin(html_url, img_src)
        
        # Stampa URL dell'immagine trovata
        console.print(f"\n📷 [bold green]Immagine trovata:[/bold green] {img_url}")
        
        # Effettua una richiesta HTTP OPTIONS all'immagine
        response = httpx.options(img_url)
        # Ottiene metodi supportati dall’header Allow
        allowed = response.headers.get("allow", "")
        allowed_methods = [m.strip().upper() for m in allowed.split(",") if m.strip()]
        
        # Stampa il codice di stato della OPTIONS e i metodi dichiarati
        console.print(f"\n🔧 [bold]Metodo OPTIONS:[/bold] {response.status_code}")
        console.print(f"📋 [bold]Metodi dichiarati:[/bold] {allowed_methods}\n")
        
        # Elenco dei metodi HTTP da testare
        metodi_da_testare = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "TRACE"]
        risultati = {}  # Dizionario per salvare i risultati
        
        # Testa ogni metodo HTTP con barra di progresso
        for metodo in track(metodi_da_testare, description="🧪 Testando metodi HTTP..."):
            try:
                # Effettua richiesta con il metodo corrente
                r = httpx.request(metodo, img_url)
                supportato = metodo in allowed_methods   # Verifica se dichiarato
                stato = r.status_code                   # Ottiene status code della risposta
                
                # Salva risultati
                risultati[metodo] = {
                    'status_code': stato,
                    'status': stato,
                    'dichiarato': supportato
                }
            except Exception as e:
                # Gestione degli errori durante la richiesta
                risultati[metodo] = {
                    'status_code': 0,
                    'status': 'ERRORE',
                    'dichiarato': metodo in allowed_methods,
                    'errore': str(e)                   # Salva il messaggio di errore
                }
        
        # Stampa il report finale
        console.print(f"\n🎯 [bold]Report finale per:[/bold] {img_url}")
        generate_report(risultati)
        
    else:
        # Se l’immagine specificata non è trovata nel documento HTML
        console.print("[red]⚠ Immagine 'logo_right.png' non trovata nella pagina HTML.[/red]")

# Gestione degli errori di connessione o richieste fallite
except httpx.RequestError as err:
    console.print(f"[red]❌ Errore durante il download della pagina HTML: {err}[/red]")

