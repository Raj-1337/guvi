p, q = map(int, input().split())
r = []
for i in range(p):
    z = []
    y = input().split()
    for s in y:
        z.append((s, True))
    r.append(z)
for i in range(p):
    for j in range(q):
        if r[i][j] == ('0', True):
            z = []
            for k in range(m):
                z.append(('0', False))
            r[i] = z
            for a in r:
                k[a] = ('0', False)
for i in r:
    t = []
    for j in i:
        t.append(j[0])
    print(" ".join(t))

