# calcolatrice parte due

ciclo_uscita = True     # flag per uscire dal ciclo
cond_stampa = False     # flag per vedere se ho già eseguito un ciclo
lista_cicli = []        # lista per salvare i risultati intermedi

def somma(uno,due):
    return uno + due
    
def diff(uno,due):
    return uno - due
    
def per(uno,due):
    return uno * due

class risultati_ciclo:
        def __init__(self, primo, secondo, terzo):
            self.primo = primo
            self.secondo = secondo
            self.terzo = terzo
    
while ciclo_uscita:
    scelta = input("Scegliere operazione\nPremere 1 per eseguire operazione\nPremere 2 per salvare il ciclo e vedere tutti i cicli salvati\nPremere 3 per pulire i dati\nPremere 0 per uscire\nInserire scelta: ")
    if scelta == '1':
        cond_stampa = True     # ciclo eseguito
        lista_risultati = []    # ogni volta azzero la lista risultati
        sommatoria = 0          # e la sommatoria
        for cont in range(3):
            a = int(input("1 per addizione\n2 per sottrazione\n3 per moltiplicazione\nInserire scelta: \n"))
            x = float(input("Inserire primo numero: "))
            y = float(input("Inserire secondo numero: "))
            if a == 1:
                lista_risultati.append(somma(x,y))  # inserisco nella lista risultati l'operazione richiesta
            elif a == 2:
                lista_risultati.append(diff(x,y))
            elif a == 3:
                lista_risultati.append(per(x,y))
            sommatoria += lista_risultati[cont]           # incremento la sommatoria ad ogni ciclo
        print("La somma dei tre risultati viene:",sommatoria)   # e la stampo

    elif scelta == '2':
        if not cond_stampa:     # controllo se ho eseguito almeno un ciclo di operazioni
            print("Non hai ancora eseguito un ciclo")
        else:
            ciclo1 = risultati_ciclo(lista_risultati[0],lista_risultati[1],lista_risultati[2]) #salvo in ciclo1 gli ultimi risultati eseguiti
            lista_cicli.append(ciclo1)      # e li inserisco nella lista_cicli
            stampare = input("Vuoi una stampa a video? (si o no):\n")
            if stampare == 'si':
                for elemento in lista_cicli: # scorro e stampo tutti gli elementi salvati 
                    print("Primo risultato:", elemento.primo, "Secondo risultato:", elemento.secondo, "Terzo risultato:", elemento.terzo)
                    print("")

    elif scelta == '3':
        lista_cicli = []        # azzero la lista_cicli
        cond_stampa = False     # reimposto la condizione di salvare elementi
        print("Calcolatrice resettata correttamente!")            

    elif scelta == '0':
        print ("Arrivederci!")  #esco
        ciclo_uscita = False

    else:
        print("Scelta non disponibile")
