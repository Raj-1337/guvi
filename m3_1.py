a, b = map(int, input().split())
r = []
for i in range(a):
    z = []
    y = input().split()
    for s in y:
        z.append((s, True))
    r.append(z)
for i in range(a):
    for j in range(b):
        if r[i][j] == ('0', True):
            x = []
            for k in range(b):
                x.append(('0', False))
            r[i] = x
            for k in r:
                k[j] = ('0', False)
for l in r:
    x = []
    for y in l:
        x.append(y[0])
    print(" ".join(x))

