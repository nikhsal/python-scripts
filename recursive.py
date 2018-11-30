def fun(n):
    if n == 1:
        return 0.5
    else:
        return fun(n-1) + float(n/(n+1))

x = input("Enter n :")
print(fun(float(x)))
