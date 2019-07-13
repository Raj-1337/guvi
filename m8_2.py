x = input().split()
for i in range(1, len(x)+1):
    if i % 2 != 0:
        x[i-1] = x[i-1][::-1]
print(" ".join(x))
