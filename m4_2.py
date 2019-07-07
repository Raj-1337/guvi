k = input()
u = list(map(int, input().split()))
v = u[:]
while len(u) > 1:
    z = []
    for i in filter((lambda b: u.index(b) % 2 != 0), u):
        z.append(i)
    u = z[:]
print(v.index(u[0]))
