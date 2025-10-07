# 4 - Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.

def fatorial(N):
    if N == 1:
        return 1
    else:
        return N * fatorial(N-1)

print(fatorial(5))