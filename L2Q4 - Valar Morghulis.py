numerodemortos=int(input())
falecidos=[]
for i in range(numerodemortos):
  falecidos.append(input())
for i in range(len(falecidos)):
  falecido=falecidos[i].split()
  print(f'Cara familia {falecido[1]}, sentimos muito pela tragica morte de {falecido[0]}.')
  if falecido[1]=='Stark':
    print("O inverno chega para todos.")
  elif falecido[1]=='Lannister':
    print("Os campos agora o ouvirao rugir.")
  elif falecido[1]=='Targaryen':
    print("Voces sao superestimados mesmo.")