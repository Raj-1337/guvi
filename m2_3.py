x = [i for i in input()]
y = x[::-1]
while len(x) > 1:
    if x.pop(0) != x.pop():
        print('NO')
        break
else:
    print('yes')
