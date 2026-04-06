import os

from funzioni.file import (
    crea_csv_hotel,
    leggi_csv_hotel,
    pulisci_dati_hotel,
    scrivi_log,
    crea_report_csv,
    crea_report_txt,
    crea_report_pdf
)

from funzioni.analisi import (
    analisi_completa,
    analisi_provenienza,
    analisi_prezzo,
    analisi_valutazione,
    analisi_urgenti
)


def menu():
    print("\n=== HOTEL DATA ANALYSIS ===")
    print("1) Genera nuovo CSV hotel")
    print("2) Leggi e pulisci CSV")
    print("3) Esegui analisi completa")
    print("4) Genera report (CSV, TXT, PDF)")
    print("5) Mostra grafici")
    print("6) Esci")
    scelta = input("\nSeleziona un'opzione: ")
    return scelta


def main():

    scrivi_log("Programma avviato")

    while True:
        scelta = menu()

        # =============================================
        # 1) GENERA CSV
        # =============================================
        if scelta == "1":
            percorso_csv = "input/hotel_data.csv"
            crea_csv_hotel(percorso_csv)
            scrivi_log("Creato nuovo CSV hotel.")
            print("\n Nuovo CSV generato!")

        # =============================================
        # 2) LEGGI E PULISCI CSV
        # =============================================
        elif scelta == "2":
            percorso_csv = "input/hotel_data.csv"
            df = leggi_csv_hotel(percorso_csv)
            # FIX: controllo che il file esista prima di procedere
            if df is None:
                print("\n File CSV non trovato. Genera prima il CSV (opzione 1).")
                continue
            df = pulisci_dati_hotel(df)
            scrivi_log("CSV letto e pulito.")
            print("\n CSV letto e pulito con successo!")

        # =============================================
        # 3) ANALISI COMPLETA
        # =============================================
        elif scelta == "3":
            percorso_csv = "input/hotel_data.csv"
            df = leggi_csv_hotel(percorso_csv)
            # FIX: controllo che il file esista prima di procedere
            if df is None:
                print("\n File CSV non trovato. Genera prima il CSV (opzione 1).")
                continue
            df = pulisci_dati_hotel(df)
            risultati = analisi_completa(df)
            scrivi_log("Analisi completa eseguita.")
            print("\n Analisi completa eseguita!")

        # =============================================
        # 4) GENERA REPORT
        # =============================================
        elif scelta == "4":
            percorso_csv = "input/hotel_data.csv"
            df = leggi_csv_hotel(percorso_csv)
            # FIX: controllo che il file esista prima di procedere
            if df is None:
                print("\n File CSV non trovato. Genera prima il CSV (opzione 1).")
                continue
            df = pulisci_dati_hotel(df)
            risultati = analisi_completa(df)

            crea_report_csv(df, risultati, "output/report.csv")
            crea_report_txt(df, risultati, "output/report.txt")
            crea_report_pdf(df, risultati, "output/report.pdf")

            scrivi_log("Report generati (CSV, TXT, PDF).")
            print("\n Report generati nella cartella output/!")

        # =============================================
        # 5) MOSTRA GRAFICI
        # =============================================
        elif scelta == "5":
            percorso_csv = "input/hotel_data.csv"
            df = leggi_csv_hotel(percorso_csv)
            # FIX: controllo che il file esista prima di procedere
            if df is None:
                print("\n File CSV non trovato. Genera prima il CSV (opzione 1).")
                continue
            df = pulisci_dati_hotel(df)

            print("\n Mostro i grafici...")
            analisi_provenienza(df)
            analisi_prezzo(df)
            analisi_valutazione(df)
            analisi_urgenti(df)

            scrivi_log("Grafici mostrati all'utente.")

        # =============================================
        # 6) ESCI
        # =============================================
        elif scelta == "6":
            scrivi_log("Programma terminato dall'utente.")
            print("\n Uscita dal programma. A presto!")
            break

        else:
            print("\n Scelta non valida, riprova.")


if __name__ == "__main__":
    main()