from math import gcd
n, q = map(int, input().split())
x = list(map(int, input().split()))
r = []
for _ in range(q):
    u, v = map(int, input().split())
    r.append(x[u-1]) if u == v else r.append(gcd(x[u-1], x[v-1]))
for i in r:
    print(i)
