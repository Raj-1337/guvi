n = int(input())
r = [2]
for i in range(3, n):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        r.append(i)
print(*r)
