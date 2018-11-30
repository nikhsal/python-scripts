import math

def squareroot(n):
    x = 2*50*int(n)/30
    h = math.sqrt(x)
    return h

y = input("Enter numbers separated by comma: ")
list = y.split(",")
n = []
for i in list:
    n.append(int(squareroot(i)))

print(n)
