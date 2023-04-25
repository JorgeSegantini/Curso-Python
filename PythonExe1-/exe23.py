
num = int(input('Digite um numero de 0 a 9999: '))
#n = str(num)
#print(f'Unídade {n[3]}\n dezena {n[2]}\n centena {n[1]}\n milhar {n[0]}')

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')