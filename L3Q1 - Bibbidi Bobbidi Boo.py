qntmocaSapato=input().split()
numeroDasCasas=input().split()
sapatos=input().split()
achou=False
sapatoCristal=qntmocaSapato[-1]
for i in range(len(sapatos)):
 if sapatos[i]==sapatoCristal:
  print('Cinderela mora na casa '+ numeroDasCasas[i]+'!')
  achou=True
if achou==False:
 print('Nenhuma das jovens e a moca do baile.')