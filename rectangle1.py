class Rectangle:
    l=0
    b=0
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b

x=input("Enter length and breadth separated by commas")
y=x.split(",")
s=Rectangle(int(y[0]),int(y[1]))
a=s.area()
print("Area :",a)
