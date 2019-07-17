from math import sqrt
c = 0
u, v = map(int, input().split())
for i in range(u, v+1):
    if len(str(i)) > 1:
        i = sum([int(k) for k in str(i)])
    if i == 1:
        continue
    for j in range(2, round(sqrt(i))+1):
        if i % j == 0:
            break
    else:
        c += 1
print(c)
