total=0
quantidade=0
while True:
 peso=float(input())
 if ((total+peso)<=18):
  total=total+peso
  quantidade=quantidade+1
  continue
 else:
  print(quantidade)
  break