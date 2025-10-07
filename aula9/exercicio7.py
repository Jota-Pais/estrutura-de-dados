# 7 - Faça uma função recursiva que receba um número inteiro positivo par N e
# imprima todos os números pares de 0 até N em ordem crescente.

def imprimePares(N):
    if N == 0:
        print(0)
    else:
        print(N)
        imprimePares(N-2)

imprimePares(10)