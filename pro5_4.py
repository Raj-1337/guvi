n, p, q, r = map(int, input().split())
x = list(map(int, input().split()))
z = []
i = 0
for i in range(0, len(x)):
    for j in range(i, len(x)):
        for k in range(j, len(x)):
            z.append(sum((p*x[i], q*x[j], r*x[k])))
print(max(z))
