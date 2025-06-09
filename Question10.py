import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define vertices of a cube centered at origin
cube_vertices = np.array([
    [-1, -1, -1, 1],
    [ 1, -1, -1, 1],
    [ 1,  1, -1, 1],
    [-1,  1, -1, 1],
    [-1, -1,  1, 1],
    [ 1, -1,  1, 1],
    [ 1,  1,  1, 1],
    [-1,  1,  1, 1],
]).T  # shape (4, 8)

# Faces of the cube
faces = [
    [0, 1, 2, 3],  # bottom
    [4, 5, 6, 7],  # top
    [0, 1, 5, 4],  # front
    [2, 3, 7, 6],  # back
    [1, 2, 6, 5],  # right
    [0, 3, 7, 4]   # left
]

# Step 1: Scaling matrix (scale x by 2, y by 1.5, z by 1)
scale_matrix = np.array([
    [2.0, 0,   0,   0],
    [0,   1.5, 0,   0],
    [0,   0,   1.0, 0],
    [0,   0,   0,   1]
])

# Step 2: Rotation matrix around Z-axis (30 degrees)
theta = np.radians(30)
cos_t = np.cos(theta)
sin_t = np.sin(theta)

rotation_matrix = np.array([
    [cos_t, -sin_t, 0, 0],
    [sin_t,  cos_t, 0, 0],
    [0,      0,     1, 0],
    [0,      0,     0, 1]
])

# Step 3: Translation matrix (translate by x=3, y=2, z=1)
translation_matrix = np.array([
    [1, 0, 0, 3],
    [0, 1, 0, 2],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])

# Combine transformations: T * R * S
combined_matrix = translation_matrix @ rotation_matrix @ scale_matrix

# Apply transformation
transformed_vertices = combined_matrix @ cube_vertices

# Function to extract face vertices
def get_faces(verts):
    return [[verts[:3, i] for i in face] for face in faces]

# Plotting
fig = plt.figure(figsize=(12, 6))

# Original cube
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_title('Original Cube')
ax1.add_collection3d(Poly3DCollection(get_faces(cube_vertices), facecolors='skyblue', edgecolors='black', alpha=0.6))
ax1.set_xlim([-5, 5])
ax1.set_ylim([-5, 5])
ax1.set_zlim([-5, 5])
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")
ax1.view_init(elev=20, azim=30)

# Transformed cube
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title('Transformed Cube (Scale → Rotate → Translate)')
ax2.add_collection3d(Poly3DCollection(get_faces(transformed_vertices), facecolors='orange', edgecolors='black', alpha=0.6))
ax2.set_xlim([-5, 8])
ax2.set_ylim([-5, 8])
ax2.set_zlim([-5, 8])
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
ax2.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()

# Output matrices for reference
print("Scale Matrix:\n", scale_matrix)
print("\nRotation Matrix (Z-axis, 30 degrees):\n", rotation_matrix)
print("\nTranslation Matrix:\n", translation_matrix)
print("\nCombined Transformation Matrix:\n", combined_matrix)
print("\nTransformed Vertices:\n", transformed_vertices)
# The code above demonstrates a sequence of transformations applied to a cube in 3D space.
# The cube is first scaled by a factor of 2 in the X and Y dimensions, then rotated around the Z-axis by 30 degrees, and finally translated by 3 units in the X and 2 units in the Y dimensions.