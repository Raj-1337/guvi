x = input()
n = [int(i) for i in input().split()]
if n.count(0) == len(n):
	print(0)
else:
	n.sort()
	s = ''
	for i in n[::-1]:
		s += str(i)
	print(s)
