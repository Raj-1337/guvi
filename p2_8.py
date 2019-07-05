from collections import Counter
n = int(input())
r = 0
t = Counter('kabali')
for _ in range(n):
	if Counter(input()) == t:
		r += 1
print(r)
