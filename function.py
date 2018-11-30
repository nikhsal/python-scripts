def fun(n):
    if n == 0:
        return 1
    else:
        return fun(n-1) + 100

x = input("Enter n :")
print(fun(int(x)))
