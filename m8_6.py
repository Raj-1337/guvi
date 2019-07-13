from itertools import chain
from statistics import mean
n = int(input())
r = []
for _ in range(n):
    r.append(list(map(int, input().split())))
print(format((mean(chain.from_iterable(r))), '.6f'))
