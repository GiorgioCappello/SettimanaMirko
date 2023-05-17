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

class Primo:

    tipo = 'macchina'

    def __init__(self,modello):
        self.modello = modello
    
    def to_string(self):
        print("Modello: " + self.modello)

class Secondo(Primo):

    def __init__(self,modello,targa):
        super().__init__(modello)
        self.targa = targa
    
    def to_string(self):
        print("Targa: " + self.targa)

class Terzo(Secondo):

    def __init__(self,modello,targa,colore):
        super().__init__(modello,targa)
        self.colore = colore
    
    def to_string(self):
        print("Colore: " + self.colore)

x = Primo("BMW")
x.to_string()
y = Secondo("BMW","AA000AA")
y.to_string()
z = Terzo("BMW","AA000AA","blu")
z.to_string()