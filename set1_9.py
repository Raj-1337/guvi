t = input()
x = [int(i) for i in input().split()]
k = int(t[-1])
print(sum(x[:k-1]))
