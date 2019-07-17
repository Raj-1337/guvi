n = int(input())
r = []
for i in range(n):
    r.append(list(map(int, input().split())))
c = 0
for i in range(n-1, 0, -1):
    c += r[i][i-1]
    if i == 1:
        break
print(c)
