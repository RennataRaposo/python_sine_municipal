dicio={1:5.30, 2:6.0, 3:3.20, 4:2.50}
codigo=int(input())
quantidade=int(input())
valor_total=quantidade*dicio.get(codigo)
if quantidade>=15 or valor_total>=40:
  valor_total=valor_total-(valor_total*0.15)
print(f' R$ {valor_total:,.2f}')  