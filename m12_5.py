from itertools import combinations_with_replacement
n = int(input())
r = [2]
z = 0
for j in range(3, n+1):
    for i in range(2, j+1):
        if i == j:
            r.append(i)
            continue
        if j % i == 0:
            break
for i in combinations_with_replacement(r, 2):
    if sum(i) == n:
        z += 1
print(z)
