import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from math import sin, cos, radians, pi

# --------- Draw coordinate axes ---------
def draw_axes():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)  # X axis (Red)
    glVertex3f(0, 0, 0)
    glVertex3f(5, 0, 0)
    glColor3f(0, 1, 0)  # Y axis (Green)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 5, 0)
    glColor3f(0, 0, 1)  # Z axis (Blue)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 5)
    glEnd()

# --------- Draw a cube ---------
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

# --------- Draw a point ---------
def draw_point(x, y, z, color=(1,0,0)):
    glColor3f(*color)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex3f(x, y, z)
    glEnd()

# --------- Draw a square in XY plane ---------
def draw_square(size=2.0):
    hs = size / 2.0
    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,1)
    for x, y in [(-hs,-hs),(hs,-hs),(hs,hs),(-hs,hs)]:
        glVertex3f(x, y, 0)
    glEnd()

# --------- Draw a clock (12 points on a circle) ---------
def draw_clock(points, color=(0,0,1)):
    glColor3f(*color)
    glBegin(GL_LINE_LOOP)
    for x, y in points:
        glVertex3f(x, y, 0)
    glEnd()
    glPointSize(8)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex3f(x, y, 0)
    glEnd()

# --------- Draw a cube using a transformation matrix ---------
def draw_cube_matrix(matrix, color=(0.5,0.5,1)):
    # 8 vertices of a unit cube
    cube = np.array([
        [-1, -1, -1, 1],
        [ 1, -1, -1, 1],
        [ 1,  1, -1, 1],
        [-1,  1, -1, 1],
        [-1, -1,  1, 1],
        [ 1, -1,  1, 1],
        [ 1,  1,  1, 1],
        [-1,  1,  1, 1],
    ])
    # Apply transformation
    transformed = (matrix @ cube.T).T
    # Draw cube faces as wireframe
    faces = [
        [0,1,2,3], [4,5,6,7], [0,1,5,4],
        [2,3,7,6], [1,2,6,5], [0,3,7,4]
    ]
    glColor3f(*color)
    for face in faces:
        glBegin(GL_LINE_LOOP)
        for idx in face:
            glVertex3fv(transformed[idx][:3])
        glEnd()

# --------- Parameters for each question ---------
# Q1: Translation, Rotation, Scaling
q1_translation = [0.0, 0.0, 0.0]
q1_angle = 0.0
q1_scale = [1.0, 1.0, 1.0]

# Q2: Camera parameters
q2_camera = [0.0, 1.0, 8.0]
q2_look = [0.0, 0.0, 0.0]
q2_up = [0.0, 1.0, 0.0]

# Q3: Clock stretching
q3_stretch = 1.0

# Q4: Reflection
q4_point = [3.0, 0.0]
q4_m = 1.0
q4_b = 3.0

# Q5: Composite transform
q5_a = 2.0

# Q6: Shear, Taper, Scale, Rotate, Translate
q6_shear = 0.5
q6_taper = 0.2
q6_scale = 3.0
q6_angle = 45.0
q6_trans = [-2, 3, 1]

# Q7: Square rotate/translate
q7_angle = 45.0
q7_tx = 3.0
q7_ty = 2.0

# Q8: Cube scaling
q8_sx = 2.0
q8_sy = 1.0
q8_sz = 0.5

# Q9: Cube rotation
q9_angle = 45.0

# Q10: Scale, rotate, translate
q10_sx = 2.0
q10_sy = 1.5
q10_sz = 1.0
q10_angle = 30.0
q10_tx = 3.0
q10_ty = 2.0
q10_tz = 1.0

# --------- Draw each question ---------
def draw_question(q):
    glPushMatrix()
    draw_axes()
    if q == 1:
        # Q1: Translation + Rotation + Scaling
        glTranslatef(*q1_translation)
        glRotatef(q1_angle, 0, 0, 1)
        glScalef(*q1_scale)
        glColor3f(0,1,0)
        draw_cube(1)
        draw_point(0, 0, 0, (1,0,0))
    elif q == 2:
        # Q2: Camera movement
        glLoadIdentity()
        gluLookAt(*q2_camera, *q2_look, *q2_up)
        draw_cube(2)
    elif q == 3:
        # Q3: Clock stretching
        points = []
        for hour in range(12):
            angle = radians(-hour * 30 + 90)
            x = cos(angle)
            y = sin(angle)
            points.append([x, y])
        theta = radians(45)
        c, s = cos(theta), sin(theta)
        stretch = np.array([
            [1 + (q3_stretch-1)*c*c, (q3_stretch-1)*c*s],
            [(q3_stretch-1)*c*s, 1 + (q3_stretch-1)*s*s]
        ])
        stretched = (stretch @ np.array(points).T).T
        draw_clock(points, (0,0,1))      # Original clock (blue)
        draw_clock(stretched, (1,0,0))   # Stretched clock (red)
    elif q == 4:
        # Q4: Reflection over y=mx+b
        m, b = q4_m, q4_b
        x, y = q4_point
        denom = 1 + m**2
        xr = ((1-m**2)*x + 2*m*y - 2*m*b)/denom
        yr = ((m**2-1)*y + 2*m*x + 2*b)/denom
        # Draw the line y=mx+b
        glColor3f(0,1,0)
        glBegin(GL_LINES)
        for t in np.linspace(-5,5,2):
            glVertex3f(t, m*t+b, 0)
        glEnd()
        # Draw original and reflected points
        draw_point(x, y, 0, (1,0,0))
        draw_point(xr, yr, 0, (0,0,1))
    elif q == 5:
        # Q5: Composite transformation
        def translation(dx,dy,dz):
            return np.array([
                [1,0,0,dx],[0,1,0,dy],[0,0,1,dz],[0,0,0,1]
            ])
        def rot_x(deg):
            t = radians(deg)
            c,s = cos(t), sin(t)
            return np.array([
                [1,0,0,0],[0,c,-s,0],[0,s,c,0],[0,0,0,1]
            ])
        def rot_y(deg):
            t = radians(deg)
            c,s = cos(t), sin(t)
            return np.array([
                [c,0,s,0],[0,1,0,0],[-s,0,c,0],[0,0,0,1]
            ])
        T1 = translation(0, q5_a, 0)
        R1 = rot_x(90)
        T2 = translation(0, 0, q5_a)
        R2 = rot_y(90)
        M = R2 @ T2 @ R1 @ T1
        draw_cube_matrix(np.eye(4), (0,1,0))  # Original cube (green)
        draw_cube_matrix(M, (1,0,0))          # Transformed cube (red)
    elif q == 6:
        # Q6: Shear, Taper, Scale, Rotate, Translate
        def shear_xz_by_y(f=0.5):
            return np.array([
                [1, f, 0, 0],[0,1,0,0],[0,f,1,0],[0,0,0,1]
            ])
        def taper_y_by_z(f=0.2):
            return np.array([
                [1,0,0,0],[0,1,f,0],[0,0,1,0],[0,0,0,1]
            ])
        def scale_z(f=3):
            return np.array([
                [1,0,0,0],[0,1,0,0],[0,0,f,0],[0,0,0,1]
            ])
        def rot_y(deg):
            t = radians(deg)
            c,s = cos(t), sin(t)
            return np.array([
                [c,0,s,0],[0,1,0,0],[-s,0,c,0],[0,0,0,1]
            ])
        def trans(dx,dy,dz):
            return np.array([
                [1,0,0,dx],[0,1,0,dy],[0,0,1,dz],[0,0,0,1]
            ])
        M = trans(*q6_trans) @ rot_y(q6_angle) @ scale_z(q6_scale) @ taper_y_by_z(q6_taper) @ shear_xz_by_y(q6_shear)
        draw_cube_matrix(np.eye(4), (0,1,0))  # Original cube (green)
        draw_cube_matrix(M, (1,0,0))          # Transformed cube (red)
    elif q == 7:
        # Q7: Square rotate then translate
        glPushMatrix()
        glTranslatef(q7_tx, q7_ty, 0)
        glRotatef(q7_angle, 0,0,1)
        draw_square(2)
        glPopMatrix()
        draw_square(2)  # Original square
    elif q == 8:
        # Q8: Cube with non-uniform scaling
        S = np.array([
            [q8_sx,0,0,0],[0,q8_sy,0,0],[0,0,q8_sz,0],[0,0,0,1]
        ])
        draw_cube_matrix(np.eye(4), (0,1,0))  # Original cube (green)
        draw_cube_matrix(S, (1,0,0))          # Scaled cube (red)
    elif q == 9:
        # Q9: Cube rotation around Y
        theta = radians(q9_angle)
        c,s = cos(theta), sin(theta)
        R = np.array([
            [c,0,s,0],[0,1,0,0],[-s,0,c,0],[0,0,0,1]
        ])
        draw_cube_matrix(np.eye(4), (0,1,0))  # Original cube (green)
        draw_cube_matrix(R, (1,0,0))          # Rotated cube (red)
    elif q == 10:
        # Q10: Scale, rotate, translate
        S = np.array([
            [q10_sx,0,0,0],[0,q10_sy,0,0],[0,0,q10_sz,0],[0,0,0,1]
        ])
        theta = radians(q10_angle)
        c,s = cos(theta), sin(theta)
        R = np.array([
            [c,-s,0,0],[s,c,0,0],[0,0,1,0],[0,0,0,1]
        ])
        T = np.array([
            [1,0,0,q10_tx],[0,1,0,q10_ty],[0,0,1,q10_tz],[0,0,0,1]
        ])
        M = T @ R @ S
        draw_cube_matrix(np.eye(4), (0,1,0))      # Original cube (green)
        draw_cube_matrix(M, (1,0.5,0))            # Transformed cube (orange)
    glPopMatrix()

def main():
    # Make all parameter variables global so they can be modified inside the loop
    global q1_translation, q1_angle, q1_scale
    global q2_camera, q2_look, q2_up
    global q3_stretch
    global q4_point, q4_m, q4_b
    global q5_a
    global q6_shear, q6_taper, q6_scale, q6_angle, q6_trans
    global q7_angle, q7_tx, q7_ty
    global q8_sx, q8_sy, q8_sz
    global q9_angle
    global q10_sx, q10_sy, q10_sz, q10_angle, q10_tx, q10_ty, q10_tz

    pygame.init()
    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -10)

    current_question = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                # Switch between questions
                if pygame.K_1 <= event.key <= pygame.K_9:
                    current_question = event.key - pygame.K_0
                elif event.key == pygame.K_0:
                    current_question = 10
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                # Controls for each question
                if current_question == 1:
                    # Q1: Move, scale, rotate
                    if event.key == pygame.K_LEFT: q1_translation[0] -= 0.2
                    if event.key == pygame.K_RIGHT: q1_translation[0] += 0.2
                    if event.key == pygame.K_UP: q1_translation[1] += 0.2
                    if event.key == pygame.K_DOWN: q1_translation[1] -= 0.2
                    if event.key == pygame.K_w: q1_scale = [x+0.1 for x in q1_scale]
                    if event.key == pygame.K_s: q1_scale = [max(0.1,x-0.1) for x in q1_scale]
                    if event.key == pygame.K_a: q1_angle += 5
                    if event.key == pygame.K_d: q1_angle -= 5
                elif current_question == 2:
                    # Q2: Move camera
                    if event.key == pygame.K_LEFT: q2_camera[0] -= 0.5
                    if event.key == pygame.K_RIGHT: q2_camera[0] += 0.5
                    if event.key == pygame.K_UP: q2_camera[1] += 0.5
                    if event.key == pygame.K_DOWN: q2_camera[1] -= 0.5
                    if event.key == pygame.K_w: q2_camera[2] -= 0.5
                    if event.key == pygame.K_s: q2_camera[2] += 0.5
                elif current_question == 3:
                    # Q3: Stretch clock
                    if event.key == pygame.K_w: q3_stretch += 0.1
                    if event.key == pygame.K_s: q3_stretch = max(0.1, q3_stretch-0.1)
                elif current_question == 4:
                    # Q4: Move point, change line
                    if event.key == pygame.K_LEFT: q4_point[0] -= 0.2
                    if event.key == pygame.K_RIGHT: q4_point[0] += 0.2
                    if event.key == pygame.K_UP: q4_point[1] += 0.2
                    if event.key == pygame.K_DOWN: q4_point[1] -= 0.2
                    if event.key == pygame.K_w: q4_m += 0.1
                    if event.key == pygame.K_s: q4_m -= 0.1
                    if event.key == pygame.K_a: q4_b += 0.1
                    if event.key == pygame.K_d: q4_b -= 0.1
                elif current_question == 5:
                    # Q5: Change parameter a
                    if event.key == pygame.K_w: q5_a += 0.2
                    if event.key == pygame.K_s: q5_a = max(0.1, q5_a-0.2)
                elif current_question == 6:
                    # Q6: Shear and rotate
                    if event.key == pygame.K_w: q6_shear += 0.1
                    if event.key == pygame.K_s: q6_shear -= 0.1
                    if event.key == pygame.K_a: q6_angle += 5
                    if event.key == pygame.K_d: q6_angle -= 5
                elif current_question == 7:
                    # Q7: Rotate and move square
                    if event.key == pygame.K_a: q7_angle += 5
                    if event.key == pygame.K_d: q7_angle -= 5
                    if event.key == pygame.K_LEFT: q7_tx -= 0.2
                    if event.key == pygame.K_RIGHT: q7_tx += 0.2
                    if event.key == pygame.K_UP: q7_ty += 0.2
                    if event.key == pygame.K_DOWN: q7_ty -= 0.2
                elif current_question == 8:
                    # Q8: Scale cube
                    if event.key == pygame.K_w: q8_sx += 0.1
                    if event.key == pygame.K_s: q8_sx = max(0.1, q8_sx-0.1)
                    if event.key == pygame.K_a: q8_sy += 0.1
                    if event.key == pygame.K_d: q8_sy = max(0.1, q8_sy-0.1)
                    if event.key == pygame.K_q: q8_sz += 0.1
                    if event.key == pygame.K_e: q8_sz = max(0.1, q8_sz-0.1)
                elif current_question == 9:
                    # Q9: Rotate cube
                    if event.key == pygame.K_a: q9_angle += 5
                    if event.key == pygame.K_d: q9_angle -= 5
                elif current_question == 10:
                    # Q10: Scale, rotate, translate cube
                    if event.key == pygame.K_w: q10_sx += 0.1
                    if event.key == pygame.K_s: q10_sx = max(0.1, q10_sx-0.1)
                    if event.key == pygame.K_a: q10_sy += 0.1
                    if event.key == pygame.K_d: q10_sy = max(0.1, q10_sy-0.1)
                    if event.key == pygame.K_q: q10_sz += 0.1
                    if event.key == pygame.K_e: q10_sz = max(0.1, q10_sz-0.1)
                    if event.key == pygame.K_LEFT: q10_tx -= 0.2
                    if event.key == pygame.K_RIGHT: q10_tx += 0.2
                    if event.key == pygame.K_UP: q10_ty += 0.2
                    if event.key == pygame.K_DOWN: q10_ty -= 0.2
                    if event.key == pygame.K_z: q10_angle += 5
                    if event.key == pygame.K_x: q10_angle -= 5

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        # For Q2, use custom camera, otherwise use default
        if current_question == 2:
            gluLookAt(*q2_camera, *q2_look, *q2_up)
        else:
            gluLookAt(0, 2, 10, 0, 0, 0, 0, 1, 0)

        draw_question(current_question)

        pygame.display.set_caption(f"Computer Graphics Project - Question {current_question}")
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()