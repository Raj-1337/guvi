n = int(input())
x = list(map(int, input().split()))
for i in range(len(x)):
    if i == 0:
        if x[i+1] < x[i]:
            print(x[i+1], end=" ")
        else:
            print(-1, end=" ")
    elif i == n - 1:
        if x[i-1] < x[i]:
            print(x[i - 1], end=" ")
        else:
            print(-1, end="")
    else:
        if x[i+1] < x[i]:
            print(x[i+1], end=" ")
        elif x[i-1] < x[i]:
            print(x[i - 1], end=" ")
        else:
            print(-1, end=" ")
