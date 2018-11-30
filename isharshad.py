def isharshad(str1):
    index = 0
    sum1 = 0
    while index < len(str1):
      letter = str1[index]
      sum1 = sum1 + int(letter)
      index = index + 1
      print(letter)
      print(sum1)
    q = int(str1)%sum1
    print(q)
    if int(q) == 0:
        print("True")
    else:
        print("Not True")


isharshad("81")
