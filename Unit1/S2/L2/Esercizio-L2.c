#include <stdio.h> //Direttiva del processore, serve per caricare la libreria che contine le funzioni input/output standard di un programma c.

int main(){  //è la funzione principale dove il processore inizia a leggere le instruzioni quando in esecuzione
    printf("*******************************\n");
    printf("Benvenuto nel Moltiplicatore!!\n"); // tramite ptintf(funzione) riesco a scrivere scrivere a schermo ciò che è all'interno degli apici
    printf("*******************************\n");

    int primo; //dichiarazione delle variabili per i numeri inseriti
    int secondo; //dichiarazione delle variabili per i numeri inseriti
    int risultato; //dichiarazione delle variabili per il risultato


    printf("\nBenvenuto! dammi pure il primo numero: "); //tramite printf chiedo all'utente di scrivere il primo numero
    scanf("%d", &primo); //serve per leggere l'imput emesso dall'utente (%d INT)
    printf("\nComplimenti per la scelta! ora dammi pure il secondo numero: ", primo); //tramite printf chiedo all'utente di scrivere il secondo numero
    scanf("%d", &secondo); //serve per leggere l'imput emesso dall'utente (%d INT)
    risultato = primo * secondo;  //operazione tra i due numeri immessi dall'utente per il risultato (%d INT)
    printf("\nIl risultato è: %d", risultato);  //tramite printf viene scritta a schermo il risultato
    printf("\nTi sorprendo dicendo che la media fra i 2 numeri è: %0.2f\n",  (float) (primo + secondo) / (float) 2); /*tramite printf viene scritta a schermo la media aritmetica
    e fine linea viene aggiunta l'operazione per ottentere la media (%0.2f FLOAT)
    */
    
    return 0;

}