import numpy as np
from OpenGL.GL import *

def draw_cube(size=1.0):
    hs = size / 2.0
    vertices = [
        [ hs, hs, hs], [ hs,-hs, hs], [-hs,-hs, hs], [-hs, hs, hs], # front
        [ hs, hs,-hs], [ hs,-hs,-hs], [-hs,-hs,-hs], [-hs, hs,-hs], # back
    ]
    faces = [
        [0,1,2,3], [4,5,6,7], [0,4,5,1],
        [3,7,6,2], [0,4,7,3], [1,5,6,2]
    ]
    glBegin(GL_QUADS)
    for face in faces:
        for v in face:
            glVertex3fv(vertices[v])
    glEnd()

def draw_sphere(radius=1.0, slices=16, stacks=16):
    for i in range(stacks):
        lat0 = np.pi * (-0.5 + float(i) / stacks)
        z0  = radius * np.sin(lat0)
        zr0 = radius * np.cos(lat0)

        lat1 = np.pi * (-0.5 + float(i+1) / stacks)
        z1 = radius * np.sin(lat1)
        zr1 = radius * np.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices+1):
            lng = 2 * np.pi * float(j) / slices
            x = np.cos(lng)
            y = np.sin(lng)
            glVertex3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()

def draw_cylinder(radius=0.4, height=0.2, slices=32):
    glBegin(GL_QUAD_STRIP)
    for i in range(slices+1):
        angle = 2 * np.pi * i / slices
        x = np.cos(angle) * radius
        y = np.sin(angle) * radius
        glVertex3f(x, y, 0)
        glVertex3f(x, y, height)
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, height)
    for i in range(slices+1):
        angle = 2 * np.pi * i / slices
        x = np.cos(angle) * radius
        y = np.sin(angle) * radius
        glVertex3f(x, y, height)
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    for i in range(slices+1):
        angle = 2 * np.pi * i / slices
        x = np.cos(angle) * radius
        y = np.sin(angle) * radius
        glVertex3f(x, y, 0)
    glEnd()

def translate(matrix, translation_vector):
    translation_matrix = np.array([
        [1, 0, 0, translation_vector[0]],
        [0, 1, 0, translation_vector[1]],
        [0, 0, 1, translation_vector[2]],
        [0, 0, 0, 1]
    ])
    return translation_matrix @ matrix

def rotate(matrix, angle, axis):
    angle_rad = np.radians(angle)
    c = np.cos(angle_rad)
    s = np.sin(angle_rad)
    if axis == 'x':
        rotation_matrix = np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'y':
        rotation_matrix = np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'z':
        rotation_matrix = np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    return rotation_matrix @ matrix

def scale(matrix, scale_vector):
    scaling_matrix = np.array([
        [scale_vector[0], 0, 0, 0],
        [0, scale_vector[1], 0, 0],
        [0, 0, scale_vector[2], 0],
        [0, 0, 0, 1]
    ])
    return scaling_matrix @ matrix