# Vito Sebastiano Giaquinta, Data 01/04/2026

lista = []
percorso = "progetti/input/spese.csv"
with open(percorso) as f:
    for riga in f:
        riga = riga.strip()
        try:
            numero = float(riga)
            lista.append(numero)
        except:
            print(f"Valore non valido {riga}")
print(lista)
      