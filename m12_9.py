n = int(input())
x = list(map(int, input().split()))
r = 0
for i in range(n-1):
    for j in range(i+1, n):
        if x[i] < x[j]: r += 1
print(r)
