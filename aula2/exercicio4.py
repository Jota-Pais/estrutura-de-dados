class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    def defineLado(self, lado):
        self.lado = lado
    def mostraLado(self):
        return self.lado
    def area(self):
        return self.lado * self.lado    
    