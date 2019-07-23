n = int(input())
c = 0
for i in map(str, range(n+1)):
    if '2' in i: c += i.count('2')
print(c)
