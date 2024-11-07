def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

numeros = list(map(int, input().split(',')))
resultados = []
contador_invalido = 0

for numero in numeros:
    if numero < 0 or numero >= 15:
        resultados.append("X")
        contador_invalido += 1
    else:
        resultados.append(calcular_fatorial(numero))

print(" ".join(map(str, resultados)))
print("Quantidade de números inválidos:", contador_invalido)