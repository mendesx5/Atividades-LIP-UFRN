conjunto_a = set()
conjunto_b = set()

for i in range(3):
    numero = int(input(""))
    conjunto_a.add(numero)

for i in range(3):
    numero = int(input(""))
    conjunto_b.add(numero)

uniao = conjunto_a | conjunto_b
intersecao = conjunto_a & conjunto_b
diferenca = conjunto_a - conjunto_b

print("União:", uniao)
print("Interseção:", intersecao)
print("Diferença:", diferenca)