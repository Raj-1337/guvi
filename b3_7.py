x = input()
t = '123456789.0'
for i in x:
    if i not in t:
        print('No')
        break
else:
    print('yes')
