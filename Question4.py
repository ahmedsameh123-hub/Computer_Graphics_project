import numpy as np
import matplotlib.pyplot as plt

def reflect_over_line(x, y, line_slope=1, line_intercept=3):
    """
    Reflect a point (x, y) over the line y = mx + b.
    Default is y = x + 3 (m=1, b=3).
    """
    m = line_slope
    b = line_intercept

    # Compute components of the reflection formula
    denominator = 1 + m**2
    a = (1 - m**2) / denominator
    c = (2 * m) / denominator
    d = (-2 * m * b) / denominator
    e = (m**2 - 1) / denominator
    f = (2 * b) / denominator

    # Apply the transformation
    x_reflected = a * x + c * y + d
    y_reflected = e * x + a * y + f

    return x_reflected, y_reflected

# Original point
x_original, y_original = 6, 0

# Reflected point over y = x + 3
x_reflected, y_reflected = reflect_over_line(x_original, y_original)

# Plotting
plt.figure(figsize=(10, 8))

# Line y = x + 3
x_vals = np.linspace(-2, 8, 100)
y_vals = x_vals + 3
plt.plot(x_vals, y_vals, 'g-', label='Line: y = x + 3')

# Plot original and reflected points
plt.scatter(x_original, y_original, color='blue', s=100, label=f'Original: ({x_original}, {y_original})')
plt.scatter(x_reflected, y_reflected, color='red', s=100, label=f'Reflected: ({x_reflected:.1f}, {y_reflected:.1f})')

# Draw a dashed line between the two points
plt.plot([x_original, x_reflected], [y_original, y_reflected], 'k--', alpha=0.6)

# Decorations
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Reflection of a Point Over Line y = x + 3")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

# Print coordinates
print(f"Original point: ({x_original}, {y_original})")
print(f"Reflected point: ({x_reflected:.1f}, {y_reflected:.1f})")