n = int(input())
x = list(map(int, input().split()))
c = []
for i in range(n):
    for j in range(i+1, n+1):
        c.append(sum(x[i:j]))
print(max(c))
