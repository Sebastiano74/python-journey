# Gestione spese
# Sebastiano Giaquinta

totale = 0
conteggio = 0

while True:
    spesa = input("Inserisci importo spesa (oppure 'fine' per uscire): ")

    if spesa.lower() == "fine":
        break

    try:
        spesa = float(spesa)
        if spesa > 0:
            totale += spesa
            conteggio += 1
        else:
            print("Inserisci un numero maggiore di 0")
    except ValueError:
        print("Valore non valido, riprova")

print(f"Totale spese: {totale:.2f}")
print(f"Numero spese: {conteggio}")
    
    


