unidade=input()
temperatura=float(input())
if unidade=="C":
 if temperatura >= -273.15:
   print (str(format(((temperatura * 9/5) + 32),'.2f')) +' F')
   print (str(format((temperatura + 273.15),'.2f'))+ ' K')
 else:
  print('Valor de temperatura abaixo do minimo')
elif unidade=="F":
 if temperatura >= -459.67:
   print (str(format(((temperatura -32) * 5/9),'.2f'))+ ' C')
   print (str(format(((temperatura - 32) * 5/9 + 273.15),'.2f'))+' K')
 else:
  print('Valor de temperatura abaixo do minimo')

elif unidade=="K":
 if temperatura >= 0.0:
   print (str(format((temperatura - 273.15),'.2f'))+ ' C')
   print (str(format(((temperatura - 273.15 )* 9/5 + 32),'.2f'))+' F')
 else:
  print('Valor de temperatura abaixo do minimo')
else:
    print('Unidade Incorreta')