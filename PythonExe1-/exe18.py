import math

ang = int(input('Digite um angulo: '))
rad = math.radians(ang)

seno = math.sin(rad)
coss = math.cos(rad)
tang = math.tan(rad)

print(f'O seno é:{seno}\nO cosseno é:{coss}\nA tangente é:{tang}')
