
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return result.scheme in ("http", "https") and result.netloc != ""
    except:
        return False

# Input utente con valore di default
default_url = "http://192.168.60.101/phpMyAdmin/"
user_url = input(f"Inserisci l'URL della pagina HTML [{default_url}]: ").strip()
html_url = user_url if user_url else default_url

# Validazione URL
if not is_valid_url(html_url):
    print(f"❌ URL non valido: '{html_url}'")
else:
    try:
        # Scarica la pagina principale
        html_response = httpx.get(html_url)
        html_response.raise_for_status()

        # Analizza con BeautifulSoup
        soup = BeautifulSoup(html_response.text, "html.parser")

        # Trova l'immagine 'logo_right.png'
        img_tag = soup.find("img", src=lambda s: s and "logo_right.png" in s)
        if img_tag:
            img_src = img_tag["src"]
            # Costruisce URL completo se è relativo
            base_url = html_url.rstrip('/')
            if img_src.startswith("/"):
                parsed = urlparse(base_url)
                img_url = f"{parsed.scheme}://{parsed.netloc}{img_src}"
            else:
                img_url = f"{base_url}/{img_src}"

            print(f"\n📷 Immagine trovata: {img_url}")

            # 2. Richiesta OPTIONS all'immagine
            response = httpx.options(img_url)
            allowed = response.headers.get("allow", "")
            allowed_methods = [m.strip().upper() for m in allowed.split(",")]

            print(f"\nMetodo OPTIONS: {response.status_code}")
            print(f"Metodi supportati dichiarati: {allowed_methods}\n")

            # 3. Testa i metodi comuni
            metodi_da_testare = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "TRACE"]

            for metodo in metodi_da_testare:
                try:
                    r = httpx.request(metodo, img_url)
                    supportato = metodo in allowed_methods
                    stato = r.status_code

                    print(f"{metodo:<7} → Status: {stato} → {'✅ Supportato' if supportato else '❌ NON dichiarato come supportato'}")
                except Exception as e:
                    print(f"{metodo:<7} → Errore durante la richiesta: {e}")
        else:
            print("⚠️ Immagine 'logo_right.png' non trovata nella pagina HTML.")

    except httpx.RequestError as err:
        print(f"❌ Errore durante il download della pagina HTML: {err}")