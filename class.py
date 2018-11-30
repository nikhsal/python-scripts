class String2:
    str1=""
    
    def printString(self):
        print(self.str1)

    def getString1(self):
        str1=input("enter string")
        return str1

str2=String2()
str2.str1=str2.getString1()
str2.printString()
