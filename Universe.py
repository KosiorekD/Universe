from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Shapes import *

isWireframeEnabled = False

ESCAPE = b'\x1b'
ENABLE_WIREFRAME = b'u'

TestCube = Cube("Test Cube", 1, 1, 1)
Sun = Sphere("Sun", 1.0)

def keyPressed(*args):
    global isWireframeEnabled

    if args[0] == ENABLE_WIREFRAME and isWireframeEnabled == True:
        isWireframeEnabled = False
        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_FILL)
    elif args[0] == ENABLE_WIREFRAME and isWireframeEnabled == False:
        isWireframeEnabled = True
        glPolygonMode(GL_FRONT, GL_LINE)
        glPolygonMode(GL_BACK, GL_LINE)

    if args[0] == ESCAPE:
        sys.exit()

def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def alterObject(object, xDirection, yDirection, zDirection, xRotation, yRotation, zRotation):
    glPushMatrix()

    glTranslatef(xDirection, yDirection, zDirection)

    glRotatef(xRotation, 1.0, 0.0, 0.0)
    glRotatef(yRotation, 0.0, 1.0, 0.0)
    glRotatef(zRotation, 0.0, 0.0, 1.0)

    object.create()

    glPopMatrix()

def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)

    #----------This is where objects in the scene are created/altered----------#
    alterObject(TestCube, 0.0, 0.0, 0.0, 0.00, 0.00, 45.00)
    alterObject(Sun, 0.0, 0.0, 0.0, 0.00, 0.00, 0.00)
    #--------------------------------------------------------------------------#

    glutSwapBuffers()

def main():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(200,200)

    window = glutCreateWindow("Universe")

    glutDisplayFunc(drawScene)
    glutIdleFunc(drawScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)

    glutMainLoop()

if __name__ == "__main__":
    main()
