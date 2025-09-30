class Retangulo:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def defineLados(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def mostraLados(self):
        return self.lado1, self.lado2
    def area(self):
        return self.lado1 * self.lado2    
    
    
    
a = Retangulo(10,20)
print(a.mostraLados())    