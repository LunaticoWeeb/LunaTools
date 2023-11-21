import numpy as np

x_data = np.loadtxt("x_noisy.txt")
y_data = np.loadtxt("y_noisy.txt")

# valor esperado a = 2.3, b = 0.45

a, b = np.polyfit(x_data, y_data, 1) # 1 = grau do polinomio

print("a = ", a)
print("b = ", b)