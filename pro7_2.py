x = input()
r = ""
for i in range(len(x)):
    for j in range(len(x), i-1, -1):
        t = x[i:j]
        if len(t) <= 1:
            continue
        elif t == t[::-1]:
            print(len(x)-len(t))
            exit(0)
else:
    print(len(x))
