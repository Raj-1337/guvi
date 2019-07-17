x = int(input())
for i in range(x):
    t = pow(2, i)
    if t == x:
        print('YES')
        exit(0)
    elif t > x:
        break
print('NO')
