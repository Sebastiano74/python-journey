# Sebastiano Giaquinta

"""print("*" * 29)
print("*          MENU             *")
print("* 1 Somma due numeri        *")
print("* 2 Controlla pari/dispari  *")
print("* 3 Moltiplica due numeri   *")
print("*  per uscire scrivi 'Esci' *")
print("*" * 29)"""

contatore_somma = 0
contatore_pari_dispari = 0
contatore_moltiplicazioni = 0
contatore_sottrazione = 0
contatore_divisione =0



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
    selezione = input("Scegli un numero del menu (1-2-3-4-5) oppure 'esci': ").strip()

    if selezione.lower() == "esci":
        print("Uscita")
        print(f"Hai fatto {contatore_somma} operazioni di somma")
        print(f"Hai fatto {contatore_pari_dispari} operazioni di pari/dispari")
        print(f"Hai fatto {contatore_moltiplicazioni} operazioni di moltiplicazione")
        print(f"Hai fatto {contatore_sottrazione} operazioni di sottrazione")
        totale = (contatore_somma+contatore_pari_dispari+contatore_moltiplicazioni+contatore_sottrazione+contatore_divisione)
        print(f"Per un totale di {totale} operazioni")
        
        if totale > 0:
            p_somma = (contatore_somma / totale) * 100
            p_pari = (contatore_pari_dispari / totale) * 100
            p_molt = (contatore_moltiplicazioni / totale) * 100
            p_sott = (contatore_sottrazione / totale) * 100
            p_div = (contatore_divisione / totale) * 100

            print(f"Somma: {p_somma:.1f}%")
            print(f"Pari/Dispari: {p_pari:.1f}%")
            print(f"Moltiplicazione: {p_molt:.1f}%")
            print(f"Sottrazione: {p_sott:.1f}%")
            print(f"Divisione: {p_div:.1f}%")
        
        if totale == 0:
            print("Non hai eseguito nessuna operazione.")
        else:        
            operazioni = {
            "somma": contatore_somma,
            "pari/dispari": contatore_pari_dispari,
            "moltiplicazione": contatore_moltiplicazioni,
            "sottrazione": contatore_sottrazione,
            "divisione": contatore_divisione,
            }

            piu_usata = max(operazioni, key=operazioni.get)
            print(f"L'operazione più usata è stata: {piu_usata} ({operazioni[piu_usata]} volte)")



        break

    elif selezione == "1":
        try:
            numero_a = int(input("Inserisci il primo numero: ").strip())
            numero_b = int(input("Inserisci il secondo numero: ").strip())
            somma = numero_a + numero_b
            print(f"La somma di {numero_a} + {numero_b} è uguale a {somma}")
            input("Premi INVIO per tornare al menu...")
            contatore_somma += 1
        except ValueError:
            print("Errore: inserisci due numeri interi validi")

    elif selezione == "2":
        try:
            numero_c = int(input("Inserisci un numero: ").strip())
            if numero_c % 2 == 0:
                print(f"Il numero {numero_c} è pari")
                input("Premi INVIO per tornare al menu...")
            else:
                print(f"Il numero {numero_c} è dispari")
                input("Premi INVIO per tornare al menu...")
            contatore_pari_dispari += 1
        except ValueError:
            print("Errore: inserisci un numero intero valido")

    elif selezione == "3":
        try:
            numero_a = int(input("Inserisci il primo numero: ").strip())            
            numero_b = int(input("Inserisci il secondo numero: ").strip())
            prodotto = numero_a * numero_b
            print(f"La moltiplicazione di {numero_a} * {numero_b} è uguale a {prodotto}")
            input("Premi INVIO per tornare al menu...")
            contatore_moltiplicazioni += 1
                

        
        except ValueError:
            print("Errore: inserisci due numeri interi validi")


    elif selezione == "4":
        try:
            numero_a = int(input("Inserisci il primo numero: ").strip())
            numero_b = int(input("Inserisci il secondo numero: ").strip())
            prodotto = numero_a - numero_b
            print(f"La sottrazione di {numero_a} / {numero_b} è uguale a {prodotto}")
            input("Premi INVIO per tornare al menu...")
            contatore_sottrazione += 1
        except ValueError:
            print("Errore: inserisci due numeri interi validi")


    elif selezione == "5":
        try:
            numero_a = int(input("Inserisci il primo numero: ").strip())
            numero_b = int(input("Inserisci il secondo numero: ").strip())
            if numero_b ==0:
                print("Errore: divisione per zero non consentita")
            else:
                prodotto = numero_a / numero_b
                print(f"La diisione di {numero_a} - {numero_b} è uguale a {prodotto}")
                input("Premi INVIO per tornare al menu...")
                contatore_divisione += 1
            
            
        except ValueError:
            print("Errore: inserisci due numeri interi validi")







    else:
        print("Scelta non valida. Inserisci 1, 2, 3, 4 oppure 'esci'.")
      



                

            

    
      
    