x = input("Enter numbers separated by commas : ")
list1 = x.split(",")
list2 = []
for x in list1:
    if int(x)%2 !=0:
        list2.append(int(x)*int(x))

print(list2)

