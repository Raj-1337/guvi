x = input()
m = 0
for i in range(len(x)-1):
    for j in range(i+1, len(x)):
        t = x[i:j]
        if t == t[::-1] and len(t) > m: m = len(t)
print(m)
