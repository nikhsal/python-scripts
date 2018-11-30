import operator
x = True
a=[]
while x:
    y=input("Enter name age and score<comma-separated>. Press n to stop ")
    y1=y.split(",")
    if y=='n':
        break
    else:
        a.append(y1)

a.sort(key=lambda r:r[0])
a.sort(key=operator.itemgetter(0,1,2))
print(a)

