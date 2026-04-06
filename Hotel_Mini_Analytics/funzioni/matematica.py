# Genera prezzo 
import random
import pandas as pd

def genera_prezzo():
    """
    Genera un prezzo realistico per una notte in hotel.
    Il prezzo è un numero intero scelto casualmente tra 80 e 250 euro.
    Utile per simulare dati di prenotazioni reali.
    """

    # definisco il prezzo minimo e massimo
    prezzo_minimo = 80
    prezzo_massimo = 250

    # genero un numero intero casuale nel range stabilito
    prezzo = random.randint(prezzo_minimo, prezzo_massimo)


    # ritorno il prezzo generato
    return prezzo

# Genera valutazione

def genera_valutazione():
    """
    Genera una valutazione realistica da parte del cliente.
    La valutazione è un numero decimale tra 3.0 e 5.0 con un solo decimale.
    """
    # definisco i limiti minimo e massimo della valutazione
    minimo = 3.0
    massimo = 5.0
    
    # genero un valore casuale tra 3.0 e 5.0
    valore_casuale =random.uniform(minimo, massimo)

    # arrotondo a un decimale
    valutazione = round(valore_casuale, 1)
    
    # ritorno la valutazione generata
    return valutazione

# Genera urgenza

def genera_urgente():
    """
    Genera un valore booleano che indica se la richiesta è urgente.
    Restituisce True nel 20% dei casi e False nell'80% dei casi.
    """
    # definisco le opzioni True/False
    elenco_valori = [True,False]


    # definisco i pesi per rendere più probabile False
    pesi =[20, 80]

    # scelgo il valore usando random
    risultato = random.choices(elenco_valori,weights= pesi)[0]



    # ritorno il valore generato
    return risultato

# converte prezzi con pandas

def converti_prezzo(df):
    """
    Converte la colonna 'Prezzo' in valori numerici interi.
    Eventuali valori non validi vengono trasformati in NaN e rimossi dal DataFrame.
    Restituisce il DataFrame con la colonna 'Prezzo' pulita e convertita.
    """
    # converto la colonna Prezzo in numeri interi
    df["Prezzo"] = pd.to_numeric(df["Prezzo"], errors="coerce")
    

    # elimino righe con prezzi non validi
    df = df.dropna(subset=["Prezzo"])
    

    return df

# converte valutazione con pandas
def converti_valutazione(df):
    """
    Converte la colonna 'Valutazione' in valori numerici float.
    Eventuali valori non validi vengono trasformati in NaN e rimossi dal DataFrame.
    Restituisce il DataFrame con la colonna 'Valutazione' pulita.
    """
    # converto la colonna Valutazione in float
    df["Valutazione"] = pd.to_numeric(df["Valutazione"], errors="coerce")
    

    # elimino righe con valutazioni non valide
    df = df.dropna(subset=["Valutazione"])
    

    return df


# converte urgente  con pandas
def converti_urgente(df):
    """
    Converte la colonna 'Urgente' in valori booleani reali (True/False).
    """
    # FIX: gestisce sia stringhe che booleani già letti da pandas
    df["Urgente"] = df["Urgente"].astype(str).map({"True": True, "False": False})
    df = df.dropna(subset=["Urgente"])
    return df





