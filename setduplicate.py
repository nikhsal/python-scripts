list2 = [12,24,35,24,88,120,155,88,120,155]
newlist = []
for i in list2:
    if i not in newlist:
        newlist.append(i)

print(newlist)
