import datetime
import random
import pandas as pd

def genera_data_casuale():
    """
    Genera una data casuale tra 30 giorni fa e 5 giorni nel futuro.
    La data è restituita come stringa nel formato DD/MM/YYYY.
    """
    oggi = datetime.date.today()
    giorno_casuale = random.randint(-30, 5)
    data_casuale = datetime.timedelta(days=giorno_casuale)
    data_finale = oggi + data_casuale
    data = data_finale.strftime("%d/%m/%Y")
    return data


def converti_date(df):
    """
    Converte la colonna 'Date' in oggetti datetime.
    Gestisce eventuali date non valide.
    """
    # fix: era df["Data"], ma nel CSV la colonna si chiama "Date"
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")

    df = df.dropna(subset=["Date"])

    return df
    