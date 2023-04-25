from datetime import date
ano = int(input('QUal ano voce deseja analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto ')
else:
    print(f'O ano {ano} nao é bissexto')

#leia um ano e mostre se é bissexto

