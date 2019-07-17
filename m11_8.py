x = [int(i) for i in input()]
x.append(x[0])
c = 0
for i in range(len(x)-1):
    c += pow(x[i], x[i+1])
print(c)
