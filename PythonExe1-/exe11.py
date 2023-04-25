p = float(input('Qual é o preço do produto R$:'))
por = float(input('De quantos % é o desconto:' ))

#d = p * 0.05 
#vf = p - d
print(f'Voce ganhou {por}% de desconto, o desconto é de {p*por/100:.2f}', end=)
print(f'O produto fica R${p - p*por/100:.2f} ')