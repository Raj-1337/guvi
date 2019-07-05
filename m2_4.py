from itertools import permutations
x = input()
for i in permutations(x, len(x)):
    print(''.join(list(i)))
