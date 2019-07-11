t = input()
x = int(t)
if x % 8 == 0:
    print('yes')
    exit(0)
for j in range(1,len(t)):
    for i in range(0,len(t)):
        z = [k for k in t]
        del(z[i:j])
        if int(''.join(z)) % 8 == 0:
            print('yes')
            exit(0)
else:
    print('no')
