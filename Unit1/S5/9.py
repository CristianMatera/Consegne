import httpx

url = "http://192.168.60.101/phpMyAdmin/themes/original/img/logo_right.png"

try:
    # Fai la richiesta OPTIONS
    response = httpx.options(url)
    allowed = response.headers.get("allow", "")
    allowed_methods = [m.strip().upper() for m in allowed.split(",")]

    print(f"Metodo OPTIONS: {response.status_code}")
    print(f"Metodi supportati dichiarati: {allowed_methods}\n")

    # Lista dei metodi HTTP comuni
    metodi_da_testare = ["GET", "POST", "PUT", "DELETE",  "HEAD",  "OPTIONS"]

    # Testa ogni metodo
    for metodo in metodi_da_testare:
        try:
            r = httpx.request(metodo, url)
            supportato = metodo in allowed_methods
            stato = r.status_code

            print(f"{metodo:<7} → Status: {stato} → {'✅ Supportato' if supportato else '❌ NON dichiarato come supportato'}")

        except Exception as e:
            print(f"{metodo:<7} → Errore durante la richiesta: {e}")

except httpx.RequestError as err:
    print(f"Errore nella richiesta OPTIONS: {err}")

