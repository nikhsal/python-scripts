list1=[1,2,3,5,6,7,8]
y = input("Enter element to be searched between 1 to 8")
x=int(y)
beg=0
end=len(list1)
n=int(beg+(end-beg)/2)
z=-1
print(beg,n,end)
if x < list1[0] or x > list1[len(list1)-1]:
    print("Not Found")
else:
    while beg <= end:
        if x == list1[n]:
            print("Element found at ",n)
            z = n
            break
        elif list1[n] < x:
            beg = n + 1
        else:
            end = n - 1
        n=int(beg+(end-beg)/2)
if z == -1:
    print("Element not found")
        
