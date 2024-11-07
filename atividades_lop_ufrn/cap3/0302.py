numero = int(input())
resto = numero % 5


if 100 < numero < 1000:
    print(f"O resto da divisão de {numero} por 5 é {resto}.")
else:
    print("Por favor, insira um número inteiro positivo entre 100 e 1000.")