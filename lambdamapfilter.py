items = [1, 2, 3, 4, 5,6,7,8,9,10]
even = list(filter(lambda x:x%2==0,items))
squared = list(map(lambda i:i**2,even))
print(squared)

