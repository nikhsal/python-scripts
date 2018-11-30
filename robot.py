import math
x = True
a=[]
t=0
while x:
    y=input("Enter UP DOWN LEFT RIGHT with value. To stop press n ")
    y1 = y.split()
    if y=='n':
        break
    else:
        a.append(y1)
        t+=1
xcor=0
ycor=0
for i in a:
    if i[0]=='UP':
        ycor += int(i[1])
    elif i[0]=='DOWN':
        ycor -= int(i[1])
    elif i[0]=='LEFT':
        xcor+=int(i[1])
    elif i[0]=='RIGHT':
        xcor-=int(i[1])
dist=math.sqrt(xcor**2 + ycor**2)
print("Distance: ",int(dist))
