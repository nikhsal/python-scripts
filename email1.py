import re
x=input("Email ID: ")
y=re.findall("^\w+",x)
print(y)
