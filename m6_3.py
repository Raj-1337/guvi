x = input().split()
n = int(x[-1])
for i in range(0, len(x[0])):
    if i + n > len(x[0]):
        break
    print(x[0][i:i+n], end=" ")
