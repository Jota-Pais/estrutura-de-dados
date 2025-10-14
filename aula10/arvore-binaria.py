class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_no(self):
        print(self.valor)

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        # A variável 'ligacoes' não é usada nas funções, mas foi mantida
        # conforme o código original.
        self.ligacoes = []

    def inserir(self, valor):
        novo = No(valor)
        # Se a árvore estiver vazia
        if self.raiz is None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                # Esquerda
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual is None:
                        pai.esquerda = novo
                        return
                # Direita
                else:
                    atual = atual.direita
                    if atual is None:
                        pai.direita = novo
                        return

    def pesquisar(self, valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual is None:
                return None
        return atual

    # Raiz, esquerda, direita
    def pre_ordem(self, no):
        if no is not None:
            print(no.valor, end=' ')
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    # Esquerda, raiz, direita
    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.valor, end=' ')
            self.em_ordem(no.direita)

    # Esquerda, direita, raiz
    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor, end=' ')

    def excluir(self, valor):
        if self.raiz is None:
            print('A árvore está vazia')
            return

        # Encontrar o nó
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True
        while atual.valor != valor:
            pai = atual
            # Esquerda
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            # Direita
            else:
                e_esquerda = False
                atual = atual.direita
            if atual is None:
                return False

        # O nó a ser apagado é uma folha (não tem filhos)
        if atual.esquerda is None and atual.direita is None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda:
                pai.esquerda = None
            else:
                pai.direita = None

        # O nó a ser apagado não possui filho na direita
        elif atual.direita is None:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            elif e_esquerda:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda

        # O nó a ser apagado não possui filho na esquerda
        elif atual.esquerda is None:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif e_esquerda:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita

        # O nó possui dois filhos
        else:
            sucessor = self.get_sucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esquerda:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor
            sucessor.esquerda = atual.esquerda
        
        return True

    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita
        while atual is not None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        
        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
            
        return sucessor

# Exemplo de como usar o código:
arvore = ArvoreBinariaBusca()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

print("Percurso em ordem:")
arvore.em_ordem(arvore.raiz) # Saída: 20 30 40 50 60 70 80
print("\n")

print("Excluindo o nó 20 (folha):")
arvore.excluir(20)
arvore.em_ordem(arvore.raiz)
print("\n")

print("Excluindo o nó 70 (tem dois filhos):")
arvore.excluir(70)
arvore.em_ordem(arvore.raiz)
print("\n")

print("Pesquisando pelo valor 60:")
resultado = arvore.pesquisar(60)
if resultado:
    print(f"Nó encontrado: {resultado.valor}")
else:
    print("Nó não encontrado.")