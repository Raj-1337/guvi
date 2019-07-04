
n = list(map(int, input().split()))
x = []
for i in range(n[0], n[1]):
  flag = True
  for j in range(2, i):
    if i % j == 0:
      flag = False
      break
  if flag and i != 1:
    x.append(str(i))
print(' '.join(x))
