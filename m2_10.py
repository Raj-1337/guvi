i, j = list(map(int, input().split()))
c = 0
for l in range(i, j+1):
    t = (bin(l)[2:]).count('1')
    if t == 1:
        continue
    for i in range(2, t):
        if t % i == 0:
            flag = False
            break
    else:
        c += 1
print(c)
