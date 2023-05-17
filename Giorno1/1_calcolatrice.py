# calcolatrice parte uno

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
    
ciclo_uscita = True     # flag per uscire dal ciclo
cond_stampa = False     # flag per vedere se ho già eseguito un ciclo
lista_cicli = []        # lista per salvare i risultati intermedi
while ciclo_uscita:
    scelta = input("Scegliere operazione\nPremere 1 per eseguire operazione\nPremere 2 per vedere la stampa dell'ultimo ciclo\nPremere 0 per uscire\nInserire scelta: ")
    if scelta == '1':
        cond_stampa = True     
        lista_risultati = []
        sommatoria = 0
        for cont in range(3):
            a = int(input("1 per addizione\n2 per sottrazione\n3 per moltiplicazione\nInserire scelta: \n"))
            x = float(input("Inserire primo numero: "))
            y = float(input("Inserire secondo numero: "))
            if a == 1:
                lista_risultati.append(somma(x,y))
            elif a == 2:
                lista_risultati.append(diff(x,y))
            elif a == 3:
                lista_risultati.append(per(x,y))
            sommatoria += lista_risultati[cont]            
        print("La somma dei tre risultati viene:",sommatoria)

    elif scelta == '2':
        if not cond_stampa:
            print("Non hai ancora eseguito un ciclo")
        else:
            ciclo1 = risultati_ciclo(lista_risultati[0],lista_risultati[1],lista_risultati[2])
            lista_cicli.append(ciclo1)
        stampa = input("Vuoi una stampa a video? (si o no):\n")
        if stampa == 'si':
            print("Primo risultato:", ciclo1.primo)
            print("Secondo risultato:", ciclo1.secondo)
            print("Terzo risultato:", ciclo1.terzo)

    elif scelta == '0':
        print ("Arrivederci!")
        ciclo_uscita = False

    else:
        print("Scelta non disponibile")
