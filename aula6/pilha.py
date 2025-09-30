class Pilha:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = [None] * self.capacidade
        
    def pilhaCheia(self):
        print( self.topo == self.capacidade - 1 )
    
    def empilhar(self, valor):
        if self.pilhaCheia():
            print('Pilha cheia')
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def verTopo(self):
        if self.topo == -1:
            print('Pilha vazia')
        else:
            print(self.valores[self.topo])
            
    def pilhaVazia(self):
       print( self.topo == -1 )
    
    def desempilhar(self):
        if self.pilhaVazia():
            print('Pilha vazia')
        else:
            self.topo -= 1


pilha1 = Pilha(5)
pilha1.empilhar(10)
pilha1.empilhar(20)
pilha1.empilhar(30)
pilha1.verTopo()
pilha1.desempilhar()
pilha1.verTopo()
