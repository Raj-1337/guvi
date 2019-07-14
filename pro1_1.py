n = int(input())
x = []
for _ in range(n):
    x.append(input())
r = ''
c = 0
for i in x[0]:
    for j in x[1:]:
        if j[c] != i:
            break
    else:
        r += i
    c += 1
print(r)
