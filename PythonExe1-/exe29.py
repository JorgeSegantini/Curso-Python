vel = float(input('Digite a velocidade do carro: '))
mul = (vel - 80) * 7
print('Boa viagem' if vel<80 else f'A velocidade era de {vel:.0f}kmh e voce foi multado em R${mul:.2f}')