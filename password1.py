import re
str1= input("Input your password").split(",")
x = True
y=[]
for p in str1:
    while x:
        if (len(p)<6 or len(p)>12):
            break
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[0-9]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[$#@]",p):
            break
        elif re.search("\s",p):
            break
        else:
            y.append(p)
            x=False
            break
print(y)
