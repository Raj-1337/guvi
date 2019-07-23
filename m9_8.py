n, k = map(int, input().split())
x = input().split()
c = 0
for i in range(0, n, k):
    if "*" in x[:i]:
        c += 1
print(c)
