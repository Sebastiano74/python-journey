"""
Menu Operazioni - Python

Programma da riga di comando che permette di eseguire diverse
operazioni matematiche tramite un menu interattivo.

Funzionalità:
- Somma di due numeri
- Controllo pari/dispari
- Moltiplicazione
- Sottrazione
- Divisione con controllo divisione per zero
- Riepilogo finale con contatori, percentuali e operazione più usata

Uso:
- Seleziona un numero dal menu (1–5)
- Digita 'esci' per terminare il programma

Autore: Vito Sebastiano Giaquinta
Data: 05/04/2026
"""

# Contatori per il riepilogo finale
contatore_somma = 0
contatore_pari_dispari = 0
contatore_moltiplicazioni = 0
contatore_sottrazione = 0
contatore_divisione = 0


# Ciclo principale del menu
while True:
    print("*" * 29)
    print("*          MENU             *")
    print("* 1 Somma due numeri        *")
    print("* 2 Controlla pari/dispari  *")
    print("* 3 Moltiplica due numeri   *")
    print("* 4 Sottrai due numeri      *")
    print("* 5 Dividi due numeri       *")
    print("*  per uscire scrivi 'Esci' *")
    print("*" * 29)

    selezione = input(
        "Scegli un numero del menu (1-2-3-4-5) oppure 'esci': "
    ).strip()

    # Uscita e riepilogo finale
    if selezione.lower() == "esci":
        totale = (
            contatore_somma
            + contatore_pari_dispari
            + contatore_moltiplicazioni
            + contatore_sottrazione
            + contatore_divisione
        )

        print("\nUscita")
        print(f"Somma: {contatore_somma}")
        print(f"Pari/Dispari: {contatore_pari_dispari}")
        print(f"Moltiplicazione: {contatore_moltiplicazioni}")
        print(f"Sottrazione: {contatore_sottrazione}")
        print(f"Divisione: {contatore_divisione}")
        print(f"Totale operazioni: {totale}")

        if totale > 0:
            print("\nPercentuali:")
            print(f"Somma: {(contatore_somma / totale) * 100:.1f}%")
            print(f"Pari/Dispari: {(contatore_pari_dispari / totale) * 100:.1f}%")
            print(f"Moltiplicazione: {(contatore_moltiplicazioni / totale) * 100:.1f}%")
            print(f"Sottrazione: {(contatore_sottrazione / totale) * 100:.1f}%")
            print(f"Divisione: {(contatore_divisione / totale) * 100:.1f}%")

            operazioni = {
                "somma": contatore_somma,
                "pari/dispari": contatore_pari_dispari,
                "moltiplicazione": contatore_moltiplicazioni,
                "sottrazione": contatore_sottrazione,
                "divisione": contatore_divisione,
            }

            piu_usata = max(operazioni, key=operazioni.get)
            print(
                f"\nOperazione più usata: "
                f"{piu_usata} ({operazioni[piu_usata]} volte)"
            )
        else:
            print("Non hai eseguito nessuna operazione.")

        break

    # Somma
    elif selezione == "1":
        try:
            a = int(input("Inserisci il primo numero: "))
            b = int(input("Inserisci il secondo numero: "))
            print(f"Risultato: {a + b}")
            contatore_somma += 1
            input("Premi INVIO per tornare al menu...")
        except ValueError:
            print("Errore: inserisci numeri interi validi")

    # Pari / Dispari
    elif selezione == "2":
        try:
            n = int(input("Inserisci un numero: "))
            if n % 2 == 0:
                print("Il numero è pari")
            else:
                print("Il numero è dispari")
            contatore_pari_dispari += 1
            input("Premi INVIO per tornare al menu...")
        except ValueError:
            print("Errore: inserisci un numero valido")

    # Moltiplicazione
    elif selezione == "3":
        try:
            a = int(input("Inserisci il primo numero: "))
            b = int(input("Inserisci il secondo numero: "))
            print(f"Risultato: {a * b}")
            contatore_moltiplicazioni += 1
            input("Premi INVIO per tornare al menu...")
        except ValueError:
            print("Errore: inserisci numeri interi validi")

    # Sottrazione
    elif selezione == "4":
        try:
            a = int(input("Inserisci il primo numero: "))
            b = int(input("Inserisci il secondo numero: "))
            print(f"Risultato: {a - b}")
            contatore_sottrazione += 1
            input("Premi INVIO per tornare al menu...")
        except ValueError:
            print("Errore: inserisci numeri interi validi")

    # Divisione
    elif selezione == "5":
        try:
            a = int(input("Inserisci il primo numero: "))
            b = int(input("Inserisci il secondo numero: "))
            if b == 0:
                print("Errore: divisione per zero non consentita")
            else:
                print(f"Risultato: {a / b}")
                contatore_divisione += 1
                input("Premi INVIO per tornare al menu...")
        except ValueError:
            print("Errore: inserisci numeri interi validi")

    else:
        print("Scelta non valida. Riprova.")
      



                

            

    
      
    