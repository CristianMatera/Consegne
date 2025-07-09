def SalutoIniziale(x):
    saluto=f"{x}"
    return saluto

x = "BENVENUTO NEL GENERATORE DI NOMI PER LA TUA BAND!!"
print(SalutoIniziale(x))

def domanda1(nome):
    Risposta1=f"Ciao,{nome}!"
    return Risposta1

nome = input("Come ti chiami?")
print(domanda1(nome))

def domanda2(NomeCane):
    Risposta2=f"Bellissimo nome {NomeCane}!"
    return Risposta2

NomeCane =  input("Come si chiama il tuo animale domestico?")
print(domanda2(NomeCane)) 

def domanda3(Città,):
    Risposta3=f"Bellissima città {Città}, spero che {NomeCane} si trovi benissimo!!"
    return Risposta3

Città = input("dove abitate?")
print(domanda3(Città))

def Generatore(Band):
    Risposta4=f"Il nome della tua nuova famossisima Banda sarà: {Band}"
    return Risposta4

Band = NomeCane+Città
print(Generatore(Band))
