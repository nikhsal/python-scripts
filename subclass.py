class Parent:
    def getGender(self):
        print("This is Parent")

class Male(Parent):
    def getGender(self):
        print("This is Male")

class Female(Parent):
    def getGender(self):
        print("This is Female")

m = Male()
m.getGender()

f=Female()
f.getGender()
