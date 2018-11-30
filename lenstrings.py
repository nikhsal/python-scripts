def length(str1,str2):
    if len(str1)>len(str2):
        return str1
    elif len(str1)<len(str2):
        return str2
    else:
        return str1+str2

x=input("First string")
y=input("Second string")
print(length(x,y))

