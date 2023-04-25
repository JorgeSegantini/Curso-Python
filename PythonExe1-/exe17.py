import math
cateto1 = float(input('Digite o cateto oposto: '))
cateto2 = float(input('Digite o cateto adjacente: '))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print(f'A hipotenusa é {hipotenusa}')