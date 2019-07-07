from itertools import chain, combinations
a = input()
b = list(map(int, input().split()))
def multi(y):
    z = 1
    for j in y:
        z *= j
    return z
q = 0
for c in chain.from_iterable(combinations(b, m) for m in range(len(b)+1)):
    u = multi(c)
    if u > q:
        q = u
print(q)
