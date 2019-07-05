n, k = list(map(int, input().split()))
r = []
res = []
for _ in range(n):
    r.append(set(map(int, input().split())))
for i in r[0]:
    for j in r[1:]:
        if i not in j:
            break
    else:
        res.append(str(i))
print(" ".join(res))
