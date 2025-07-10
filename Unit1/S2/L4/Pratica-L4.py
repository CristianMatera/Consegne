def perimetro():
    print("**********************************************************************************")
    print("BENVENUTO NEL CALCOLATORE DEl PERIMETRO DI UNA FIGURA GEOMETRICA A TUA SCELTA!!!")
    print("**********************************************************************************")
    print("""
         - Quadrato  --> 1
         - Rettangolo--> 2
         - Triangolo --> 3
         - Equilatero--> 4
         - Isoscele  --> 5
         - Cerchio   --> 6       
          """)
    
    print("Inserire la scelta: ")
    scelta = int(input("--> "))
    if scelta == 1:
        print("Hai scelto il calcolo del perimetro di un quadrato!")
        lato = input("Inserire il valore del lato: ")
        print(f"Il perimetro del quadrato avente lato {lato} è: {int(lato) *4}!!")
    elif scelta == 2:
        print("Hai scelto il calcolo del perimetro di un rettangolo!")
        base = input("Inserire il valore della base: ")
        altezza = input("Inserire il valore dell'altezza: ")
        print(f"Il perimetro del rettangolo avente base {base} e altezza {altezza} è: {int(base)*int(altezza)}!!")
    elif scelta == 3:
        print("Hai scelto il calcolo del perimetro di un triangolo!")
        lato1 = input("Inserire il valore di lato1: ")
        lato2 = input("Inserire il valore di lato2: ")
        lato3 = input("inserire il valore di lato3: ")
        print(f"Il perimetro del triangolo avente lato1 {lato1}, lato2 {lato2} e lato3 {lato3} è: {int(lato1)+int(lato2)+int(lato3)}!!")
    elif scelta == 4:
        print("Hai scelto il calcolo del perimetro di un Triangolo Equilatero(lati dal valore uguale)!")
        lato = input("inserire il valore del lato: ")
        print(f"Il perimetro del triangolo equilatero avente lati dello stesso valore {lato} è: {int(lato) *3}!!")
    elif scelta == 5:
        print("hai scelto il calcolo del perimetro di un Triangolo Isoscele(due lati uguali)!")
        base = input("Inserire il valore della base: ")
        lato = input("inserire il valore di lato: ")
        print(f"Il perimetro del triangolo isoscele avente due lati dello stesso valore {lato} e base {base} è: {int(base)+2*int(lato)}!!")
    elif scelta == 6:
        print("Hai scelto il calcolo del perimetro di un Cerchio!")
        raggio = input("Inserire il valore del raggio: ")
        π = 3.14
        print(f"Il perimetro del cerchio avente il raggio {raggio} e pi greco {π} è: {π*int(raggio)*2}!!")
        
                                                                                                              
    else:
        print("Inserisci una scelta tra le opzioni!!!")    
        

perimetro()




