n, m = map(int, input().split())
r = []
for i in range(n):
    t = []
    x = input().split()
    for j in x:
        t.append((j, True))
    r.append(t)
for i in range(n):
    for j in range(m):
        if r[i][j] == ('0', True):
            t = []
            for k in range(m):
                t.append(('0', False))
            r[i] = t
            for k in r:
                k[j] = ('0', False)
for i in r:
    t = []
    for j in i:
        t.append(j[0])
    print(" ".join(t))

