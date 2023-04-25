n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
# verifianco quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n1
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor némero é {menor}')
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior número é {maior}')


# 3 numeros e mostre qual é o maior e o menor
