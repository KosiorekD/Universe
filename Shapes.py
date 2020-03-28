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

colors = [red, orange, yellow, green, blue, violet]

class Cube:
    def __init__(self, name, xScale, yScale, zScale):
        self.name = name

        self.xScale = xScale
        self.yScale = yScale
        self.zScale = zScale

        self.xPos = 0
        self.yPos = 0
        self.zPos = 0

    def create(self):
        cubeVertices = (( 1.0 * self.xScale, 1.0 * self.yScale, 1.0 * self.zScale),
                        ( 1.0 * self.xScale, 1.0 * self.yScale,-1.0 * self.zScale),
                        ( 1.0 * self.xScale,-1.0 * self.yScale,-1.0 * self.zScale),
                        ( 1.0 * self.xScale,-1.0 * self.yScale, 1.0 * self.zScale),
                        (-1.0 * self.xScale, 1.0 * self.yScale, 1.0 * self.zScale),
                        (-1.0 * self.xScale,-1.0 * self.yScale,-1.0 * self.zScale),
                        (-1.0 * self.xScale,-1.0 * self.yScale, 1.0 * self.zScale),
                        (-1.0 * self.xScale, 1.0 * self.yScale,-1.0 * self.zScale))

        cubeEdges = ((0, 1),
                     (0, 3),
                     (0, 4),
                     (1, 2),
                     (1, 7),
                     (2, 5),
                     (2, 3),
                     (3, 6),
                     (4, 6),
                     (4, 7),
                     (5, 6),
                     (5, 7))

        cubeQuads = ((0, 3, 6, 4),
                     (2, 5, 6, 3),
                     (1, 2, 5, 7),
                     (1, 0, 4, 7),
                     (7, 4, 6, 5),
                     (2, 3, 0, 1))

        # Draw the Cube
        glBegin(GL_QUADS)
        for cubeQuad in cubeQuads:
            glColor3f(colors[1][0], colors[1][1], colors[1][2])
            for cubeVertex in cubeQuad:
                glVertex3fv(cubeVertices[cubeVertex])
        glEnd()

class Sphere:
    def __init__(self, name, scale):
        self.name = name
        self.scale = scale

        self.xPos = 0
        self.yPos = 0
        self.zPos = 0

    def create(self):
        glColor3f(colors[0][0], colors[0][1], colors[0][2])
        glutSolidSphere(self.scale, 16, 16)
