x = [i for i in input()]
for i in range(len(x)):
    if i == 0:
        z = x[i+1:]
        if z == list(reversed(z)):
            print('YES')
            break
    elif i == len(x)-1:
        z = x[:i]
        if z == list(reversed(z)):
            print('YES')
            break
    else:
        z = x[:i] + x[i+1:]
        if z == list(reversed(z)):
            print('YES')
            break
else:
    print('NO')
