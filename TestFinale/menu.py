# Uno script di python che con un menu gestisca la creazione di un OGGETTO UTENTE con ( nome, cognome, password, e soldi )
# con login e registrazione e che gli permetta se loggato di cambiare i dati o di eliminare il suo account 

utenti = []
############################################ Classi ###################################
class Utente:
    def __init__(self, nome, cognome, password, soldi):
        self.nome = nome
        self.cognome = cognome
        self.password = password
        self.soldi = soldi

    def to_string(self):
        print(f'Nome: {self.nome}\nCognome: {self.cognome}\nPassword: {self.password}\nSoldi : {self.soldi}\n')

########################################### Funzioni ####################################

# Creazione di un nuovo utente
def registrazione():
    try:    
        nome = input("Inserisci il tuo nome: ")
        cognome = input("Inserisci il tuo cognome: ")
        password = input("Inserisci la password: ")
        soldi = float(input("Inserisci l'importo dei tuoi soldi: "))
        return Utente(nome, cognome, password, soldi)
    except:
        print("Errore, non è stato possibile creare il nuovo account")
        return None

# Login
def login(utenti):
    username = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")

    for utente in utenti:
        if utente.nome == username and utente.password == password:
            return utente

    return None

# Modifica dei dati dell'utente corrente
def modifica_dati(utente):
    nuovo_nome = input("Inserisci il nuovo nome (premi invio senza scrivere nulla per non modificare): ")
    nuovo_cognome = input("Inserisci il nuovo cognome (premi invio senza scrivere nulla per non modificare): ")
    nuova_password = input("Inserisci la nuova password (premi invio senza scrivere nulla per non modificare): ")
    nuovo_soldi = input("Inserisci il nuovo importo dei soldi (premi invio senza scrivere nulla per non modificare): ")

    if nuovo_nome:
        utente.nome = nuovo_nome
    if nuovo_cognome:
        utente.cognome = nuovo_cognome
    if nuova_password:
        utente.password = nuova_password
    if nuovo_soldi:
        utente.soldi = float(nuovo_soldi)

# Eliminare un utente
def elimina_account(utenti, utente):
    utenti.remove(utente)
    print("Account eliminato con successo.")

# Conferma scelta
def conferma():
    while True:
        scelta_conferma = input("Sei sicuro della tua scelta? (si/no): ")
        if scelta_conferma.lower() == 'si':
            return True
        elif scelta_conferma.lower() == 'no':
            return False
        else:
            print("Errore, scelta non valida")

######################################### Switch ######################################

# Switch iniziale
def switch_iniziale():
    print("Benvenuto!")
    while True:
        print("1. Accedere al sistema")
        print("0. Uscire")
        scelta_iniziale = input("Inserire scelta: ")
        if scelta_iniziale == '0':
            print("Arrivederci!")
            break
        elif scelta_iniziale == '1':
            switch_accesso(utenti)
        else:
            print("Errore, scelta non disponibile\n")

# Switch di accesso
def switch_accesso(utenti):
    while True:
        print("\nBenvenuto nell'area di accesso")
        print("1. Login")
        print("2. Registrare un nuovo account")
        print("0. Tornare indietro")
        scelta_accesso = input("Inserire scelta: ")
        if scelta_accesso == '0':
            break
        elif scelta_accesso == '1':
            utente_corrente = login(utenti)
            if utente_corrente:
                print("Accesso effettuato correttamente!\n")
                switch_interna(utenti, utente_corrente)
            else:
                print("Credenziali non valide!")
        elif scelta_accesso == '2':
            nuovo_utente = registrazione()
            if nuovo_utente:
                utenti.append(nuovo_utente)
                print("Registrazione avvenuta correttamente!")
            else:
                print("Riprova! \n")
        else:
            print("Errore, scelta non disponibile\n")

# Switch interna per modifiche
def switch_interna(utenti, utente_corrente):
    print("Benvenuto! Ecco le tue informazioni:")
    utente_corrente.to_string()
    while True:
        print("\n1. Modifica i dati")
        print("2. Elimina account")
        print("3. Visualizza dati")
        print("0. Effettua il Log out")
        scelta = input("Inserire scelta: ")
        if scelta == '0':
            print("Arrivederci!")
            break
        elif scelta == '1':
            if conferma():
                modifica_dati(utente_corrente)
        elif scelta == '2':
            if conferma():
                elimina_account(utenti, utente_corrente)
                break
        elif scelta == '3':
            utente_corrente.to_string()
        else:
            print("Errore, scelta non valida!")

######################################## App #############################################

switch_iniziale()