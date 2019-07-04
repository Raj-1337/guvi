
n = list(map(int, input().split()))
r = []
for i in range(n[0], n[-1]):
  t = str(i)
  l = len(t)
  c = 0
  for j in t:
    j = int(j)
    c += pow(j, l)
  if c == i:
    r.append(i)
for i in r:
  print(i, end= " ")
