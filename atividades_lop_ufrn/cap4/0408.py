numeros = list(map(int, input().split(',')))

def e_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(lista_numeros):
    primos = [numero for numero in lista_numeros if e_primo(numero)]
    return primos

primos = encontrar_primos(numeros)

print(', '.join(map(str, primos)))