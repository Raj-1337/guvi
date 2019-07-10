n, q = map(int, input().split())
x = list(map(int, input().split()))
r = []
for _ in range(q):
    u, v = map(int, input().split())
    r.append(min(x[u-1:v]))
for i in r:
    print(i)
