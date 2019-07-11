k = input()
x = list(map(int, input().split()))
x.sort()
c = 0
for i in range(len(x)):
    if sum(x[:i]) <= x[i]:
        c += 1
print(c)
