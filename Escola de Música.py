def ClassificaAluno(media, faltas):
 if media >=9.5 and faltas<=10:
  print("Aprovado com louvor".upper())
 elif media >=7  and faltas<=10:
  print("Aprovado".upper())
 elif media <7 and faltas<=10:
  print("Reprovado".upper())
 else:
  print("reprovado por faltas".upper())
media=float(input())
faltas=int(input())
ClassificaAluno(media, faltas)