class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    
    def inserir(self, dado):
        novo = Node(dado)
        if self.head is None:
            self.head = novo
        else:
            atual = self.head
            while atual.prox:
                atual = atual.prox
            atual.prox = novo

    
    def imprimir(self):
        atual = self.head
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.prox
        print("None")

    def excluir_primeiro(self):
        if self.head:
            self.head = self.head.prox

    
    def excluir(self, valor):
        atual = self.head
        anterior = None
        while atual:
            if atual.dado == valor:
                if anterior:
                    anterior.prox = atual.prox
                else:
                    self.head = atual.prox
                return True
            anterior = atual
            atual = atual.prox
        return False

    def pesquisar(self, valor):
        atual = self.head
        while atual:
            if atual.dado == valor:
                return True
            atual = atual.prox
        return False

lista = ListaEncadeada()

for letra in "joao carlos":
    lista.inserir(letra)

print("Lista inicial:")
lista.imprimir()

lista.excluir_primeiro()

print("Após exclusão do primeiro:")
lista.imprimir()

print("Pesquisa pelo último caractere 's':", lista.pesquisar("s"))

lista.excluir("c")

print("Após exclusão do 'c':")
lista.imprimir()
