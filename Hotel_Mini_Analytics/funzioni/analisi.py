import pandas as pd
import matplotlib.pyplot as plt

def analisi_provenienza(df):
    """
    Analizza la provenienza delle richieste e mostra il conteggio per ogni sorgente.
    Restituisce una serie Pandas con i conteggi.
    """
    conteggi = df["Provenienza"].value_counts()
    print(conteggi)
    conteggi.plot(kind="bar")
    plt.show()
    return conteggi


def analisi_prezzo(df):
    """
    Analizza la distribuzione dei prezzi contenuti nel DataFrame.
    Calcola statistiche principali come prezzo minimo, massimo e medio.
    Mostra inoltre un istogramma dei prezzi per visualizzare la distribuzione.
    Restituisce un dizionario con le statistiche calcolate.
    """
    minimo = df["Prezzo"].min()
    massimo = df["Prezzo"].max()
    media = df["Prezzo"].mean()
    mediana = df["Prezzo"].median()

    print(f"Prezzo minimo: {minimo:.2f}€")
    print(f"Prezzo massimo: {massimo:.2f}€")
    print(f"Prezzo medio: {media:.2f}€")
    print(f"Prezzo mediana: {mediana:.2f}€")

    df["Prezzo"].plot(kind="hist", bins=10)
    plt.show()

    return {
        "minimo": minimo,
        "massimo": massimo,
        "media": media,
        "mediana": mediana
    }


def analisi_valutazione(df):
    """
    Analizza la distribuzione delle valutazioni dei clienti.
    Calcola statistiche principali come minimo, massimo, media e mediana.
    Mostra inoltre un istogramma delle valutazioni per visualizzarne la distribuzione.
    Restituisce un dizionario con le statistiche calcolate.
    """
    minimo = df["Valutazione"].min()
    massimo = df["Valutazione"].max()
    media = df["Valutazione"].mean()
    mediana = df["Valutazione"].median()

    print(f"Valutazione minima: {minimo:.2f}")
    print(f"Valutazione massima: {massimo:.2f}")
    print(f"Valutazione media: {media:.2f}")
    print(f"Valutazione mediana: {mediana:.2f}")

    df["Valutazione"].plot(kind="hist", bins=10)
    plt.show()

    return {
        "minimo": minimo,
        "massimo": massimo,
        "media": media,
        "mediana": mediana
    }


def analisi_urgenti(df):
    """
    Analizza la colonna 'Urgente' del DataFrame.
    Calcola il numero e la percentuale di richieste urgenti e non urgenti.
    Mostra un grafico a torta per visualizzare la distribuzione.
    Restituisce un dizionario con i risultati dell'analisi.
    """
    conteggi = df["Urgente"].value_counts()
    totale = conteggi.sum()

    # .get() evita crash se True o False non esistono nel CSV
    urgenti = conteggi.get(True, 0)
    non_urgenti = conteggi.get(False, 0)
    percentuale_true = (urgenti / totale * 100)
    percentuale_false = (non_urgenti / totale * 100)  # fix typo: folse → false

    print(f"Percentuale urgenti: {percentuale_true:.1f}%")
    print(f"Percentuale non urgenti: {percentuale_false:.1f}%")

    conteggi.plot(kind="pie", autopct="%1.1f%%")
    plt.show()

    return {
        "urgenti": urgenti,
        "non_urgenti": non_urgenti,
        "percentuale_urgenti": percentuale_true,
        "percentuale_non_urgenti": percentuale_false  # fix typo
    }


def analisi_completa(df):
    """
    Esegue tutte le analisi disponibili sul DataFrame hotel.
    Include analisi di: Provenienza, Prezzo, Valutazione e Urgenza.
    Restituisce un dizionario completo con le statistiche aggregate.
    """
    risultati_provenienza = analisi_provenienza(df)
    risultati_prezzo = analisi_prezzo(df)
    risultati_valutazione = analisi_valutazione(df)
    risultati_urgenti = analisi_urgenti(df)

    return {
        "provenienza": risultati_provenienza,
        "prezzo": risultati_prezzo,
        "valutazione": risultati_valutazione,
        "urgenti": risultati_urgenti
    }





