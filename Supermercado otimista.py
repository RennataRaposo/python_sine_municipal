dia=input()
preco=float(input())
opcao=input()
nome=input()
if (dia=='seg' or dia=='ter' or dia=='qua') and opcao=='ouro':
 print(f'O preco do produto {nome} no dia {dia} eh {preco/2:,.2f}')
elif (dia=='qui' or dia=='sex') and (10 < preco < 100):
 print(f'O preco do produto {nome} no dia {dia} eh {preco/3:,.2f}')
elif dia=='sab' and opcao=='prata':
 print(f'O preco do produto {nome} no dia {dia} eh {3*preco:,.2f}')
else:
 print(f'O preco do produto {nome} no dia {dia} eh {2*preco:,.2f}')