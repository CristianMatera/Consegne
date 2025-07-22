 #Programma per estrarre i nomi dei campi dal form di login di phpMyAdmin
# usando requests e Beautiful Soup, ignorando esplicitamente il token CSRF.

import requests
from bs4 import BeautifulSoup

# L'URL della pagina di login di phpMyAdmin.
# Assicurati che sia quello corretto per la tua installazione.
phpmyadmin_url = "http://192.168.60.101/phpMyAdmin/index.php"

print("=== ESTRAZIONE DETTAGLI FORM DI LOGIN DA PHPMYADMIN (SENZA TOKEN CSRF) ===")
print("URL di phpMyAdmin:", phpmyadmin_url)
print()

# Fase 1: Ottenere la pagina di login (GET request)
print("1. Ottenimento della pagina di login...")
try:
    # Esegui una richiesta GET per ottenere il contenuto HTML della pagina di login.
    response = requests.get(phpmyadmin_url, timeout=10)
    response.raise_for_status()  # Solleva un'eccezione per errori HTTP (4xx o 5xx)

    # Inizializza Beautiful Soup con il contenuto HTML della risposta.
    # Questo ci permette di navigare e cercare gli elementi del form.
    soup = BeautifulSoup(response.text, 'html.parser')

    print("   ✓ Pagina di login ottenuta con successo (Codice:", response.status_code, ")")
    print()

    # Fase 2: Trovare il form di login
    # Cerchiamo il tag <form>. phpMyAdmin ha solitamente un solo form principale per il login.
    # Potresti voler essere più specifico se ci sono più form nella pagina,
    # ad esempio cercando un form con un certo 'id' o 'class'.
    login_form = soup.find('form')

    if login_form:
        print("2. Form di login trovato. Analisi dei campi...")
        # Estrai l'URL a cui il form invierebbe i dati (l'attributo 'action').
        form_action_url = login_form.get('action')
        if form_action_url:
            # Combina l'action con l'URL base se è un percorso relativo.
            full_form_action_url = requests.compat.urljoin(phpmyadmin_url, form_action_url)
            print(f"   URL di invio del form (action): {full_form_action_url}")
        else:
            print("   ✗ Attenzione: L'attributo 'action' del form non è stato trovato. Userò l'URL base.")
            full_form_action_url = phpmyadmin_url

        print("\n   Campi di input trovati nel form:")
        # Trova tutti i tag <input> all'interno del form.
        input_fields = login_form.find_all('input')

        # Dizionario per memorizzare i nomi dei campi e i valori (se presenti)
        # In questo caso, ignoreremo l'estrazione specifica del token CSRF.
        form_details = {}

        for field in input_fields:
            field_name = field.get('name')
            field_type = field.get('type', 'text') # Default 'text' se type non specificato
            field_value = field.get('value', '') # Recupera il valore, utile per i campi hidden o i default

            if field_name: # Ci interessano solo i campi che hanno un attributo 'name'
                print(f"     - Nome: '{field_name}', Tipo: '{field_type}'")
                if field_type == 'hidden':
                    print(f"       (Campo nascosto - Valore: '{field_value}')")
                # Tutti i campi (inclusi gli hidden) vengono aggiunti al riepilogo
                form_details[field_name] = field_value # Salva il valore anche per i campi hidden

        print("\n   Riepilogo dei dettagli del form estratti:")
        print(f"   URL azione del form: {full_form_action_url}")
        print(f"   Nomi campi di input e valori default/hidden: {form_details}")

    else:
        print("✗ Errore: Nessun form trovato sulla pagina di phpMyAdmin. Assicurati che l'URL sia corretto e che la pagina contenga un form di login.")

except requests.exceptions.RequestException as e:
    print("✗ Errore durante l'ottenimento della pagina di login:", str(e))
except Exception as e:
    print("✗ Si è verificato un errore inatteso:", str(e))

print()
print("=== FINE ESTRAZIONE DETTAGLI FORM ===")
print("Ora hai i nomi dei campi di input e i valori dei campi nascosti (se presenti)")
print("che puoi usare per costruire un successivo tentativo di interazione.")

