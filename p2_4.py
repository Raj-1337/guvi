# your code goes here
k = input()
n = [i for i in input()]
v = 'aeiouAEIOU'
for i in n:
	if i in v:
		n.remove(i)
print(''.join(n[::-1]))
