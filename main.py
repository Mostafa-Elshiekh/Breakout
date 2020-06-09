from functions import*
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#from playsound import playsound
import threading

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    # mouse coordinates inbetween [WINDOW_WIDTH=800,WINDOW_HEIGHT=500]
    # glutInitWindowSize (1100, 600) # try and notice the bat; mouse coordinates inbetween [1100,600] (where 1100 pixels = 800 in openGL)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Simple Ball Bat OpenGL game")
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutPassiveMotionFunc(MouseMotion)
    #glutWireSphere(100,10,10)
    #glColor3f(0,1,1)

    init()
    glutMainLoop()


main()