# ereditarietà

'''class Persona:

    tipo = 'umano'

    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
    
    def masterD(self):
        print("Ciao sono " + self.nome + " " + self.tipo)

x = Persona("Mirko", 99)
x.masterD()

class Allievo(Persona):

    def __init__(self,nome,eta,grado):
        super().__init__(nome,eta)
        self.grado = grado
    
    def masterD(self):
        print("Ciao sono " + self.nome + " " + self.tipo + " " + self.grado)

y = Allievo("Marius",23,"Terzo Dan")
y.masterD()'''

# Tre generazioni

class Primo:

    tipo = 'macchina'

    def __init__(self,modello):
        self.modello = modello
    
    def to_string1(self):
        print("Modello: " + self.modello)

class Secondo(Primo):

    def __init__(self,modello,targa):
        super().__init__(modello)
        self.targa = targa
    
    def to_string2(self):
        print("Targa: " + self.targa)

class Terzo(Secondo):

    def __init__(self,modello,targa,colore):
        super().__init__(modello,targa)
        self.colore = colore
    
    def to_string3(self):
        x.to_string1()
        y.to_string2()
        print("Colore: " + self.colore)

x = Primo("BMW")
y = Secondo("Mercedes","BB000BB")
z = Terzo("Wolksvagen","CC000CC","blu")


z.to_string3()
