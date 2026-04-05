"""
Analisi Spese da File CSV

Programma Python che legge un file CSV contenente importi di spesa,
converte i valori validi in numeri e ignora quelli non validi.

Funzionalità:
- Lettura di un file CSV (una spesa per riga)
- Conversione in float
- Scarto dei valori non validi
- Riepilogo finale delle spese valide

Autore: Vito Sebastiano Giaquinta
Data: 01/04/2026
"""

# Percorso del file CSV
PERCORSO_FILE = "progetti/input/spese.csv"

# Lista che conterrà le spese valide
spese = []


# Apertura del file in modalità lettura
with open(PERCORSO_FILE, encoding="utf-8") as file:
    for riga in file:
        riga = riga.strip()

        # Salta le righe vuote
        if not riga:
            continue

        try:
            valore = float(riga)
            spese.append(valore)
        except ValueError:
            print(f"Valore non valido ignorato: '{riga}'")


# Riepilogo finale
print("\nSpese valide lette dal file:")
print(spese)

if spese:
    totale = sum(spese)
    media = totale / len(spese)

    print(f"\nTotale spese: {totale:.2f}")
    print(f"Numero spese: {len(spese)}")
    print(f"Spesa media: {media:.2f}")
else:
    print("\nNessuna spesa valida trovata.")