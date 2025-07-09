def SalutoIniziale(x): ## definizione della funzione "saluto iniziale"
    saluto=f"{x}"
    return saluto

x = "BENVENUTO NEL GENERATORE DI NOMI PER LA TUA BAND!!" ## x è la variabile con associato il messaggio di benvenuto
print(SalutoIniziale(x))  ## stampa a schermo il saluto 

def domanda1(nome): ## definizione della funzione "domanda1"    
    Risposta1=f"Ciao,{nome}!"  
    return Risposta1

nome = input("Come ti chiami?") ## nome è una variabile che si ottiene tramite l'imput dell'utente che risponde alla domanda "come ti chiami?"
print(domanda1(nome))  ## stampa a schermo Risposta1 cioè "ciao, cristian!"

def domanda2(NomeCane): ## definizione della funzione "domanda2"
    Risposta2=f"Bellissimo nome {NomeCane}!"
    return Risposta2

NomeCane =  input("Come si chiama il tuo animale domestico?")  ##NomeCane è una variabili che si ottiene tramite l'imput dell'utente che risponde alla domanda "come si chiama il tuo animale domestico?"
print(domanda2(NomeCane)) ## stampa a schermo Risposta2 cioè "bellissimo nome coby"

def domanda3(Città,):
    Risposta3=f"Bellissima città {Città}, spero che {NomeCane} si trovi benissimo!!" ## definizione della funzione "domanda3"
    return Risposta3

Città = input("dove abitate?")  ## Città è una variabile che si ottiene tramite l'imput dell'utente che risponde alla domanda "dove abitate?"
print(domanda3(Città)) ## stampo a schermo Risposta3 cioè "bellissima città Brescia, spero che coby si trovi benissimo!!"

def Generatore(Band): ## definizione della funzione "Generatore"
    Risposta4=f"Il nome della tua nuova famossisima Band sarà: {Band}"
    return Risposta4

Band = NomeCane+Città  ## Band è una variabile che si ottiene tramite insieme di NomeCane+Città
print(Generatore(Band))  #stampa a schermo Risposta4 cioè "il nome della tua nuova famossisima Band sarà: Coby Brescia"
