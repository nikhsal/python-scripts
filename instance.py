class A:
    a="I am a class attribute"

x=A()
x.a="I am instance attribute"
print("Instance x",x.a)
y=A()
print("Instance y", y.a)
