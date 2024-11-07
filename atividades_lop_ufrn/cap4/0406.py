import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while tentativas < 20:
    tentativas += 1
    palpite = (int(input()))
    if palpite == numero_secreto:
        print(f"Parabéns! Você adivinho o número em {tentativas} tenteativas.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor")

print(f"O número secreto era {numero_secreto}")
print("Fim de jogo")