# faça uma função recursiva para somar os elementos de uma lista

def somaElementos(a):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + somaElementos(a[1:])

print(somaElementos([1, 2, 3, 4, 5]))

# Faça uma função recursiva que calcula o elemento máximo em um vetor.

def maxElemento(a):
    if len(a) == 1:
        return a[0]
    else:
        return max(a[0], maxElemento(a[1:]))

print(maxElemento([1, 2, 3, 4, 5]))


# Faça uma função recursiva que calcula o elemento mínimo em um vetor.

def minElemento(a):
    if len(a) == 1:
        return a[0]
    else:
        return min(a[0], minElemento(a[1:]))

print(minElemento([1, 2, 3, 4, 5]))

# Faça uma função recursiva que calcula a média dos elementos de um vetor

def mediaElementos(a):
    if len(a) == 1:
        return a[0]    
    else:
        return (a[0] + mediaElementos(a[1:])) / len(a) 

print(mediaElementos([1, 2, 3, 4, 5])) # deu ruim, o /len(a) ta rodando multiplas vezes, tem que colocar a divisão no fim da operação só