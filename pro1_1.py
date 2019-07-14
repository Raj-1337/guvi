n = int(input())
x = []
for _ in range(n):
    x.append(input())
r = []
for i in range(len(x)):
    for j in range(i+1, len(x)):
        t = ''
        c = 0
        while x[i][c] == x[j][c]:
            t += x[i][c]
            c += 1
            if len(x[i]) == c or len(x[j]) == c:
                break
        if t:
            r.append(t)
print(max(r, key=(lambda a: len(a))))
