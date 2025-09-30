class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = [None] * self.capacidade

    def imprimir(self):
        if self.ultimaPosicao == -1:
            print('O vetor está vazio')
        else:
            print("Índice - Valor")
            print("-------------")
            for i in range(self.ultimaPosicao + 1):
                print(f'{i:^6} - {self.valores[i]}')

    def inserir(self, valor):
        if self.ultimaPosicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao_inserir = 0
        while posicao_inserir <= self.ultimaPosicao and self.valores[posicao_inserir] < valor:
            posicao_inserir += 1

        for i in range(self.ultimaPosicao, posicao_inserir - 1, -1):
            self.valores[i + 1] = self.valores[i]

        self.valores[posicao_inserir] = valor
        self.ultimaPosicao += 1

    def pesquisar(self, valor):
        limite_inferior = 0
        limite_superior = self.ultimaPosicao

        while limite_inferior <= limite_superior:
            meio = (limite_inferior + limite_superior) // 2
            
            if self.valores[meio] == valor:
                return meio
            elif self.valores[meio] < valor:
                limite_inferior = meio + 1
            else:
                limite_superior = meio - 1
        
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultimaPosicao -= 1
            self.valores[self.ultimaPosicao + 1] = None
            return 1
        
        
