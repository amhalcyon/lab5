import re

s = str(input())
x = re.search("[a-z]+_[a-z]+", s)

if x:
  print("YES! We have a match!")
else:
  print("No match")