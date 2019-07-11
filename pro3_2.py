k = input()
x = list(map(int, input().split()))
print(max([sum(x[0::2]), sum(x[1::2])]))
