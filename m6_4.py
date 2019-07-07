k = input()
x = list(map(int, input().split()))
for i in range(1, len(x)+1):
    print(min(x[:i]), end=" ")
