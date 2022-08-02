def fibonacci(valor=10):
    resultado = [0, 1]
    while resultado[-1] < valor:
        resultado.append(resultado[-1]+resultado[-2])
    if valor in resultado:
        print(f'O valor {valor}, pertence ao Fibonacci.')
    else:
        print(f'O valor {valor}, não pertence ao Fibonacci.')
    return resultado


for fib in fibonacci(1000):
    print(fib, end=' ')