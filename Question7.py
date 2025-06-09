import numpy as np
import matplotlib.pyplot as plt

# Define the original square in the XY-plane
# Square of side length 2 centered at origin (0,0)
square = np.array([
    [-1, -1, 0, 1],
    [ 1, -1, 0, 1],
    [ 1,  1, 0, 1],
    [-1,  1, 0, 1],
    [-1, -1, 0, 1]  # To close the shape
]).T  # Transpose for matrix multiplication

# Define rotation by 45° around the center (0,0)
theta = np.radians(45)
cos_t, sin_t = np.cos(theta), np.sin(theta)
rotation_matrix = np.array([
    [cos_t, -sin_t, 0, 0],
    [sin_t,  cos_t, 0, 0],
    [0,      0,     1, 0],
    [0,      0,     0, 1]
])

# Define translation by (3, 2, 0)
translation_matrix = np.array([
    [1, 0, 0, 3],
    [0, 1, 0, 2],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Composite transformation: First rotate, then translate
composite_matrix = translation_matrix @ rotation_matrix

# Apply the composite transformation to the square
transformed_square = composite_matrix @ square

# Plotting
plt.figure(figsize=(8, 8))

# Plot original square
plt.plot(square[0], square[1], 'b-o', label='Original Square')

# Plot transformed square
plt.plot(transformed_square[0], transformed_square[1], 'r-o', label='Transformed Square')

# Coordinate axes and grid
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()

# Labels and limits
plt.title("Square: Rotate 45° around center, then translate (3,2,0)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xlim(-3, 7)
plt.ylim(-3, 7)

# Show plot
plt.show()
