id = int(input())

if 1 <= id <= 5:
    print(f"Ilha {id} é exclusiva da Espécie 1.\nPortanto, não é compartilhada com outras espécies.")
elif 11 <= id <= 17:
    print(f"Ilha {id} é exclusiva da Espécie 2.\nPortanto, não é compartilhada com outras espécies.")
elif 6 <= id <= 10:
    print(f"Ilha {id} é compartilhada entre espécie(s):1 2.")