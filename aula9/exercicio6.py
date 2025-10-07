# 6 - Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente. 

def contagemRegressiva(N):
    if N == 0:
        print(0)
    else:
        print(N)
        contagemRegressiva(N-1)
contagemRegressiva(7)