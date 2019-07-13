x1 = input().split('#')
x2 = input().split('#')
d = {}
d[x1[0]] = sum([int(i) for i in x1[1:]])
d[x2[0]] = sum([int(i) for i in x2[1:]])
print(max(d, key=(lambda a: d[a])))
