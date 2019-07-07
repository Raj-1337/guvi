from itertools import chain, combinations
k = input()
x = list(map(int, input().split()))
def multi(t):
    z = 1
    for i in t:
        z *= i
    return z
p = 0
for i in chain.from_iterable(combinations(x, n) for n in range(len(x)+1)):
    t = multi(i)
    if t > p:
        p = t
print(p)
