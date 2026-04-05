# Python Journey – Progetti Python

Questo repository raccoglie una selezione di progetti Python sviluppati durante il mio percorso di apprendimento.

Lo scopo del progetto è mostrare esempi pratici di utilizzo di Python per:

- gestione di dati
- automazione di operazioni semplici
- lettura e analisi di file
- interazione con l’utente da riga di comando

Il repository contiene solo progetti completi e funzionanti, non esercizi didattici.

---

## Progetti presenti

### Analisi spese da file CSV

Script Python che legge un file CSV contenente una lista di spese e:

- converte i valori numerici
- gestisce eventuali dati non validi
- salva i valori corretti in una lista per successive elaborazioni

File principale:

- `analisi_spese_csv.py`

Cartelle utilizzate:

- `progetti/input/` (file CSV di input)
- `progetti/output/` (eventuali file di output)

---

### Contatore e somma spese

Script Python che permette all’utente di:

- inserire più spese manualmente
- validare l’input dell’utente
- calcolare il totale delle spese
- contare quante spese sono state inserite

File principale:

## Gestione Spese – Python

## Descrizione

Programma Python da riga di comando per inserire una serie di spese e ottenere un riepilogo finale.

## Funzionalità

- Inserimento di più spese
- Validazione dell’input
- Accetta solo numeri positivi
- Uscita digitando "fine"
- Calcolo del totale e del numero di spese

## Come si usa

Esegui il programma e inserisci gli importi delle spese.  
Quando hai finito, scrivi `fine`.

## Esempio

Inserisci importo spesa (oppure 'fine'): 10  
Inserisci importo spesa (oppure 'fine'): 5.5  
Inserisci importo spesa (oppure 'fine'): fine  

Totale spese: 15.50  
Numero spese: 2  

## Competenze dimostrate

- Input/output da console
- if / while
- try / except
- Conversione dei tipi di dato
- Logica di controllo

## Stato

Progetto base completato.

## Menu Operazioni – Python

## Descrizione del menu

Programma Python da riga di comando che permette di eseguire diverse operazioni matematiche tramite un menu interattivo.

Il programma continua a funzionare finché l’utente non sceglie di uscire.

## Funzionalità del Menu

- Somma di due numeri
- Controllo se un numero è pari o dispari
- Moltiplicazione di due numeri
- Sottrazione di due numeri
- Divisione di due numeri (con controllo divisione per zero)
- Conteggio delle operazioni eseguite
- Calcolo delle percentuali di utilizzo di ogni operazione
- Riepilogo finale con operazione più usata

## Come si usa (Menu Operazioni)

1. Avvia il programma.
2. Scegli un’opzione dal menu digitando un numero (1–5).
3. Inserisci i valori richiesti.
4. Premi INVIO per tornare al menu.
5. Digita `esci` per terminare il programma e visualizzare il riepilogo.

## Esempio di utilizzo del menu

Scegli un numero del menu (1-2-3-4-5) oppure 'esci': 1  
Inserisci il primo numero: 10  
Inserisci il secondo numero: 5  
La somma di 10 + 5 è uguale a 15  

Scegli un numero del menu (1-2-3-4-5) oppure 'esci': esci  

Uscita  
Hai fatto 2 operazioni di somma  
Hai fatto 1 operazione di pari/dispari  
Per un totale di 3 operazioni  
Operazione più usata: somma

## Competenze dimostrate (Menu Operazioni)

- input / output da console
- if / elif / else
- while
- try / except
- gestione errori
- contatori e percentuali
- uso di dizionari e funzione `max()`
- logica di programma strutturata

## Stato del progetto

Completato – progetto dimostrativo per portfolio.
