# 2  Faça uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N.

def somatorio(N):
    if N == 1:
        return 1
    else:
        return N + somatorio(N-1)

print(somatorio(10))
