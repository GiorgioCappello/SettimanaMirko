# CREARE UNA CLASSE LISTAalunni, che dovrà essere sempre valorizzata appena si accede al primo menu,  
# Un primo menu con entra o esci, se esci si chiude tutto, 
# se entri devi darmi X nomi obbligatori e X corrispettivi voti agli studenti, 
# L'esericizio sarà creare un sistema che permetta di andare a scegliere un singolo utente e, creando 
# una nuova classe con ereditarietà, di modificare e aggiungere i suoi voti 


# creo classe ListaAlunni con all'inerno aggiungi alunno, aggiungi voto, visualizzo elenco
class ListaAlunni:
    
    def __init__(self):
        self.alunni = {}

    def aggiungi_alunno(self, nome):
        self.alunni[nome] = []

    def aggiungi_voto(self, nome, voto):
        if nome in self.alunni:
            self.alunni[nome].append(voto)
        else:
            print("Alunno non presente nella lisa!")

    def visualizzo_elenco(self):
        print("\nElenco alunni: ")
        for nome,voti in self.alunni.items():
            print("Nome: ", nome)
            print("Voti: ", voti)
            print()


# creo classe per visualizzare alunno, modificare il voto o aggiungerlo 
class Alunno(ListaAlunni):
    def __init__(self, lista):
        super().__init__()
        self.alunni = lista.alunni

    def modifica_voto(self, nome, indice, voto):
        if nome in self.alunni:
            if indice < len(self.alunni[nome]):
                self.alunni[nome][indice] = voto
                self.visualizza_alunno(nome)
            else:
                print("Indice del voto non valido.")
        else:
            print("Alunno non presente nella lista.")

    def aggiungi_voto2(self, nome, nuovo_voto):
        if nome in self.alunni:
            self.alunni[nome].append(nuovo_voto)
            self.visualizza_alunno(nome)
        else:
            print("Allunno non presente nella lista.")

    def visualizza_alunno(self, nome):
        if nome in self.alunni:
            print("Voti di", nome, ":")
            for voto in self.alunni[nome]:
                print(voto)
        else:
            print("Alunno non presente nella lista.")




lista_alunni = ListaAlunni()
print("Benvenuto!")
while True:
    scelta_menu = input("Entra (1) o Esci (0)\n")
    
    if scelta_menu == '0':
        # uscita
        print("Arrivederci!")
        break
    
    elif scelta_menu == '1':
        
        # chiedo quanti alunni inserire
        num_alunni = int(input("Inserisci il numero di alunni da aggiungere: "))

        # ciclo per richiedere num_alunni
        for i in range(num_alunni):
            nome_alunno = input("Inserire nome dell'alunno: ")
            lista_alunni.aggiungi_alunno(nome_alunno)
            num_voti_alunno = int(input("Inserire numeri di voti dell'alunno: "))
            
            # ciclo per aggiungere voto all'alunno
            for j in range(num_voti_alunno):
                print("Inserire voto", j+1, ": ")
                voto_alunno = float(input(""))
                if voto_alunno > 10 or voto_alunno <= 0:
                    print("Non puoi inserire ", voto_alunno, "come voto! Verrà messo 0 in automatico... Poi modificalo!")
                    lista_alunni.aggiungi_voto(nome_alunno, 0)
                else:
                    lista_alunni.aggiungi_voto(nome_alunno, voto_alunno)

        lista_alunni.visualizzo_elenco()

        # chiedo se si vuole modificare un voto
        while True:
            scelta_alunno = input("Vuoi selezionare un alunno? (si o no): ")

            if scelta_alunno == 'no':
                break
            elif scelta_alunno == 'si':
                nome_selezionato = input("Inserisci il nome dell'alunno da selezionare: ")

                # creo la classe alunno
                alunno = Alunno(lista_alunni)
                alunno.visualizza_alunno(nome_selezionato)
                
                # se l'alunno esiste chiedo di modificare o aggiungere
                if nome_selezionato in lista_alunni.alunni:
                    while True:
                        scelta_modifica = input("Vuoi modificare (M) o aggiungere (A) un voto? (M/A): ")
                        
                        # modifica
                        if scelta_modifica == 'M':
                            indice = int(input("Inserisci indice del voto da modificare: "))
                            nuovo_voto = input("Inserisci il nuovo voto: ")
                            alunno.modifica_voto(nome_selezionato, indice, nuovo_voto)
                            break
                        
                        # aggiungo
                        elif scelta_modifica == 'A':
                            nuovo_voto = input("Inserisci il nuovo voto: ")
                            alunno.aggiungi_voto(nome_selezionato, nuovo_voto)
                            break

                        else:
                            # errore
                            print("Scelta non valida! Riprova")
            else:
                # errore
                print("Scelta non valida! Riprova")

    else: 
        # errore
        print("Scelta non valida! Riprova")
