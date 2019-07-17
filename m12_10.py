n = int(input())
x = list(map(int, input().split()))
r = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if x[i] + x[j] == x[k]: r += 1
print(r)
