n = list(map(int, input().split()))
for i in range(max(n), (n[0]*n[1])+1):
	if i % n[0] == 0 and i % n[1] == 0:
		print(i)
		break
