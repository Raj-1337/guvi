x = input()
t = '123456789.0'
for i in x:
    if i not in t:
        print('no')
        break
else:
    print('yes')
