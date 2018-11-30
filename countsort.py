g=input("Enter string:")
l=g.split()
freq=[l.count(i) for i in l]
d=dict(zip(l,freq))
s=sorted(d)
ls={j:d[j] for j in s}
print(ls)
