
k = int(input())
x = list(map(int, input().split()))
n = int(len(x)/2)
if sum(x[:n])//len(x[:n]) == sum(x[n:])//len(x[n:]):
    print('yes')
else:
    print('no')
