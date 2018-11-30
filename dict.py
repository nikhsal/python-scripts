import sys

dict = {}
n=sys.argv[1]
for i in range(0,int(n)+1):
    dict[i]=i*i
print(dict)
