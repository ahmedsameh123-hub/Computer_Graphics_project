import numpy as np
import matplotlib.pyplot as plt
import math

# 1. Generate clock points on a unit circle
def create_clock_points():
    points = []
    for hour in range(12):
        angle = math.radians(-hour * 30 + 90)  # 30 degrees per hour, starting from the top (12 o'clock)
        x = math.cos(angle)
        y = math.sin(angle)
        points.append([x, y])
    return np.array(points)

# 2. Create a stretching matrix along a given diagonal angle
def create_stretch_matrix(angle_degrees=45, stretch_factor=1.5):
    angle = math.radians(angle_degrees)
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    
    # Rotation to align the diagonal with x-axis
    rotate_to_diagonal = np.array([
        [cos_theta, sin_theta],
        [-sin_theta, cos_theta]
    ])
    
    # Stretching along x-axis
    stretch = np.array([
        [stretch_factor, 0],
        [0, 1]
    ])
    
    # Rotate back to original orientation
    rotate_back = np.array([
        [cos_theta, -sin_theta],
        [sin_theta, cos_theta]
    ])
    
    # Final transformation matrix
    return rotate_back @ stretch @ rotate_to_diagonal

# 3. Apply the transformation
clock_points = create_clock_points()
stretch_matrix = create_stretch_matrix(45, 1.5)  # Stretch 50% along the 45° diagonal
stretched_points = (stretch_matrix @ clock_points.T).T

# 4. Plot the original and stretched clocks
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Original clock
ax1.set_aspect('equal')
ax1.scatter(clock_points[:, 0], clock_points[:, 1], color='blue')
for i, (x, y) in enumerate(clock_points):
    ax1.text(x * 1.1, y * 1.1, f"{i+1}", ha='center', va='center')
ax1.set_title("Original Clock")
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.grid(True)

# Stretched clock
ax2.set_aspect('equal')
ax2.scatter(stretched_points[:, 0], stretched_points[:, 1], color='red')
for i, (x, y) in enumerate(stretched_points):
    ax2.text(x * 1.1, y * 1.1, f"{i+1}", ha='center', va='center')
ax2.set_title("Stretched Clock (50% along 45° diagonal)")
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
ax2.grid(True)

plt.show()

# 5. Print results for documentation
print("Stretch Matrix:")
print(stretch_matrix)

print("\nOriginal Clock Points:")
print(clock_points)

print("\nStretched Clock Points:")
print(stretched_points)