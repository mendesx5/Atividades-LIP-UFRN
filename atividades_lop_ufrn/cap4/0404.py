notas = list(map(float, input().split(',')))

alunos_aprovados = 0
alunos_reprovados = 0
soma_notas = 0

for nota in notas:
    soma_notas += nota
    if nota >= 5:
        alunos_aprovados += 1
    else:
        alunos_reprovados += 1

media = soma_notas / len(notas)

print(f"Número de Alunos Aprovados: {alunos_aprovados}")
print(f"Número de Alunos Reprovados: {alunos_reprovados}")
print(f"Média da Turma: {media:.2f}")