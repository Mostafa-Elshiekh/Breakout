from global_var import*
from classes import*
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from playsound import playsound
import threading
import time


def Sound_thread(filename):
    playsound(filename)


FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

deltaX = 1
deltaY = 1

time_interval = 5  # try  1000 msec


class RectLevel:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

    # creating list


new = []

count_y = 30  # counter to shift the rect to the higher level in y axis
count_x = 0  # counter to shift the rect to the second rect in x axis(At the same level(

for k in range(0, 4):
    for j in range(0, 10):
        new.append(RectLevel(435 - count_x, 444 + count_y, 475 - count_x, 460 + count_y))
        count_x += 45

    count_y += 30  # increment y to go higher level
    count_x = 0  # make it 0 to return to the start of level


# class to define attributes for Bat and boll
class RECTA:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


# initial position of the borders ,wall and ball
ball = RECTA(50, 50, 65, 65)  # initial position of the ball
wall = RECTA(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
player = RECTA(100, 30, 80, 40)  # initial position of the bat
RectLeftDown = RECTA(0, 300, 100, 0)  # initial position of the bat
RectRightDown = RECTA(0, 300, 95, 0)
Rect1 = RECTA(0, 42, 95, 30)
Rect2 = RECTA(0, 42, 95, 30)
Rect3 = RECTA(0, 592, 100, 500)
Rect4 = RECTA(0, 592, 100, 500)
Rect5 = RECTA(0, 595, 0, 582)
Rect6 = RECTA(0, 400, 100, 500)
Rect7 = RECTA(0, 300, 100, 400)
Rect8 = RECTA(0, 400, 100, 500)
Rect9 = RECTA(0, 400, 100, 300)


# Initialization
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)  # l,r,b,t,n,f

    glMatrixMode(GL_MODELVIEW)


def DrawRectangle(rect):
    glLoadIdentity()
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()


def borders():
    player.left = mouse_x - 30  # remember that "mouse_x" is a global variable
    player.right = mouse_x + 30

    RectLeftDown.left = 5  # remember that "mouse_x" is a global variable
    RectLeftDown.right = 18

    RectRightDown.left = 482  # remember that "mouse_x" is a global variable
    RectRightDown.right = 495

    Rect2.left = 482  # remember that "mouse_x" is a global variable
    Rect2.right = 495

    Rect1.left = 5  # remember that "mouse_x" is a global variable
    Rect1.right = 18

    Rect3.left = 482  # remember that "mouse_x" is a global variable
    Rect3.right = 495

    Rect4.left = 5  # remember that "mouse_x" is a global variable
    Rect4.right = 18

    Rect5.left = 5  # remember that "mouse_x" is a global variable
    Rect5.right = 495

    Rect6.left = 5  # remember that "mouse_x" is a global variable
    Rect6.right = 18

    Rect7.left = 5  # remember that "mouse_x" is a global variable
    Rect7.right = 18

    Rect8.left = 495  # remember that "mouse_x" is a global variable
    Rect8.right = 482

    Rect9.left = 495  # remember that "mouse_x" is a global variable
    Rect9.right = 482


def drawText(string, x, y):
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()  # remove the previous transformations
    #       glScale(0.13,0.13,1)  # Try this line
    glTranslate(x, y, 0)  # try comment this line
    glScale(0.13, 0.13, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:  # render character by character starting from the origin
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)


def Test_Ball_Wall(ball, wall):  # Collision Detection between Ball and Wall
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM

    if ball.right >= wall.right - 12:
        return FROM_RIGHT
    if ball.left <= wall.left + 12:
        return FROM_LEFT
    if ball.top >= wall.top - 12:
        return FROM_TOP
    if ball.bottom <= wall.bottom:
        return FROM_BOTTOM

    # Otherwise this function returns None


def Test_Ball_Brick(ball, new):  # Collision Detection between Ball and Brick
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM

    for k in range(0, 4):
        for j in range(0, 10):
            if ball.top >= new[j].bottom:
                return FROM_TOP
            '''
            if ball.right >= new[j].right :
                return FROM_RIGHT
            if ball.left >= new[j].left:
                return FROM_LEFT
            if ball.bottom <= new[j].bottom:
                return FROM_BOTTOM
            '''


def brickRemove(bricklist, bricknum):
    bricklist.pop(bricknum)


def Test_Ball_Player(ball, player):  # Collision Detection between Ball and Bat
    if ball.bottom <= player.top and ball.left >= player.left and ball.right <= player.right:
        return True
    return False


mouse_x = 0


def MouseMotion(x, y):  # returns the mouse coordinates in "pixel"
    global mouse_x
    if x >= 90:
        mouse_x = x - 48


def Timer(v):
    Display()

    glutTimerFunc(time_interval, Timer, 1)


pcResult = 0
playerResult = 0


def Display():
    global pcResult
    global playerResult
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY

    glClear(GL_COLOR_BUFFER_BIT)

    # string = "PC : " + str(pcResult)
    # drawText(string, 100, 10)
    string = "Player :  " + str(playerResult)
    drawText(string, 200, 10)

    ball.left = ball.left + deltaX  # updating ball's coordinates
    ball.right = ball.right + deltaX
    ball.top = ball.top + deltaY
    ball.bottom = ball.bottom + deltaY

    glColor(1, 1, 1)  # White color

    DrawRectangle(ball)

    if Test_Ball_Wall(ball, wall) == FROM_RIGHT:
        deltaX = -1
        x = threading.Thread(target=Sound_thread, args=("./sounds/wall.mp3",))
        x.start()

    if Test_Ball_Wall(ball, wall) == FROM_LEFT:
        deltaX = 1
        x = threading.Thread(target=Sound_thread, args=("./sounds/wall.mp3",))
        x.start()

    if Test_Ball_Wall(ball, wall) == FROM_TOP:
        deltaY = -1
        x = threading.Thread(target=Sound_thread, args=("./sounds/wall.mp3",))
        x.start()

    if Test_Ball_Wall(ball, wall) == FROM_BOTTOM:
        deltaY = 1
        x = threading.Thread(target=Sound_thread, args=("./sounds/wall.mp3",))
        x.start()

    if Test_Ball_Brick(ball, new) == FROM_TOP:
        deltaY = -1
        x = threading.Thread(target=Sound_thread, args=("./sounds/brick.mp3",))
        x.start()
        playerResult = playerResult + 1
        brickRemove(new, BrickNum)

    # Some possibilities if the ball passed from any space left and hit the bricks from above or from sides

    '''
    if Test_Ball_Brick(ball,new) == FROM_BOTTOM : 
        deltaY = 1
        x = threading.Thread(target=Sound_thread , args=("./sounds/brick.mp3",)) 
        x.start()
        playerResult = playerResult + 1
    if Test_Ball_Brick(ball,new) == FROM_LEFT : 
        deltaX = 1
        x = threading.Thread(target=Sound_thread , args=("./sounds/brick.mp3",)) 
        x.start()
        playerResult = playerResult + 1
    if Test_Ball_Brick(ball,new) == FROM_RIGHT : 
        deltaX = -1
        x = threading.Thread(target=Sound_thread , args=("./sounds/brick.mp3",)) 
        x.start()
        playerResult = playerResult + 1
    '''

    player.left = mouse_x - 30  # remember that "mouse_x" is a global variable
    player.right = mouse_x + 30

    borders()
    glColor(0, 0.5, 0)
    glColor(1, 1, 1)
    DrawRectangle(player)

    # to draw the borders
    DrawRectangle(RectLeftDown)
    DrawRectangle(RectRightDown)
    glColor(0, 0, 1)
    DrawRectangle(Rect1)
    DrawRectangle(Rect2)
    DrawRectangle(Rect3)
    DrawRectangle(Rect4)
    DrawRectangle(Rect5)
    glColor(1, 0.5, 0)
    DrawRectangle(Rect6)
    glColor(0.5, 0.5, 0)
    DrawRectangle(Rect7)
    glColor(1, 0.5, 0)
    DrawRectangle(Rect8)
    glColor(0.5, 0.5, 0)
    DrawRectangle(Rect9)
    glColor(0.5, 0.8, 0)

    for i in range(0, 40):  # to draw the all rect in levels
        DrawRectangle(new[i])

    if Test_Ball_Player(ball, player) == True:
        deltaY = 1
        x = threading.Thread(target=Sound_thread, args=("./sounds/bat.mp3",))
        x.start()

    glutSwapBuffers()
