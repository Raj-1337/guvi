x = input()
if x == x[::-1]:
    print('yes')
    exit(0)
else:
    c = 0
    for i in x[::-1]:
        if i != '0':
            break
        else:
            c += 1
    t = (c*'0'+x)
    if t == t[::-1]:
        print('yes')
    else:
        print('no')
