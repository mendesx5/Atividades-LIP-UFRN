import math

ca, co = map(int, input().split())

hipotenusa = math.sqrt(ca**2 + co**2)

print(f"{hipotenusa:.2f} metros")