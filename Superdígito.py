superdigito= input()
sd=superdigito.split()
n = sd[0]
k = int(sd[1])
z = ""
for x in range (1, k+1):
  z = n+z
print(z)