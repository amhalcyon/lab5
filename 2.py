import re

s = str(input())
x = re.search("a(bb|bbb)", s)

if x:
  print("YES! We have a match!")
else:
  print("No match")