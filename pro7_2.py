x = input()
r = ""
for i in range(len(x)):
    for j in range(len(x), i-1, -1):
        t = x[i:j]
        if len(t) <= 1:
            continue
        elif t == t[::-1]:
            if len(t) > len(r):
                r = t
print(len(x) - len(r)) if r else print(len(x))
