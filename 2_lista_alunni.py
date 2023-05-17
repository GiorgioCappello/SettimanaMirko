# CREARE UNA CLASSE LISTAALLUNNI, che dovrà essere sempre valorizzata appena si accede al primo menu,  
# Un primo menu con entra o esci, se esci si chiude tutto, 
# se entri devi darmi X nomi obbligatori e X corrispettivi voti agli studenti, 
# L'esericizio sarà creare un sistema che permetta di andare a scegliere un singolo utente e, creando 
# una nuova classe con ereditarietà, di modificare e aggiungere i suoi voti 


# creo classe ListaAlunni con all'inerno aggiungi alunno, aggiungi voto
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

    
# creo classe per visualizzare alunno e modificare il voto



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
                lista_alunni.aggiungi_voto(voto_alunno)
    
    else: 
        # errore
        print("Scelta non valida! Riprova")



