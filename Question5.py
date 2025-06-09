import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def translation_matrix(dx, dy, dz):
    """Create 4x4 translation matrix"""
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])

def rotation_x_matrix(degrees):
    """Create 4x4 rotation matrix around X-axis"""
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]
    ])

def rotation_y_matrix(degrees):
    """Create 4x4 rotation matrix around Y-axis"""
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]
    ])

# Transformation sequence (Question 5)
def composite_transformation(a):
    """Create composite transformation matrix"""
    T1 = translation_matrix(0, a, 0)        # Translate Y by a
    R1 = rotation_x_matrix(90)              # Rotate 90° CCW around X (positive X)
    T2 = translation_matrix(0, 0, a)        # Translate Z by a
    R2 = rotation_y_matrix(90)              # Rotate 90° CCW around Y (positive Y)
    
    # Apply transformations in reverse order (right-to-left)
    return R2 @ T2 @ R1 @ T1

# Parameters
a = 2  # Arbitrary translation value
P = np.array([1, 1, 1, 1])  # Original point in homogeneous coordinates

# Calculate composite matrix
M = composite_transformation(a)
P_transformed = M @ P

# Create 3D visualization
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# Original point and axes
ax1.scatter(P[0], P[1], P[2], color='r', s=100, label='Original Point')
ax1.quiver(0, 0, 0, 2, 0, 0, color='r', arrow_length_ratio=0.1)
ax1.quiver(0, 0, 0, 0, 2, 0, color='g', arrow_length_ratio=0.1)
ax1.quiver(0, 0, 0, 0, 0, 2, color='b', arrow_length_ratio=0.1)
ax1.set_title('Original Position')
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)
ax1.set_zlim(-3, 3)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.legend()

# Transformed point and axes
ax2.scatter(P_transformed[0], P_transformed[1], P_transformed[2], 
           color='b', s=100, label='Transformed Point')

# Transform axes to show effect
x_axis = M @ np.array([2, 0, 0, 1])
y_axis = M @ np.array([0, 2, 0, 1])
z_axis = M @ np.array([0, 0, 2, 1])

ax2.quiver(0, 0, 0, x_axis[0], x_axis[1], x_axis[2], color='r', arrow_length_ratio=0.1)
ax2.quiver(0, 0, 0, y_axis[0], y_axis[1], y_axis[2], color='g', arrow_length_ratio=0.1)
ax2.quiver(0, 0, 0, z_axis[0], z_axis[1], z_axis[2], color='b', arrow_length_ratio=0.1)

ax2.set_title('After Composite Transformations')
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.set_zlim(-3, 3)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.legend()

plt.tight_layout()
plt.show()

# Print detailed transformation steps
print("Step-by-Step Transformation Matrices:")
print(f"\n1. Translate Y by {a}:\n{translation_matrix(0, a, 0)}")
print(f"\n2. Rotate 90° around X:\n{rotation_x_matrix(90)}")
print(f"\n3. Translate Z by {a}:\n{translation_matrix(0, 0, a)}")
print(f"\n4. Rotate 90° around Y:\n{rotation_y_matrix(90)}")

print("\nComposite Transformation Matrix (M = R2 * T2 * R1 * T1):")
print(M)

print("\nPoint Transformation:")
print(f"Original P: {P[:3]}")
print(f"Transformed P': {P_transformed[:3]}")