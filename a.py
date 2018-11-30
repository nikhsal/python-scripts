a=input("Enter a number from 1 to 9")
s = [1,11,111,1111]
list1 = [x * int(a) for x in s]
sum1=0
for j in list1:
    sum1=sum1+j
    
print(sum1)
