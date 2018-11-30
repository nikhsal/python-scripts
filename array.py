from array import *

x = input("enter dimension:")
list = x.split(",")
name = []
row = int(list[0])
col = int(list[1])
print(name)
print("hello")
for i in range(row):
    column=[]
    for j in range(col):
        column.append(i*j)
    name.append(column)

print(name)


