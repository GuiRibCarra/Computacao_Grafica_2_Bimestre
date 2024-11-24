from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
from math import cos, sin

window_width, window_height = 800, 600
box_opening = False
box_lid_angle = 0
ball_position = [-0.5, -0.5]
child_position = -1.0
scene_stage = 0


def draw_box():
    # Caixa com tampa
    glColor3f(1, 0, 0)  # Vermelho
    glBegin(GL_QUADS)
    # Corpo da caixa
    glVertex3f(-0.3, -0.3, 0.0)
    glVertex3f(0.3, -0.3, 0.0)
    glVertex3f(0.3, 0.3, 0.0)
    glVertex3f(-0.3, 0.3, 0.0)
    glEnd()

    # Tampa da caixa
    glPushMatrix()
    glTranslatef(0, 0.3, 0)
    glRotatef(box_lid_angle, 1, 0, 0)
    glColor3f(0, 1, 0)  # Verde
    glBegin(GL_QUADS)
    glVertex3f(-0.3, 0.0, 0.0)
    glVertex3f(0.3, 0.0, 0.0)
    glVertex3f(0.3, 0.1, 0.0)
    glVertex3f(-0.3, 0.1, 0.0)
    glEnd()
    glPopMatrix()


def draw_ball():
    glColor3f(1, 1, 1)  # Branco
    glBegin(GL_POLYGON)
    for angle in range(0, 360, 10):
        x = ball_position[0] + 0.1 * cos(angle * 3.14159 / 180)
        y = ball_position[1] + 0.1 * sin(angle * 3.14159 / 180)
        glVertex2f(x, y)
    glEnd()

    glColor3f(0, 0, 0)  # Preto
    glBegin(GL_POLYGON)
    for angle in range(0, 360, 30):
        x = ball_position[0] + 0.05 * cos(angle * 3.14159 / 180)
        y = ball_position[1] + 0.05 * sin(angle * 3.14159 / 180)
        glVertex2f(x, y)
    glEnd()


def draw_child():
    glColor3f(0, 0, 1)  # Azul
    glBegin(GL_QUADS)
    glVertex3f(child_position - 0.1, -0.7, 0)
    glVertex3f(child_position + 0.1, -0.7, 0)
    glVertex3f(child_position + 0.1, -0.5, 0)
    glVertex3f(child_position - 0.1, -0.5, 0)
    glEnd()


def draw_field():
    glColor3f(0.3, 0.8, 0.3)  # Verde para o campo
    glBegin(GL_QUADS)
    glVertex3f(0.5, -0.8, 0)
    glVertex3f(1.0, -0.8, 0)
    glVertex3f(1.0, -0.4, 0)
    glVertex3f(0.5, -0.4, 0)
    glEnd()


def update_scene():
    global box_opening, box_lid_angle, ball_position, child_position, scene_stage

    if scene_stage == 0:  # Abrir a caixa
        if box_lid_angle < 90:
            box_lid_angle += 2
        else:
            scene_stage = 1
            time.sleep(0.5)

    elif scene_stage == 1:  # Bola saindo da caixa
        if ball_position[1] < 0:
            ball_position[1] += 0.02
        else:
            scene_stage = 2
            time.sleep(0.5)

    elif scene_stage == 2:  # Criança caminhando para o campo
        if child_position < 0.7:
            child_position += 0.01
            ball_position[0] = child_position
        else:
            scene_stage = 3  # Final da animação

    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    if scene_stage < 3:
        draw_box()
        if scene_stage >= 1:
            draw_ball()
        if scene_stage >= 2:
            draw_child()
    else:
        draw_field()
        draw_child()

    glutSwapBuffers()


def main():
    global window_width, window_height
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Presente e Campo")
    glClearColor(0, 0, 0, 1)
    glutDisplayFunc(display)
    glutIdleFunc(update_scene)
    glutMainLoop()


if __name__ == "__main__":
    main()