import numpy as np
import matplotlib.pyplot as plt

def generate_data(n, degree):
    # Generate x values
    x = np.linspace(-10, 10, n)
    
    # Generate random coefficients for the polynomial
    coefficients = np.random.randn(degree + 1)
    
    # Generate y values based on the polynomial
    y = np.polyval(coefficients, x)
    
    # Add some random error to x and y
    x += np.random.randn(n)
    y += np.random.randn(n)
    
    return x, y

def save_data(x, y, x_filename, y_filename):
    # Save x and y values in .txt files
    np.savetxt(x_filename, x)
    np.savetxt(y_filename, y)

# Example usage:
n = 100
degree = 3
x, y = generate_data(n, degree)

# Save the data
save_data(x, y, f'coord_x{degree}.txt', f'coord_y{degree}.txt')

# Plot the generated data
plt.scatter(x, y)
plt.show()
