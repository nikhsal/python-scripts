s = input("Input a string")
u=l=0
for c in s:
    if c.isupper():
        u=u+1
    elif c.islower():
        l=l+1
    else:
        pass
print("Upper", u)
print("Lower", l)
