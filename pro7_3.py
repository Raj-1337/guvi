x = input()
r = ""
for i in range(len(x)):
    for j in range(len(x), i-1, -1):
        t = x[i:j]
        if len(t) <= 1:
            continue
        for k in t:
            if t.count(k) > 1: break
        else:
            if len(t) > len(r): r = t
print(len(r)) if r else print(0)
