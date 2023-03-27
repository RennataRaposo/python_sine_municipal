N=7
votos_cinema=0
votos_boliche=0
for i in range(N):
 passeio=input().upper()
 if passeio=="CINEMA":
  votos_cinema+=1
 else:
  votos_boliche+=1
if votos_cinema > votos_boliche:
 print('CINEMA')
else:
 print('BOLICHE')