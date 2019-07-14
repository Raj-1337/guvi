n = int(input())
x = list(map(int, input().split()))
f = True
r = []
for _ in range(n):
    if f:
        t = max(x)
        r.append(t)
        x.remove(t)
        f = False
    else:
        t = min(x)
        r.append(t)
        x.remove(t)
        f = True
for i in r:
    print(i, end=" ")
