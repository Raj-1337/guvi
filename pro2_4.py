n, q = map(int, input().split())
x = list(map(int, input().split()))
r = []
for _ in range(q):
    u, v = map(int, input().split())
    t = x[u-1]
    for i in (x[u:v]):
        t = t ^ i
    r.append(t)
for i in r:
    print(i)
