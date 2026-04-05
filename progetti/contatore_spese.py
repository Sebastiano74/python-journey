"""
Gestione Spese - Python

Programma da riga di comando che permette all'utente di inserire
una serie di spese e ottenere un riepilogo finale.

Funzionalità:
- Inserimento spese una alla volta
- Controllo input (solo numeri positivi)
- Uscita digitando 'fine'
- Riepilogo con totale e numero di spese

Autore: Vito Sebastiano Giaquinta
Data: 01/04/2026
"""

# Variabili per il riepilogo finale
totale = 0.0
conteggio = 0

# Ciclo principale: continua finché l'utente non scrive "fine"
while True:
    spesa = input("Inserisci importo spesa (oppure 'fine' per uscire): ").strip()

    # Controllo uscita
    if spesa.lower() == "fine":
        break

    try:
        spesa = float(spesa)

        # Accettiamo solo importi positivi
        if spesa > 0:
            totale += spesa
            conteggio += 1
        else:
            print("Inserisci un numero maggiore di 0")

    except ValueError:
        print("Valore non valido, riprova")

# Riepilogo finale
print(f"Totale spese: {totale:.2f}")
print(f"Numero spese: {conteggio}")
    


