k = int(input())
x = list(map(int, input().split()))
r = []
for i in range(k):
    mul = 1
    for j in range(k):
        if j == i:
            continue
        else:
            mul *= x[j]
    r.append(str(mul))
print(" ".join(r))
