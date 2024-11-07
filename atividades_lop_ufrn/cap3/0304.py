n = int(input())
b = bin(n)[2:]
lista = []

if 10 <= n <= 20:
    lista.extend(b)
    print(lista)
else:
    print("O número inserido não está dentro do intervalo permitido.")