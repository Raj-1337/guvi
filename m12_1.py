n = int(input())
r = []
for i in range(n):
    r.append(list(map(int, input().split())))
c = 0
for i in range(n):
    c += r[i][i]
print(c)
