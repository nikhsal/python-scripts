class American:
    name="American"
    def getName(self):
        print(self.name)

class Newyorker(American):
    def getName(self):
        print(self.name)

a=American()
a.getName()

b=Newyorker()
b.name="Hello"
b.getName()
