k = input()
x = input().split()
p = input()
l = len(p)
c = 0
for i in x:
    if i[:l] == p:
        c += 1
print(c)
