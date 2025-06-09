import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_translation_matrix(dx, dy, dz):
    """Create 4x4 translation matrix"""
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])

def get_z_rotation_matrix(degrees):
    """Create 4x4 rotation matrix around Z-axis"""
    theta = np.radians(degrees)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    return np.array([
        [cos_theta, -sin_theta, 0, 0],
        [sin_theta, cos_theta, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def get_scaling_matrix(sx, sy, sz):
    """Create 4x4 scaling matrix"""
    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

# Define original triangle vertices (homogeneous coordinates)
triangle = np.array([
    [0, 0, 0, 1],  # Vertex 1
    [1, 0, 0, 1],  # Vertex 2
    [0.5, 1, 0, 1],  # Vertex 3
    [0, 0, 0, 1]   # Close the triangle
])

# Define transformation matrices
translation = get_translation_matrix(4, 0, 2)  # Translate by (4, 0, 2)
rotation = get_z_rotation_matrix(90)          # Rotate 90° around Z-axis
scaling = get_scaling_matrix(2, 3, 4)         # Scale by (2, 3, 4)

# Apply transformations to triangle
transformed_triangle = (translation @ rotation @ scaling @ triangle.T).T

# Apply transformations to point P = (1, 2, 3)
P = np.array([1, 2, 3, 1])
P_transformed = translation @ rotation @ scaling @ P

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot original triangle (red)
ax.plot(triangle[:, 0], triangle[:, 1], triangle[:, 2], 
        'r-', label="Original Triangle", linewidth=3)

# Plot transformed triangle (green dashed)
ax.plot(transformed_triangle[:, 0], transformed_triangle[:, 1], transformed_triangle[:, 2],
        'g--', label="Transformed Triangle", linewidth=3)

# Configure plot
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Triangle Transformations\n(Translation + Rotation + Scaling)')
ax.legend()

plt.tight_layout()
plt.show()  

# Print matrices and results
print("Translation Matrix:\n", translation)
print("\nRotation Matrix (90° around Z):\n", rotation)
print("\nScaling Matrix:\n", scaling)
print("\nOriginal point P:", P[:3])
print("Transformed point P':", P_transformed[:3])