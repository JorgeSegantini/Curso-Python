a = float(input('Quantos Km voce andou com o carro? '))
d = float(input('Por quantos dias voce ficou com o carro? '))
v1 = d * 60
v2 = a * 0.15
s = (v1 + v2)
vf = s / a
print(
    f'O valor percorrido foi {a} a quantidade de dias foi {d} o valor final a pagar foi R${s} Voce gastou {vf} por Km rodado.')
