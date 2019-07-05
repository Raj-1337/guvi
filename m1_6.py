k = input()
x = [i for i in input().split()]
flag = True
for i in x:
	if x.count(i) > 1:
		print(i)
		flag = False
		break
if flag:
	print('unique')
