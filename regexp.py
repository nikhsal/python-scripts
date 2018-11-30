import re
x=input("Text")
list=[i for i in x if i.isdigit()]
print(list)
y=re.findall("([0-9]*)",x)
print(y)
