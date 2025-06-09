import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Shear in XZ by Y (X = X + y*factor, Z = Z + y*factor)
def shear_xz_by_y_matrix(factor=0.5):
    return np.array([
        [1, factor, 0, 0],
        [0, 1, 0, 0],
        [0, factor, 1, 0],
        [0, 0, 0, 1]
    ])

# 2. Taper in Y by Z
def taper_y_by_z_matrix(factor=0.2):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, factor, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# 3. Scale in Z
def scale_z_matrix(factor=3):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, factor, 0],
        [0, 0, 0, 1]
    ])

# 4. Rotate around Y
def rotate_y_matrix(degrees=45):
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]
    ])

# 5. Translation
def translate_matrix(dx=-2, dy=3, dz=1):
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])

# Composite transformation (T * Ry * Sz * Tyz * Sxz)
def composite_transform():
    Sxz = shear_xz_by_y_matrix(0.5)
    Tyz = taper_y_by_z_matrix(0.2)
    Sz = scale_z_matrix(3)
    Ry = rotate_y_matrix(45)
    T = translate_matrix(-2, 3, 1)
    return T @ Ry @ Sz @ Tyz @ Sxz

# Original point
P = np.array([3, 2, 1, 1])
M = composite_transform()
P_transformed = M @ P

# Visualization
fig = plt.figure(figsize=(15, 6))

# Original
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(P[0], P[1], P[2], color='r', s=100, label='Original Point (3,2,1)')
ax1.quiver(0, 0, 0, 5, 0, 0, color='r', arrow_length_ratio=0.1)
ax1.quiver(0, 0, 0, 0, 5, 0, color='g', arrow_length_ratio=0.1)
ax1.quiver(0, 0, 0, 0, 0, 5, color='b', arrow_length_ratio=0.1)
ax1.set_title('Original Position')
ax1.set_xlim(-5, 10)
ax1.set_ylim(-5, 10)
ax1.set_zlim(-5, 10)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.legend()

# Transformed
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(P_transformed[0], P_transformed[1], P_transformed[2], 
           color='b', s=100, label=f'Transformed Point ({P_transformed[0]:.1f},{P_transformed[1]:.1f},{P_transformed[2]:.1f})')

# Transformed axes
x_axis = M @ np.array([5, 0, 0, 1])
y_axis = M @ np.array([0, 5, 0, 1])
z_axis = M @ np.array([0, 0, 5, 1])
origin = M @ np.array([0, 0, 0, 1])

ax2.quiver(origin[0], origin[1], origin[2], 
           x_axis[0]-origin[0], x_axis[1]-origin[1], x_axis[2]-origin[2], 
           color='r', arrow_length_ratio=0.1)
ax2.quiver(origin[0], origin[1], origin[2], 
           y_axis[0]-origin[0], y_axis[1]-origin[1], y_axis[2]-origin[2], 
           color='g', arrow_length_ratio=0.1)
ax2.quiver(origin[0], origin[1], origin[2], 
           z_axis[0]-origin[0], z_axis[1]-origin[1], z_axis[2]-origin[2], 
           color='b', arrow_length_ratio=0.1)

ax2.set_title('After Composite Transformations')
ax2.set_xlim(-5, 10)
ax2.set_ylim(-5, 10)
ax2.set_zlim(-5, 10)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.legend()

plt.tight_layout()
plt.show()

# Print matrices and result
print("Individual Transformation Matrices:")
print(f"\n1. Shear XZ by Y (factor 0.5):\n{shear_xz_by_y_matrix(0.5)}")
print(f"\n2. Taper Y by Z (factor 0.2):\n{taper_y_by_z_matrix(0.2)}")
print(f"\n3. Scale Z by 3:\n{scale_z_matrix(3)}")
print(f"\n4. Rotate 45° around Y:\n{rotate_y_matrix(45)}")
print(f"\n5. Translate by (-2, 3, 1):\n{translate_matrix(-2, 3, 1)}")

print("\nComposite Transformation Matrix (T * Ry * Sz * Tyz * Sxz):")
print(M)

print("\nPoint Transformation Results:")
print(f"Original point: {P[:3]}")
print(f"Transformed point: {P_transformed[:3]}")