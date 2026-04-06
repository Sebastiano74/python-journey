# Messaggio Casuale

import random

def genera_messaggio_casuale():
    """
    Restituisce un messaggio casuale scelto da una lista di richieste
    realistiche fatte dai clienti di un hotel.
    Utile per generare dati finti ma credibili nei progetti di simulazione.
    """

    # lista di messaggi realistici suddivisi per categorie

    #  Gruppo 1: Check-in / Check-out
    gruppo_1 = ["Late check-in possibile?",
                "Arriverò alle 23:45 va bene?",
                "Possiamo fare il check-in anticipato?",
                "È possibile lasciare i bagagli prima del check-in?",
                "Possiamo lasciare i bagagli dopo il check-out?"]
    
    # Gruppo 2: Famiglie / Bambini
    gruppo_2 = ["Serve una culla in camera.",
                "Avete un lettino per bambini?",
                "Possiamo avere una stanza silenziosa per il bambino?"]
    
    # Gruppo 3: Parcheggio
    gruppo_3 = ["Richiesta info sul parcheggio.",
                "Il parcheggio è incluso?",
                "Posso prenotare un posto auto?",
                "Avete parcheggio per auto grande?"]
    
    # Gruppo 4: Camera e comfort
    gruppo_4 = ["Camera silenziosa, per favore.",
                "È disponibile una camera ai piani alti?",
                "Servono due cuscini extra.",
                "Ci sono asciugamani extra?"]
    
    # Gruppo 5: Servizi dell’hotel
    gruppo_5 = ["Colazione inclusa?",
                "A che ora è la colazione?",
                "Avete servizio navetta?",
                "Il Wi-Fi è gratuito?"]
    
    # Gruppo 6: Richieste urgenti
    gruppo_6 = ["Abbiamo un problema urgente con la prenotazione.",
                 "Siamo arrivati e non troviamo l’ingresso.",
                 "Serve assistenza immediata.",
                 "La carta non funziona potete aiutarci subito?"]
    
    # unisco tutti i messaggi in un'unica lista
    lista_messaggi = gruppo_1 + gruppo_2 + gruppo_3 + gruppo_4 + gruppo_5 + gruppo_6

    # scelgo un messaggio casuale dalla lista

    messaggio = random.choice(lista_messaggi)


    return messaggio


# Genera provenienza

def genera_provenienza():
    """
    Restituisce una provenienza  casuale scelto da una lista di piattaforme
    realistiche.
    Utile per generare dati finti ma credibili nei progetti di simulazione.
    """

    # lista delle possibili provenienze
    # OTA
    ota_lista = ["Booking",
                 "Expedia",
                 "Hotels.com",
                 "Agoda"]
    
    # Metasearch
    metasearch_lista = ["Google Travel",
                        "TripAdvisor"]
    
    # Direct
    direct_lista = ["Direct",
                    "Email",
                    "Telefono",
                    "WalkIn"]
    
    # unisco tutte le provenienze in un'unica lista
    provenienza_lista = ota_lista + metasearch_lista + direct_lista

    # selezione casuale della provenienza
    provenienza = random.choice(provenienza_lista)

    # ritorno della provenienza scelta
    return provenienza





    


    






