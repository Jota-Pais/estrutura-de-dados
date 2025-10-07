# 3  Faça uma função recursiva que receba um número inteiro positivo N e calcule o Fibonacci do número.

def fibonacci(N):
    if N == 1:
        return 1
    elif N == 0:
        return 0
    else:
        return fibonacci(N-1) + fibonacci(N-2)

print(fibonacci(10))

    