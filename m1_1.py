from collections import Counter
n = input()
x = [i for i in input().split()]
t = Counter(x)
r = []
for i, j in t.items():
	if j > 1:
		r.append(i)
r.sort()
print(' '.join(r))
