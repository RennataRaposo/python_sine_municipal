forma=input().upper()
if forma=='Q':
 lado=float(input())
 print(format((lado**2),'.2f'))
 print(format((lado*4),'.2f'))
elif forma=='R':
 altura=float(input())
 base=float(input())
 print(format((base*altura),'.2f'))
 print(format(2*(altura*base),'.2f'))
elif forma=='C':
 pi=3.14
 raio=float(input())
 print(format(pi*(raio**2),'.2f'))
 print(format(2*(pi*raio),'.2f'))
else:
 print('Nenhuma figura selecionada')