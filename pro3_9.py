x = int(input())
t = int(x/2)
r = []
for i in range(x, t, -1):
    print(i)
    j = str(i)
    if i + sum([int(k) for k in j]) == x:
        print(1)
        print(i)