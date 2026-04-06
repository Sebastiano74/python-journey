# Hotel Mini Analytics

Programma Python da riga di comando per la generazione, pulizia e analisi di dati di prenotazioni alberghiere.

---

## Descrizione

Hotel Mini Analytics genera automaticamente un dataset CSV con dati realistici di un hotel (date, provenienza, prezzi, valutazioni, messaggi e urgenza), lo pulisce e produce analisi statistiche complete con grafici e report in più formati.

---

## Funzionalità

- **Generazione dati** – Crea un file CSV con dati hotel realistici generati automaticamente
- **Pulizia dati** – Converte e valida tutte le colonne (date, prezzi, valutazioni, urgenza)
- **Analisi completa** – Statistiche su prezzi, valutazioni, provenienza e richieste urgenti
- **Grafici** – Visualizzazioni con matplotlib (istogrammi, grafici a barre, torta)
- **Report multipli** – Esporta i risultati in formato CSV, TXT e PDF
- **Log automatico** – Ogni operazione viene registrata in `output/log.txt`

---

## Struttura del progetto

```
Hotel_Mini_Analytics/
│
├── main.py                  # Entry point – menu interattivo
├── funzioni/
│   ├── analisi.py           # Analisi statistiche e grafici
│   ├── file.py              # Lettura, pulizia CSV e generazione report
│   ├── matematica.py        # Generazione e conversione valori numerici
│   ├── date.py              # Generazione e conversione date
│   └── stringhe.py          # Generazione messaggi e provenienza
│
├── input/
│   └── hotel_data.csv       # File CSV generato dal programma
│
└── output/
    ├── report.csv           # Report in formato CSV
    ├── report.txt           # Report in formato TXT
    ├── report.pdf           # Report in formato PDF
    └── log.txt              # Log delle operazioni
```

---

## Come si usa

1. Clona il repository e installa le dipendenze:

```bash
git clone https://github.com/Sebastiano74/python-journey.git
cd python-journey/Hotel_Mini_Analytics
pip install -r requirements.txt
```

1. Avvia il programma:

```bash
python main.py
```

1. Scegli un'opzione dal menu:

```
=== HOTEL DATA ANALYSIS ===
1) Genera nuovo CSV hotel
2) Leggi e pulisci CSV
3) Esegui analisi completa
4) Genera report (CSV, TXT, PDF)
5) Mostra grafici
6) Esci
```

> **Nota:** eseguire prima l'opzione 1 per generare il CSV, poi procedere con le altre opzioni.

---

## Colonne del CSV

| Colonna      | Descrizione                        |
|--------------|------------------------------------|
| Date         | Data della prenotazione            |
| Provenienza  | Canale di provenienza del cliente  |
| Prezzo       | Prezzo della prenotazione (€)      |
| Valutazione  | Valutazione del cliente (1–10)     |
| Messaggio    | Messaggio lasciato dal cliente     |
| Urgente      | Indica se la richiesta è urgente   |

---

## Dipendenze

## Stato

Progetto completato – sviluppato come progetto dimostrativo per portfolio.

```
## Stato

Progetto completato – sviluppato come progetto dimostrativo per portfolio.

- pandas
- numpy
- matplotlib
- reportlab

Installazione:
```

Installazione:

```bash
pip install -r requirements.txt
```

---

## Competenze dimostrate

- Struttura a package Python con moduli separati
- Pandas – lettura, pulizia e analisi di DataFrame
- NumPy – calcolo percentili e operazioni su array
- Matplotlib – grafici a barre, istogrammi, torta
- ReportLab – generazione di PDF programmatica
- Gestione file (CSV, TXT, PDF, log)
- Menu interattivo da riga di comando
- Gestione errori e controllo input

---

## Autore

**Vito Sebastiano Giaquinta**  
[GitHub](https://github.com/Sebastiano74)

---

## Stato

Progetto completato – sviluppato come progetto dimostrativo per portfolio.
