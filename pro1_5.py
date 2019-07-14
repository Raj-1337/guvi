from itertools import combinations_with_replacement, count
n, a, b = map(int, input().split())
h = n / 2
f = False
t = []
for i in count(2):
    for j in combinations_with_replacement([a, b], i):
        if sum(j) == h:
            t.append(j)
            f = True
            break
        if sum(j) > h:
            f = True
            break
    if f:
        break
print('YES') if t else print('NO')
