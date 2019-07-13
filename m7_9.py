import re
c = input()
if re.search("[a-zA-Z0-9]{3,}[&]?@gmail\.com", c):
    print("YES")
else:
    print("NO")
