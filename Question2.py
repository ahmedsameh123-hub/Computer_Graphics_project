import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_view_matrix(camera_pos, target_pos, up_vector):
    """Calculate the view matrix for camera transformation"""
    forward = (camera_pos - target_pos) / np.linalg.norm(camera_pos - target_pos)
    right = np.cross(up_vector, forward) / np.linalg.norm(np.cross(up_vector, forward))
    up = np.cross(forward, right)
    
    rotation = np.identity(4)
    rotation[:3, 0] = right
    rotation[:3, 1] = up
    rotation[:3, 2] = forward
    
    translation = np.identity(4)
    translation[:3, 3] = -camera_pos
    
    return rotation @ translation

# Define camera parameters
camera_position = np.array([0, 1, 0])
target_position = np.array([0, 0, 0])
up_vector = np.array([1, 1, 0])

# Calculate view matrix
view_matrix = calculate_view_matrix(camera_position, target_position, up_vector)

# Create a simple 3D object (cube vertices)
cube_vertices = np.array([
    [-0.5, -0.5, -0.5, 1],
    [0.5, -0.5, -0.5, 1],
    [0.5, 0.5, -0.5, 1],
    [-0.5, 0.5, -0.5, 1],
    [-0.5, -0.5, 0.5, 1],
    [0.5, -0.5, 0.5, 1],
    [0.5, 0.5, 0.5, 1],
    [-0.5, 0.5, 0.5, 1]
])

# Transform cube to camera space
transformed_cube = (view_matrix @ cube_vertices.T).T

# Create figure
fig = plt.figure(figsize=(12, 6))

# Plot in world coordinates
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(camera_position[0], camera_position[1], camera_position[2], c='r', s=100, label='Camera')
ax1.scatter(target_position[0], target_position[1], target_position[2], c='g', s=100, label='Target')
ax1.quiver(*camera_position, *(target_position-camera_position), color='b', label='View Direction')
ax1.quiver(*camera_position, *up_vector, color='y', label='Up Vector')

# Plot cube in world space
for i in range(4):
    ax1.plot([cube_vertices[i, 0], cube_vertices[(i+1)%4, 0]],
             [cube_vertices[i, 1], cube_vertices[(i+1)%4, 1]],
             [cube_vertices[i, 2], cube_vertices[(i+1)%4, 2]], 'k-')
    ax1.plot([cube_vertices[i+4, 0], cube_vertices[(i+1)%4+4, 0]],
             [cube_vertices[i+4, 1], cube_vertices[(i+1)%4+4, 1]],
             [cube_vertices[i+4, 2], cube_vertices[(i+1)%4+4, 2]], 'k-')
    ax1.plot([cube_vertices[i, 0], cube_vertices[i+4, 0]],
             [cube_vertices[i, 1], cube_vertices[i+4, 1]],
             [cube_vertices[i, 2], cube_vertices[i+4, 2]], 'k-')

ax1.set_title('World Space')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.legend()

# Plot in camera coordinates
ax2 = fig.add_subplot(122, projection='3d')
for i in range(4):
    ax2.plot([transformed_cube[i, 0], transformed_cube[(i+1)%4, 0]],
             [transformed_cube[i, 1], transformed_cube[(i+1)%4, 1]],
             [transformed_cube[i, 2], transformed_cube[(i+1)%4, 2]], 'k-')
    ax2.plot([transformed_cube[i+4, 0], transformed_cube[(i+1)%4+4, 0]],
             [transformed_cube[i+4, 1], transformed_cube[(i+1)%4+4, 1]],
             [transformed_cube[i+4, 2], transformed_cube[(i+1)%4+4, 2]], 'k-')
    ax2.plot([transformed_cube[i, 0], transformed_cube[i+4, 0]],
             [transformed_cube[i, 1], transformed_cube[i+4, 1]],
             [transformed_cube[i, 2], transformed_cube[i+4, 2]], 'k-')

ax2.scatter(0, 0, 0, c='r', s=100, label='Camera (Origin)')
ax2.quiver(0, 0, 0, 0, 0, -1, color='b', label='View Direction (Z-axis)')
ax2.quiver(0, 0, 0, *up_vector/np.linalg.norm(up_vector), color='y', label='Up Vector')

ax2.set_title('Camera Space')
ax2.set_xlabel('X (Right)')
ax2.set_ylabel('Y (Up)')
ax2.set_zlabel('Z (Forward)')
ax2.legend()

plt.tight_layout()
plt.show()

# Print results
print("Camera Position:", camera_position)
print("Target Position:", target_position)
print("Up Vector:", up_vector)
print("\nView Matrix:\n", view_matrix)