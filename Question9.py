import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define vertices of a unit cube centered at origin
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

# Define cube faces using vertex indices
faces = [
    [0, 1, 2, 3],  # bottom
    [4, 5, 6, 7],  # top
    [0, 1, 5, 4],  # front
    [2, 3, 7, 6],  # back
    [1, 2, 6, 5],  # right
    [0, 3, 7, 4]   # left
]

# Define rotation matrix around Y-axis (45 degrees)
theta = np.radians(45)
cos_t = np.cos(theta)
sin_t = np.sin(theta)

rotation_matrix_y = np.array([
    [ cos_t, 0, sin_t, 0],
    [     0, 1,     0, 0],
    [-sin_t, 0, cos_t, 0],
    [     0, 0,     0, 1]
])

# Apply rotation
rotated_vertices = rotation_matrix_y @ cube_vertices

# Function to extract face vertices
def get_faces(verts):
    return [[verts[:3, i] for i in face] for face in faces]

# Plotting
fig = plt.figure(figsize=(12, 6))

# Original cube
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_title('Original Cube')
ax1.add_collection3d(Poly3DCollection(get_faces(cube_vertices), facecolors='cyan', edgecolors='black', alpha=0.6))
ax1.set_xlim([-3, 3])
ax1.set_ylim([-3, 3])
ax1.set_zlim([-3, 3])
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")
ax1.view_init(elev=20, azim=30)

# Rotated cube
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title('Rotated Cube (45° around Y-axis)')
ax2.add_collection3d(Poly3DCollection(get_faces(rotated_vertices), facecolors='orange', edgecolors='black', alpha=0.6))
ax2.set_xlim([-3, 3])
ax2.set_ylim([-3, 3])
ax2.set_zlim([-3, 3])
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
ax2.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()

# Print matrix and one vertex comparison
print("Rotation Matrix (Y-axis, 45 degrees):")
print(rotation_matrix_y)

print("\nOriginal Vertex [0]:", cube_vertices[:3, 0])
print("Rotated Vertex [0]:", rotated_vertices[:3, 0])
print("Rotated Vertex [0] (homogeneous):", rotated_vertices[:, 0])
print("Rotated Vertex [0] (non-homogeneous):", rotated_vertices[:3, 0] / rotated_vertices[3, 0])