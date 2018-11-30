z=[]
for i in range(1000,3000):
    d = [int(x) for x in str(i)]
    n=0
    for j in d:
        if j%2 == 0:
            n=n+1
    if n==4:
        z.append(i)

print(z)
