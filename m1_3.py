k = input()
x = list(map(int, input().split()))
r = []
for i in range(len(x)):
	if i == x[i]:
		r.append(i)
if r:
	for i in sorted(r):
		print(i, end=" ")
else:
	print(-1)
