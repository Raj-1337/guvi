n = input()
x = list(map(int, input().split()))
c = 0
r = []
for i in range(len(x)):
    for j in range(i, len(x)):
        for k in range(j, len(x)):
            if x[i] < x[j] < x[k] and [x[i], x[j], x[k]] not in r:
                r.append([x[i], x[j], x[k]])
                c += 1
print(c)
