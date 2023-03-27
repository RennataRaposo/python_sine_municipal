pi=3.14
raio1=float(input())
raio2=float(input())
circulo1= (pi*(raio1**2))
circulo2= (pi*(raio2**2))
if circulo1>circulo2:
 print('Primeiro circulo')
elif circulo1<circulo2:
 print('Segundo circulo')
else:
 print('Iguais')