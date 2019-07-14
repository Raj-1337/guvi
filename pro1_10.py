n = input()
x = list(map(int, input().split()))
c = 0
for i in range(1, len(x)):
    if x[i] == x[i-1]:
        continue
    else:
        for j in x[:i]:
            if j < x[i]:
                c += j
print(c)
