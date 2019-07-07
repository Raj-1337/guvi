k = input()
a = list(map(int, input().split()))
b = a[:]
while len(a) > 1:
    z = []
    for i in filter((lambda b: a.index(b) % 2 != 0), a):
        z.append(i)
    a = z[:]
print(b.index(a[0]))
