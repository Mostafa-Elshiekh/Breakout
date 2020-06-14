from functions import *
from OpenGL.GLUT import *
from global_var import *


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowSize(500, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Super Breakout")
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutPassiveMotionFunc(MouseMotion)

    init()
    glutMainLoop()


main()
