n = int(input())
x = []
for _ in range(n):
    x.append(input())
r, c, flag = '', 0, False
for i in x[0]:
    for j in x[1:]:
        if len(j) == c:
            flag = True
            break
        if j[c] != i:
            break
    else:
        r += i
    if flag:
        break
    c += 1
print(r)
