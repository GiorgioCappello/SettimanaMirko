# menù da copiare

scelta = 'ok'

def switch(scelta):
    if scelta == '1':
        return "Sei un programmatore eccezionale, capace di creare soluzioni innovative e codice di alta qualità. Il tuo talento è davvero ammirevole."
    elif scelta == '2':
        return "Sei un programmatore che ha bisogno di migliorare la precisione e l'attenzione ai dettagli. Presta maggiore attenzione alla scrittura del codice"
    elif scelta == '3':
        return "Ammiro la tua dedizione e passione per la programmazione. Il tuo impegno nel migliorare costantemente le tue abilità e imparare nuove tecnologie è davvero encomiabile."
    elif scelta == '0':
        print("Arrivederci!")

print("Benvenuto nel simulatore di motivational coaching per programmatori!")
while(scelta != '0'):

    scelta = input("Premere 1 per ricevere un complimento\nPremere 2 per ricevere un insulto\nPremere 3 per essere motivato\nPremere 0 per uscire\nInserire scelta (a tuo rischio e pericolo):")

    print(switch(scelta))