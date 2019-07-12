k = input()
x = list(map(int, input().split()))
r = 0
x.insert(0, x[-1])
x.append(x[1])
if len(x) < 3:
    print(0)
else:
    for i in range(1, len(x)-1):
        if (x[i] > x[i-1] and x[i] > x[i+1]) or (x[i] < x[i-1] and x[i] < x[i+1]):
            r += 1
    print(r)
