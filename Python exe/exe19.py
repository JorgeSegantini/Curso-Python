import random
al1 = input('Digite o nome do primeito aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

nomes = [al1, al2, al3, al4]

esc = random.choice(nomes)
print(f'O aluno sorteado foi {esc} parabéns!')
#

