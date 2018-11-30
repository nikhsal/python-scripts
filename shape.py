class Shape:
    l = 0
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,l):
        self.l=l
    def area(self):
        return self.l*self.l

x=input("Enter length")
s=Square(int(x))

y=s.area()
print(y)
