idades = list(map(int, input().split()))

for idade in idades:
    
    if 13 <= idade <= 17:
        print("Adolescente")
    elif 18 <= idade <= 59:
        print("Maior de idade")
    elif 60 <= idade:
        print("Idoso")
    else:
        print("Menor de idade")