class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def lista_vazia(self):
        return self.primeiro is None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.lista_vazia():
            print("A lista está vazia")
            return None
        
        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp

    def excluir_final(self):
        if self.lista_vazia():
            print("A lista está vazia")
            return None

        temp = self.ultimo
        if self.primeiro.proximo is None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp
        
    def excluir_qualquer(self, valor):
        if self.lista_vazia():
            print("A lista está vazia")
            return None

        atual = self.primeiro
        while atual.valor != valor:
            atual = atual.proximo
            if atual is None:
                return None
        
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo
            
        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def mostrar_inicio(self):
        if self.lista_vazia():
            print("A lista está vazia")
            return

        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_final(self):
        if self.lista_vazia():
            print("A lista está vazia")
            return
            
        atual = self.ultimo
        while atual is not None:
            atual.mostra_no()
            atual = atual.anterior


lista_nome = ListaDuplamenteEncadeada()
meu_nome = "joao"

for letra in meu_nome:
    lista_nome.insere_final(letra)

print("a/b. Nome 'joao' inserido e impresso:")
lista_nome.mostrar_inicio()

print("\nc/d. Lista apos exclusao do primeiro elemento:")
lista_nome.excluir_inicio()
lista_nome.mostrar_inicio()

print("\ne. Pesquisa pelo caractere 'o':")
ultimo_caractere = meu_nome[-1]
resultado_pesquisa = lista_nome.mostrar_final()
if resultado_pesquisa:
    print(f"Retorno: No encontrado com valor '{resultado_pesquisa.valor}'")
else:
    print("Retorno: Nulo (None)")

print("\nf/g. Lista apos exclusao do elemento 'a':")
elemento_excluir = 'a'
lista_nome.excluir_qualquer(elemento_excluir)
lista_nome.mostrar_inicio()