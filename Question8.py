import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define vertices of a unit cube centered at origin (length = 2)
cube_vertices = np.array([
    [-1, -1, -1, 1],
    [ 1, -1, -1, 1],
    [ 1,  1, -1, 1],
    [-1,  1, -1, 1],
    [-1, -1,  1, 1],
    [ 1, -1,  1, 1],
    [ 1,  1,  1, 1],
    [-1,  1,  1, 1],
]).T  # Shape: (4, 8)

# Define cube faces using vertex indices
faces = [
    [0, 1, 2, 3],  # bottom
    [4, 5, 6, 7],  # top
    [0, 1, 5, 4],  # front
    [2, 3, 7, 6],  # back
    [1, 2, 6, 5],  # right
    [0, 3, 7, 4]   # left
]

# Non-uniform scaling matrix
scaling_matrix = np.array([
    [2,   0,   0, 0],   # scale X by 2
    [0,   1,   0, 0],   # scale Y by 1
    [0,   0, 0.5, 0],   # scale Z by 0.5
    [0,   0,   0, 1]
])

# Apply scaling to cube
transformed_vertices = scaling_matrix @ cube_vertices  # shape (4,8)

# Function to extract face vertices from vertex array
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

# Transformed cube
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title('Transformed Cube (Scaled)')
ax2.add_collection3d(Poly3DCollection(get_faces(transformed_vertices), facecolors='orange', edgecolors='black', alpha=0.6))
ax2.set_xlim([-3, 3])
ax2.set_ylim([-3, 3])
ax2.set_zlim([-3, 3])
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
ax2.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()

# Print matrices and results
print("Non-uniform Scaling Matrix (Sx=2, Sy=1, Sz=0.5):")
print(scaling_matrix)

print("\nOriginal Vertex [0]:", cube_vertices[:3, 0])
print("Transformed Vertex [0]:", transformed_vertices[:3, 0])
