list1 = [12,24,35,70,88,120,155]
list2 = [x for x in list1]
for i in list1:
    if list1.index(i)==0 or list1.index(i)==4 or list1.index(i)==6:    
        list2.remove(i)

print(list2)

