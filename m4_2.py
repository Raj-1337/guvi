k = input()
x = list(map(int, input().split()))
y = x[:]
while len(a) > 1:
    z = []
    for i in filter((lambda b: x.index(b) % 2 != 0), x):
        z.append(i)
    x = z[:]
print(y.index(x[0]))
