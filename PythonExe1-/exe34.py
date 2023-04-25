sal = float(input('Qual é seu dalario? '))
if sal > 1250:
    print(f'Voce recebeu um aumento de 10% agora seu sálario é {sal*0.10 + sal}')
else:
    print(f'Voce recebeu um aumento de 15%, agora seu sálario é {sal*0.15 + sal}')