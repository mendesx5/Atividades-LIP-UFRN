palavras = list(map(str, input().split()))

for palavra in palavras:
    if palavra == palavra[::-1]:
        print("Sim", end=' ')
    else:
        print("Não", end=' ')