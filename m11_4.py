k = [int(i) for i in input()]
t = 0
for i in range(len(k)+1):
    t += sum(k[:i])
print(t)
