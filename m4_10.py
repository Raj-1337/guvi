x = input()
y = 0
for i in x:
    y += int(i)
if str(y) == str(y)[::-1]:
    print('YES')
else:
    print('NO')
