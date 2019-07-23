x, y = map(int, input().split())
for i in range(2, x):
    if x % i == 0:
        print('no')
        break
else:
    for i in range(2, y):
        if y % i == 0:
            print('no')
            break
    else:
        print('yes')
