def imprimir_triangulo(tipo, linhas):
    if tipo == 'tipo1':
        for i in range(1, linhas + 1):
            print('*' * i)
    elif tipo == 'tipo2':
        for i in range(linhas, 0, -1):
            print('*' * i)

tipo, linhas = input().split(', ')
linhas = int(linhas)

imprimir_triangulo(tipo, linhas)