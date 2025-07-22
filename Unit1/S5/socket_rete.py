import socket as so
SRV_ADDR = ('192.168.50.100')
SRV_PORT = 8080
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print(f"Server in ascolto su {SRV_ADDR}:{SRV_PORT}")
s.accept()
connection,address = s.accept()
print(f"Qualcuno si è connessa da {address[0]} usando la porta {address[1]}")
while True:
    data = connection.recv(1024)
    if not data:
        break
    print(f"Ricevuto: {data.decode()}")
    connection.sendall(data)
connection.sendall(b"Messaggio ricevuto\n")
print(data.decode('utf-8'))
connection.close()
s.close()