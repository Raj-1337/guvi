n, k = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
c = 0
#t = 0
while True:
    f = True
    for i in range(n):
        if x[i] > y[i] and (k == 0 or k < (x[i] - y[i])):
            f = False
            break
        else:
            if y[i] < x[i]:
                k -= (x[i] - y[i])
                y[i] = 0
            else:
                y[i] -= x[i]
    if not f:
        break
    c += 1
print(c)
