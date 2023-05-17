# 10- Creare un menu ad inserimento che permetta in loop di inserire un nome e una password e che dopo li verifichi 
# scrivendo "loggato!" 


# verificare credenziali per accedere (manca magari un controllo su quante password puoi sbagliare e un tasto per uscire)
# ma per ora penso sia accettabile così

'''def verifica_credenziali():
    while True:
        nome = input("Inserire nome utente: ")
        password = input ("Inserire password: ")
        
        if nome == 'Giacomo' and password == '1234':
            return 1
        else:
            print("Accesso negato! Riprova:")


def switch_accesso():
    print("Benvenuto!")
    while True:
        print("Seleziona un'opzione:\n1 per loggare\n0 per uscire")
        scelta = input("")
        if scelta == '0':
            print("Arrivederci!")
            break
        elif scelta == '1':
            if verifica_credenziali() == 1:
                print("loggato!")
                break
            # una volta loggato posso andare avanti qui togliendo il break
        else:
            print("Scelta non valida! Riprova:")


switch_accesso()'''


# 11- Andare a creare un sistema di ordinazione di ferie, che permetta sulla base di tre proposte di modificare i vari 
# parametri di esse spesa, tempo di viaggio e vista mare (int, string, bool  ) e che poi stampi il tutto chiedendo 
# conferma, in quest'esercizio dovrete usare almeno ( oggetto: utente con validazione  e SceltaFerie coi dati)

# uso esercizio 1 per verificare credenziali. Per ora accetta solo Giacomo, non faccio in tempo a creare anche il processo
# di registrazione nuovo account

def verifica_credenziali():
    while True:
        nome = input("Inserire nome utente: ")
        password = input ("Inserire password: ")
        
        if nome == 'Giacomo' and password == '1234':
            return 1
        else:
            print("Accesso negato! Riprova:")

# classe coi dati
class SceltaFerie:
    def __init__(self, spesa, tempo_viaggio, vista_mare):
        self.spesa = spesa
        self.tempo_viaggio = tempo_viaggio
        self.vista_mare = vista_mare

# funzione per richiedere i dati e modificare le ferie
def modifica_ferie(ferie):
    print("Modifica i parametri delle ferie:")
    spesa = int(input("Spesa (in euro): "))
    tempo_viaggio = input("Tempo di viaggio: ")
    vista_mare = input("Vista mare (si/no): ")

    if spesa > 0 and (vista_mare == 'si' or vista_mare == 'no'):
        ferie.spesa = spesa
        ferie.tempo_viaggio = tempo_viaggio
        ferie.vista_mare = vista_mare
    else:
        print("Scelta non valida, i dati non sono stati salvati! Riporvare:")

# funzione per stampare le ferie
def stampa_scelta_ferie(ferie):
    print("\nEcco la tua scelta di ferie:")
    print("Spesa: " + str(ferie.spesa) + " euro")
    print("Tempo di viaggio: " + ferie.tempo_viaggio)
    print("Vista mare: " + ferie.vista_mare)

# funzione che resituisce un booleano        
def conferma_scelta():
    scelta = input("Vuoi confermare la scelta delle ferie? (si/no): ")
    return scelta == "si"

# switch per gestire le scelte 
def switch_scelte():
    while True:
        print("Premi 1 per modificare le tue scelte\nPremi 2 per visualizzare e confermare\nScrivi 'exit' per tornare indietro")
        scelta_modifica = input("")
        ferie = SceltaFerie(0, "", "")
        if scelta_modifica == '1':
            modifica_ferie(ferie)
            stampa_scelta_ferie(ferie)
        elif scelta_modifica == '2':
            stampa_scelta_ferie(ferie)
            if conferma_scelta():
                print("Scelta confermata. Buone ferie!")
                break
            else:
                print("Scelta annullata.")
        elif scelta_modifica == 'exit':
            break
        else:
            print("Scelta non valida! Riprova:")


def switch_accesso():
    print("Benvenuto!")
    while True:
        print("Seleziona un'opzione:\n1 per loggare\n0 per uscire")
        scelta = input("")
        if scelta == '0':
            print("Arrivederci!")
            break
        elif scelta == '1':
            if verifica_credenziali() == 1:
                print("\nBenvenuto!")
                switch_scelte()
        else:
            print("Scelta non valida! Riprova:")


switch_accesso()

# Avessi più tempo prima di tutto aggiungeri vari controlli per l'inserimento di dati corretti. 
# Poi farei il processo di registrazione e qualcosa (magari un dizionario) per salvare le modifiche
# se si conferma la scelta e di non salvarle se si esce senza confermare.