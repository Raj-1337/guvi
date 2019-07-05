k = input()
x = [i for i in input().split()]
for i in x:
	if x.count(i) > 1:
		print(i)
		break
