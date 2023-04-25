from random import randint
from time import sleep
n = randint(1,5) #o computador vai gerar um número de 1 a 5
print('+-' * 40)
ten = int(input('Tente acertar o número de 1 até 5: '))
print('+-' * 40)
print('Processando')
sleep(3)
if n == ten:
    print('Voce acertou o número')
else:
    print('Voce errou o número')
print(f'O número correto é: {n}')
print('+-' * 40)