x = int(input())
c = 0
for i in range(0, x):
    if pow(2, i) > x:
        break
    c = x - pow(2, i)
print(c)
