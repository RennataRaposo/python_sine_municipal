N=7
Total=float(0)
for a in range(N):
 qnt_caixa=int(input())
 tam_caixa=input().lower()
 if (tam_caixa=='p'):
  Total+=qnt_caixa*10
 else:
   Total+=qnt_caixa*16
print(int(Total))
print(int((Total*2)/N))