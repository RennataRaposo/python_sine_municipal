posicao=int(input())
def fibonacci (f):
  if f ==1:
    return 0
  elif f==2:
    return 1
  else:
    return fibonacci (f-1) + fibonacci (f-2)
print(fibonacci(posicao))