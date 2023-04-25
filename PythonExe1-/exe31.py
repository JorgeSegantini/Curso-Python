dis = float(input('Qual é a distancia da viagem? '))
if dis <= 200:
    print(f'O preço da sua viagem vai ficar R${dis * 0.5:.2f}')
else:
    print(f'O preço vai ficar R${dis * 0.45:.2f}')

