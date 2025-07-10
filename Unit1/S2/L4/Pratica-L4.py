def perimetro():  ## inizio funzione perimetro
    print("**********************************************************************************")
    print("BENVENUTO NEL CALCOLATORE DEl PERIMETRO DI UNA FIGURA GEOMETRICA A TUA SCELTA!!!")      ## stampa a schermo il benvenuto
    print("**********************************************************************************")
    print("""                   
         - Quadrato  --> 1
         - Rettangolo--> 2
         - Triangolo --> 3
         - Equilatero--> 4
         - Isoscele  --> 5
         - Cerchio   --> 6       
          """)                 ## stampa a schermo le scelte che l'utente dovrà digitare
    
    print("Inserire la scelta: ")
    scelta = int(input("--> "))  ## variabile che descrive il valore che verrà inserito (input) dall'utente, (inte) serve a convertire un valore in un numero intero
    if scelta == 1:  ## if permette di eseguire un blocco di codice solo se una certa condizione è vera, in questo caso 1
        print("Hai scelto il calcolo del perimetro di un quadrato!")  ## stampato a schermo la conferma della scelta
        lato = input("Inserire il valore del lato: ")   ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        print(f"Il perimetro del quadrato avente lato {lato} è: {int(lato) *4}!!") ## stampa a schermo il risultato del perimetro, f permette di fare il calcolo all'interno della stringa
    elif scelta == 2:  ## if permette di eseguire un blocco di codice solo se una certa condizione è vera, in questo caso 1
        print("Hai scelto il calcolo del perimetro di un rettangolo!")  
        base = input("Inserire il valore della base: ")  ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        altezza = input("Inserire il valore dell'altezza: ")  ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        print(f"Il perimetro del rettangolo avente base {base} e altezza {altezza} è: {int(base)*int(altezza)}!!")  ## stampa a schermo il risultato del perimetro, f permette di fare il calcolo all'interno della stringa
    elif scelta == 3:  ## if permette di eseguire un blocco di codice solo se una certa condizione è vera, in questo caso 1
        print("Hai scelto il calcolo del perimetro di un triangolo!")
        lato1 = input("Inserire il valore di lato1: ")  ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        lato2 = input("Inserire il valore di lato2: ")  ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        lato3 = input("inserire il valore di lato3: ")  ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        print(f"Il perimetro del triangolo avente lato1 {lato1}, lato2 {lato2} e lato3 {lato3} è: {int(lato1)+int(lato2)+int(lato3)}!!")  ## stampa a schermo il risultato del perimetro, f permette di fare il calcolo all'interno della stringa
    elif scelta == 4:  ## if permette di eseguire un blocco di codice solo se una certa condizione è vera, in questo caso 1
        print("Hai scelto il calcolo del perimetro di un Triangolo Equilatero(lati dal valore uguale)!")
        lato = input("inserire il valore del lato: ")  ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        print(f"Il perimetro del triangolo equilatero avente lati dello stesso valore {lato} è: {int(lato) *3}!!")  ## stampa a schermo il risultato del perimetro, f permette di fare il calcolo all'interno della stringa
    elif scelta == 5:  ## if permette di eseguire un blocco di codice solo se una certa condizione è vera, in questo caso 1
        print("hai scelto il calcolo del perimetro di un Triangolo Isoscele(due lati uguali)!")
        base = input("Inserire il valore della base: ")  ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        lato = input("inserire il valore di lato: ")  ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        print(f"Il perimetro del triangolo isoscele avente due lati dello stesso valore {lato} e base {base} è: {int(base)+2*int(lato)}!!")  ## stampa a schermo il risultato del perimetro, f permette di fare il calcolo all'interno della stringa
    elif scelta == 6:  ## if permette di eseguire un blocco di codice solo se una certa condizione è vera, in questo caso 1
        print("Hai scelto il calcolo del perimetro di un Cerchio!")
        raggio = input("Inserire il valore del raggio: ")  ## variabile che consente di inserire tramite (input) all'utente il valore del lato
        π = 3.14  ## variabile pi greco è assegnata al valore 3.14
        print(f"Il perimetro del cerchio avente il raggio {raggio} e pi greco {π} è: {π*int(raggio)*2}!!")  ## stampa a schermo il risultato del perimetro, f permette di fare il calcolo all'interno della stringa
        
                                                                                                              
    else:
        print("Inserisci una scelta tra le opzioni!!!")    ##
    
        

perimetro()




