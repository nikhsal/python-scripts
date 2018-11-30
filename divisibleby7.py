class Generat:
    def div7(self, n):
        x = list(i for i in range(n) if i%7==0)
        print(x)

g=Generat()
n=int(input("Enter n: "))
g.div7(n)

