import numpy as np

a = np.array([[1,1], [1,2]])
b = np.array([35,47])
x = np.linalg.solve(a, b)
print(x)
print("Chickens",int(x[0]))
print("Rabbit",int(x[1]))
