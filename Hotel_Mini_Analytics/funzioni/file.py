import os
import pandas as pd
from datetime import datetime
import numpy as np

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from .date import genera_data_casuale, converti_date
from .stringhe import genera_messaggio_casuale, genera_provenienza
from .matematica import genera_prezzo, genera_valutazione, genera_urgente, \
    converti_prezzo, converti_valutazione, converti_urgente


def crea_riga_hotel():
    """
    Crea una singola riga realistica del CSV hotel.
    Combina: data, provenienza, prezzo, valutazione, messaggio e urgenza.
    Restituisce la riga già pronta in formato CSV.
    """
    data = genera_data_casuale()
    provenienza = genera_provenienza()
    prezzo = genera_prezzo()
    valutazione = genera_valutazione()
    messaggio = genera_messaggio_casuale()
    urgente = genera_urgente()

    riga = data + ";" + provenienza + ";" + str(prezzo) + ";" + \
           str(valutazione) + ";" + messaggio + ";" + str(urgente)
    return riga


def crea_csv_hotel(percorso_file):
    """
    Crea il file CSV hotel con dati realistici generati automaticamente.
    Scrive l'intestazione e un numero definito di righe usando crea_riga_hotel().
    Ritorna il percorso completo del file creato.
    """
    cartella = os.path.dirname(percorso_file)
    os.makedirs(cartella, exist_ok=True)
    print(f"Cartella creata: {cartella}")

    with open(percorso_file, "w", encoding="utf-8") as f:
        # FIX: intestazione con ";" per coerenza con le righe dati
        f.write("Date;Provenienza;Prezzo;Valutazione;Messaggio;Urgente\n")
        for i in range(20):
            riga = crea_riga_hotel()
            f.write(riga + "\n")

    return percorso_file


def leggi_csv_hotel(percorso_file):
    """
    Legge il CSV dell'hotel e restituisce un DataFrame Pandas.
    Controlla che il file esista.
    """
    esiste_file = os.path.exists(percorso_file)
    if not esiste_file:
        print("Il file non è stato trovato")
        return None

    df = pd.read_csv(percorso_file, sep=";")
    print(df)
    return df


def pulisci_dati_hotel(df):
    """
    Pulisce tutte le colonne del DataFrame hotel.
    Applica le conversioni: Date, Prezzo, Valutazione, Urgente.
    Restituisce un DataFrame pulito e coerente.
    """
    df = converti_date(df)
    df = converti_prezzo(df)
    df = converti_valutazione(df)
    df = converti_urgente(df)
    return df


def scrivi_log(messaggio):
    """
    Scrive un messaggio nel file output/log.txt con data e ora.
    Se la cartella non esiste, la crea automaticamente.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs("output", exist_ok=True)
    percorso = "output/log.txt"
    with open(percorso, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {messaggio}\n")


def crea_report_csv(df, risultati, percorso_report):
    """
    Crea un file CSV con tutte le metriche dell'analisi hotel.
    """
    os.makedirs("output", exist_ok=True)

    with open(percorso_report, "w", encoding="utf-8") as f:
        f.write("metrica,valore\n")

        f.write(f"prezzo_minimo,{risultati['prezzo']['minimo']}\n")
        f.write(f"prezzo_massimo,{risultati['prezzo']['massimo']}\n")
        f.write(f"prezzo_medio,{risultati['prezzo']['media']}\n")
        f.write(f"prezzo_mediana,{risultati['prezzo']['mediana']}\n")

        prezzi_array = df["Prezzo"].to_numpy()
        perc75 = np.percentile(prezzi_array, 75)
        f.write(f"prezzo_percentile_75,{perc75}\n")

        f.write(f"valutazione_minima,{risultati['valutazione']['minimo']}\n")
        f.write(f"valutazione_massima,{risultati['valutazione']['massimo']}\n")
        f.write(f"valutazione_media,{risultati['valutazione']['media']}\n")
        f.write(f"valutazione_mediana,{risultati['valutazione']['mediana']}\n")

        f.write(f"percentuale_urgenti,{risultati['urgenti']['percentuale_urgenti']}\n")
        f.write(f"percentuale_non_urgenti,{risultati['urgenti']['percentuale_non_urgenti']}\n")

        provenienza_top = risultati["provenienza"].idxmax()
        f.write(f"provenienza_top,{provenienza_top}\n")


def crea_report_txt(df, risultati, percorso_txt):
    """
    Crea un report leggibile in formato TXT con tutte le metriche dell'analisi hotel.
    """
    os.makedirs("output", exist_ok=True)

    prezzi_array = df["Prezzo"].to_numpy()
    perc75 = np.percentile(prezzi_array, 75)

    with open(percorso_txt, "w", encoding="utf-8") as f:
        f.write("REPORT HOTEL\n")
        f.write("------------------------\n\n")

        f.write(" PREZZI\n")
        f.write(f"Prezzo minimo: {risultati['prezzo']['minimo']}€\n")
        f.write(f"Prezzo massimo: {risultati['prezzo']['massimo']}€\n")
        f.write(f"Prezzo medio: {risultati['prezzo']['media']:.2f}€\n")
        f.write(f"Prezzo mediana: {risultati['prezzo']['mediana']:.2f}€\n")
        f.write(f"Prezzo 75° percentile: {perc75:.2f}€\n\n")

        f.write(" VALUTAZIONI\n")
        f.write(f"Valutazione minima: {risultati['valutazione']['minimo']}\n")
        f.write(f"Valutazione massima: {risultati['valutazione']['massimo']}\n")
        f.write(f"Valutazione media: {risultati['valutazione']['media']:.2f}\n")
        f.write(f"Valutazione mediana: {risultati['valutazione']['mediana']:.2f}\n\n")

        f.write(" PROVENIENZA\n")
        provenienza_top = risultati["provenienza"].idxmax()
        f.write(f"Provenienza più frequente: {provenienza_top}\n\n")

        f.write(" RICHIESTE URGENTI\n")
        f.write(f"Percentuale urgenti: {risultati['urgenti']['percentuale_urgenti']:.2f}%\n")
        f.write(f"Percentuale non urgenti: {risultati['urgenti']['percentuale_non_urgenti']:.2f}%\n\n")

        f.write(" TOTALE RICHIESTE\n")
        f.write(f"Totale richieste: {len(df)}\n")


def crea_report_pdf(df, risultati, percorso_pdf):
    """
    Crea un report PDF con tutte le metriche dell'analisi hotel.
    """
    os.makedirs("output", exist_ok=True)

    prezzi_array = df["Prezzo"].to_numpy()
    perc75 = np.percentile(prezzi_array, 75)

    c = canvas.Canvas(percorso_pdf, pagesize=A4)
    larghezza, altezza = A4
    y = altezza - 50

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "REPORT HOTEL - Analisi Dati")
    y -= 40

    c.setFont("Helvetica", 12)

    c.drawString(50, y, " PREZZI")
    y -= 20
    c.drawString(70, y, f"Prezzo minimo: {risultati['prezzo']['minimo']}€")
    y -= 15
    c.drawString(70, y, f"Prezzo massimo: {risultati['prezzo']['massimo']}€")
    y -= 15
    c.drawString(70, y, f"Prezzo medio: {risultati['prezzo']['media']:.2f}€")
    y -= 15
    c.drawString(70, y, f"Prezzo mediana: {risultati['prezzo']['mediana']:.2f}€")
    y -= 15
    c.drawString(70, y, f"Prezzo 75° percentile: {perc75:.2f}€")
    y -= 30

    c.drawString(50, y, " VALUTAZIONI")
    y -= 20
    c.drawString(70, y, f"Valutazione minima: {risultati['valutazione']['minimo']}")
    y -= 15
    c.drawString(70, y, f"Valutazione massima: {risultati['valutazione']['massimo']}")
    y -= 15
    c.drawString(70, y, f"Valutazione media: {risultati['valutazione']['media']:.2f}")
    y -= 15
    c.drawString(70, y, f"Valutazione mediana: {risultati['valutazione']['mediana']:.2f}")
    y -= 30

    c.drawString(50, y, " PROVENIENZA")
    y -= 20
    provenienza_top = risultati["provenienza"].idxmax()
    c.drawString(70, y, f"Provenienza più frequente: {provenienza_top}")
    y -= 30

    c.drawString(50, y, " RICHIESTE URGENTI")
    y -= 20
    c.drawString(70, y, f"Percentuale urgenti: {risultati['urgenti']['percentuale_urgenti']:.2f}%")
    y -= 15
    c.drawString(70, y, f"Percentuale non urgenti: {risultati['urgenti']['percentuale_non_urgenti']:.2f}%")
    y -= 30

    c.drawString(50, y, " TOTALE RICHIESTE")
    y -= 20
    c.drawString(70, y, f"Totale richieste: {len(df)}")

    c.save()