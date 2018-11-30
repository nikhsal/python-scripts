a = input("Enter String")
x = dict((letter,a.count(letter)) for letter in set(a))
print(x)
