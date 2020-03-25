from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

red = [1.0, 0.0, 0.0]
orange = [1.0, 0.33, 0.0]
yellow = [1.0, 1.0, 0.0]
green = [0.0, 1.0, 0.0]
blue = [0.0, 0.0, 1.0]
indigo = [0.29, 0.0, 0.51]
violet = [0.56, 0.0, 1.0]

class Cube:
    def __init__(self, name):
        self.name = name

    def create(self):
        vertices = [[1.0, 1.0, -1.0],
                    [-1.0, 1.0,-1.0],
                    [-1.0, 1.0, 1.0],
                    [ 1.0, 1.0, 1.0],

                    [ 1.0,-1.0, 1.0],
                    [-1.0,-1.0, 1.0],
                    [-1.0,-1.0,-1.0],
                    [ 1.0,-1.0,-1.0],

                    [ 1.0, 1.0, 1.0],
                    [-1.0, 1.0, 1.0],
                    [-1.0,-1.0, 1.0],
                    [ 1.0,-1.0, 1.0],

                    [ 1.0,-1.0,-1.0],
                    [-1.0,-1.0,-1.0],
                    [-1.0, 1.0,-1.0],
                    [ 1.0, 1.0,-1.0],

                    [-1.0, 1.0, 1.0],
                    [-1.0, 1.0,-1.0],
                    [-1.0,-1.0,-1.0],
                    [-1.0,-1.0, 1.0],

                    [ 1.0, 1.0,-1.0],
                    [ 1.0, 1.0, 1.0],
                    [ 1.0,-1.0, 1.0],
                    [ 1.0,-1.0,-1.0]]

        colors = [red, orange, yellow, green, blue, violet]

        # Draw the Cube (multiple quads)
        glBegin(GL_QUADS)

        for quad in range(6):
            glColor3f(colors[quad][0], colors[quad][1], colors[quad][2])
            glVertex3f(vertices[quad * 4][0], vertices[quad * 4][1], vertices[quad * 4][2])
            glVertex3f(vertices[(quad * 4) + 1][0], vertices[(quad * 4) + 1][1], vertices[(quad * 4) + 1][2])
            glVertex3f(vertices[(quad * 4) + 2][0], vertices[(quad * 4) + 2][1], vertices[(quad * 4) + 2][2])
            glVertex3f(vertices[(quad * 4) + 3][0], vertices[(quad * 4) + 3][1], vertices[(quad * 4) + 3][2])

        glEnd()
