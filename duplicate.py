ip = input("Enter words  to remove duplicates: ")
print(ip)
s = ip.split(" ")
print(s)
t = set(s)
u=list(t)
u.sort()
print(u)

