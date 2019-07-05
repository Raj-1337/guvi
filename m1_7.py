k = input()
x = list(map(int, input().split()))
r = []
for i in range(len(x)):
    if i % 2 == 0:
        if x[i] % 2 != 0:
            r.append(x[i])
    else:
        if x[i] % 2 == 0:
            r.append(x[i])
for i in r:
    print(i, end=" ")
