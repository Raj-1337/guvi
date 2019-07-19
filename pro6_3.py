x = [i.lower() for i in input() if i != " "]
print('yes') if len(set(x)) == 26 else print('no')
