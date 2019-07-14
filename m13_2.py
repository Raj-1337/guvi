n = input()
x = list(map(int, input().split()))
for i in range(len(x)):
    if sum(x[:i]) == sum(x[i+1:]):
        print('yes')
        break
else:
    print('no')
