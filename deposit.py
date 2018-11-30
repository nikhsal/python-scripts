t=int(input("Enter number of lines to be input"))
total=0
while t!=0:
    c, n=input().split()
    n=int(n)
    if c=='D':
        total+=n
    elif c=='W':
        total-=n
    t-=1
print(total)
#t is the number of transactions
#c is to determine whether it's a deposit or withdrawal
#n is the amount of money deposited or withdrawn
