from itertools import chain, combinations
u = input()
v = list(map(int, input().split()))
def multi(l):
    z = 1
    for i in l:
        z *= i
    return z
m = 0
for c in chain.from_iterable(combinations(v, z) for z in range(len(v)+1)):
    t = multi(c)
    if t > m:
        m = t
print(m)
