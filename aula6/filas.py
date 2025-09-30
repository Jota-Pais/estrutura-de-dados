class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.valores = [None] * self.capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0

    def filaCheia(self):
        return self.numero_elementos == self.capacidade

    def filaVazia(self):
        return self.numero_elementos == 0

    def enfileirar(self, valor):
        if self.filaCheia():
            print('ERRO: Fila já está cheia.')
            return

        self.final = (self.final + 1) % self.capacidade
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.filaVazia():
            print('ERRO: Fila já está vazia.')
            return None

        temp = self.valores[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.filaVazia():
            return None
        return self.valores[self.inicio]
    
    
    