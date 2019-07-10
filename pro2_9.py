from itertools import chain
k = int(input())
r = []
for _ in range(k):
    t = list(map(int, input().split()))
    r.append(t)
for i in sorted(chain.from_iterable(r)):
    print(i, end=" ")
