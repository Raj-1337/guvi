
n = input()
if n not in "abcdefghijklmnopqrstuvwxyz":
  print("Invalid")
elif n in "aeiou":
  print("Vowel")
else:
  print("Consonant")
