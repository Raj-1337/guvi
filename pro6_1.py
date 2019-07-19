n = int(input())
x = list(map(int, input().split()))
r = []
for i in range(n):
    if x[i] > 0:
        t = True
    else:
        t = False
    c = 1
    for j in range(i+1, n):
        if t:
            if x[j] < 0:
                c += 1
                t = False
            else:
                r.append(c)
                break
        else:
            if x[j] > 0:
                c += 1
                t = True
            else:
                r.append(c)
                break
    else:
        r.append(c)
print(*r)
