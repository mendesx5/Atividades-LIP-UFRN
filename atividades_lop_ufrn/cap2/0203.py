string1 = input("")
string2 = input("")

def comparar_booleanos(string1, string2):
    if string1.lower() == string2.lower():
        print("São iguais")
    else:
        print("São diferentes")

comparar_booleanos(string1, string2)