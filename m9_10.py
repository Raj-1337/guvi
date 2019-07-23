x = [i for i in input()]
r = [0, 0]
i = 0
while i < len(x):
    t, j = 1, i + 1
    while j < len(x) and x[i] == x[j]:
        t += 1
        j += 1
    if t > r[1]:
        r = [x[i], t]
    i = j
print(r[0], r[1])
