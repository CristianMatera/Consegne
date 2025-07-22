import http.client
host = input("inserire ip/host del sistema target:  ")
port = input("inserire porta del sistema target (default 80):  ")
if(port == ""):
    port = 80
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request("OPTIONS", "/")