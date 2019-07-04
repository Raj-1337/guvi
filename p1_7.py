n = input()
o = n[::2]
e = n[1::2]
s = ''
for i,j in zip(o,e):
    s += (j + i)
print(s)
