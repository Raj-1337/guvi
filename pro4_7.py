k = input()
x = list(map(int, input().split()))
r = 0
if len(x) == 1:
    print(1)
    exit(0)
elif len(x) == 2:
    if x[0] == x[1]:
        print(0)
        exit(0)
    else:
        print(2)
        exit(0)
else:
    x.insert(0, x[-1])
    x.append(x[1])
    for i in range(1, len(x)-1):
        if (x[i] > x[i-1] and x[i] > x[i+1]) or (x[i] < x[i-1] and x[i] < x[i+1]):
            r += 1
    print(r)
