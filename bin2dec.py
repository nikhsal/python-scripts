x = input("Enter Binary Numbers : ")
y = x.split(",")
z=[]
for i in y:
    if int(i,2)%5 == 0:
        z.append(i)

print(z)
