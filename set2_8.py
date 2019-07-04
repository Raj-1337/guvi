
n = input()
l = len(n)
c = 0
for i in n:
  i = int(i)
  c += pow(i,l)
if c == int(n):
  print("yes")
else:
  print("no")
