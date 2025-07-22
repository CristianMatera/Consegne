import httpx

url = "http://192.168.60.101/phpMyAdmin/"

try:
    # Fai la richiesta OPTIONS
    response = httpx.options(f"{url}/get")
    allowed = response.headers.get("Allow" )
    allowed_methods = [m.strip().upper() for m in allowed.split(",")]

    print(f"Metodo OPTIONS: {response.status_code}")
    print(f"Metodi supportati dichiarati: {allowed}\n")

    # Lista dei metodi HTTP comuni
    #metodi_da_testare = ["GET", "POST", "PUT", "DELETE",  "HEAD",  "OPTIONS"]

    # Testa ogni metodo
    for metodo in allowed_methods:
        try:
            r = httpx.request(metodo, url)
            supportato = metodo in allowed
            stato = r.status_code

            print(f"{metodo:<7} → Status: {stato} → {'✅ Supportato' if supportato else '❌ NON dichiarato come supportato'}")

        except Exception as e:
            print(f"{metodo:<7} → Errore durante la richiesta: {e}")

except httpx.RequestError as err:
    print(f"Errore nella richiesta OPTIONS: {err}")

