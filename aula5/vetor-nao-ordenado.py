class VetorNaoOrdenado:
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = [0] * capacidade
    
    def inserir(self, valor):
        if self.ultimaPosicao == self.capacidade -1:
            print('vetor cheio')
        else:
            self.ultimaPosicao += 1
            self.valores[self.ultimaPosicao] = valor
    
    def imprimir(self):
        if self.ultimaPosicao == -1:
            print('vetor vazio')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i,'-',self.valores[i])
    
    def pesquisar(self, valor):
        for i in range(self.ultimaPosicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
    
    def excluir(self,valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.valores[self.ultimaPosicao] = 0
            self.ultimaPosicao -= 1
            return 1




vetor = VetorNaoOrdenado(7)

vetor.inserir('J')
vetor.inserir('o')
vetor.inserir('a')
vetor.inserir('o')

vetor.imprimir()
        
vetor.pesquisar('a')
vetor.pesquisar('o')
vetor.pesquisar('J')
        
vetor.excluir('J')
vetor.excluir('a')
vetor.excluir('o')

vetor.imprimir()
        
        
        
                
        
        
            
         
    
             
    
    
    
    
    
    
    
    
    