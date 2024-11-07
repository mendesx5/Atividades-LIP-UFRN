peso = float(input(""))
altura = float(input(""))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f"Seu IMC é {IMC:.2f} (Abaixo do peso).")
elif 18.5 < IMC < 24.9:
    print(f"Seu IMC é {IMC:.2f} (Saudável).")
elif 15.0 < IMC < 29.9:
    print(f"Seu IMC é {IMC:.2f} (Sobrepeso).")
elif 30.0 < IMC < 34.9:
    print(f"Seu IMC é {IMC:.2f} (Obesidade grau I).")
elif 35.0 < IMC < 39.9:
    print(f"Seu IMC é {IMC:.2f} (Obesidade grau II).")
else:
    print(f"Seu IMC é {IMC:.2f} (Obesidade grau III).")