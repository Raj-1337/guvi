k = input()
x = list(map(int, input().split()))
print((x.index(min(x))+1), (x.index(max(x))+1))
