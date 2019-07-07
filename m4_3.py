from itertools import permutations
x = input()
X = int(x)
r = []
y = [int(i) for i in x]
for i in permutations(y, len(y)):
    t = int(''.join([str(j) for j in i]))
    if t > X:
        r.append(t)
if not r:
    print('impossible')
else:
    print(min(r))
