x = input().split()
u = len(x[0])
v = len(x[1])
if u < v:
    x[0] += "".join([str(i) for i in range(1, (v-u)+1)])
elif v < u:
    x[1] += "".join([str(i) for i in range(1, (u-v)+1)])
t = ''
for i, j in zip(x[0], x[1]):
    t += (i+j)
print(t)
