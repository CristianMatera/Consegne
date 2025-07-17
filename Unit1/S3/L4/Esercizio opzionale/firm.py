from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64


# Carica la chiave privata
with open('/home/kali/Desktop/Consegna/Consegne/Unit1/S3/L4/Esercizio opzionale/private_key.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)
# Carica la chiave pubblica
with open('/home/kali/Desktop/Consegna/Consegne/Unit1/S3/L4/Esercizio opzionale/public_key.pem', 'rb') as key_file:
     public_key = serialization.load_pem_public_key(key_file.read())

message = 'Ciao, Epicode spacca!'
# Firma con la chiave privata
signed = private_key.sign( message.encode(), padding.PKCS1v15(), hashes.SHA256())
# Verifica della firma con la chiave pubblica
encrypted_b64 = base64.b64encode(signed).decode('utf-8')
try:
     
     public_key.verify(signed, message.encode(), padding.PKCS1v15(), hashes.SHA256())
     print("Base64 della firma:", encrypted_b64)
     print("Messaggio originale da confrontare:", message)
     print("La firma è valida.")
except Exception as e:
     print("La firma non è valida.", str(e))