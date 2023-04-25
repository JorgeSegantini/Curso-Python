nome = str(input('Digite seu nome: ')).strip()

lma = nome.upper()
lmi = nome.lower()
car = nome.split()

print(f'Nome em letra maiúscula {lma}')
print(f'Nome em letra minúscula {lmi}')
print(f'Quantas letras tem {len(nome) - nome.count(" ")}')
print(f'Seu primeiro nome tem {nome.find(" ")}')
print(len(car[0]))