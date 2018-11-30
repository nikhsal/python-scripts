import math
class Circle:
    r=0
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r*math.pi*self.r

x=input("Enter radius")
s=Circle(int(x))

y=s.area()
print("Area : ",y)
