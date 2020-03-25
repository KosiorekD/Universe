from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

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

        colors = [[1.0, 0.0, 0.0],
                  [1.0, 1.0, 0.0],
                  [0.0, 0.0, 1.0],
                  [0.0, 1.0, 1.0],
                  [1.0, 1.0, 1.0],
                  [0.0, 1.0, 0.0]]

        # Draw the Cube (multiple quads)
        glBegin(GL_QUADS)

        for side in range(6):
            glColor3f(colors[side][0], colors[side][1], colors[side][2])
            glVertex3f(vertices[side * 4][0], vertices[side * 4][1], vertices[side * 4][2])
            glVertex3f(vertices[(side * 4) + 1][0], vertices[(side * 4) + 1][1], vertices[(side * 4) + 1][2])
            glVertex3f(vertices[(side * 4) + 2][0], vertices[(side * 4) + 2][1], vertices[(side * 4) + 2][2])
            glVertex3f(vertices[(side * 4) + 3][0], vertices[(side * 4) + 3][1], vertices[(side * 4) + 3][2])

        glEnd()
