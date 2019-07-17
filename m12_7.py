x = input()
r = [pow(int(i), j) for i, j in zip(x, range(len(x)))]
print(sum(r))
