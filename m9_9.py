z = input()
x = []
for i in z:
    if i not in x: x.append(i)
print(''.join(x[::-1]))
