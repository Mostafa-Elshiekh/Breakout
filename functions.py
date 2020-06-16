from global_var import *
from classes import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame
import threading

pygame.mixer.init()

# initial position of the borders ,wall and ball
ball = RECTA(243, 243, 250, 250)  # initial position of the ball
wall = RECTA(0, 10, WINDOW_WIDTH, WINDOW_HEIGHT)
player = RECTA(240, 30, 260, 37)  # initial position of the bat
Rect1 = RECTA(490, 0, 500, 250)
Rect2 = RECTA(0, 0, 10, 250)
Rect3 = RECTA(0, 30, 10, 40)
Rect4 = RECTA(490, 30, 500, 40)
Rect5 = RECTA(490, 250, 500, 350)
Rect6 = RECTA(0, 250, 10, 350)
Rect7 = RECTA(490, 350, 500, 450)
Rect8 = RECTA(0, 350, 10, 450)
Rect9 = RECTA(490, 450, 500, 620)
Rect10 = RECTA(0, 450, 10, 600)
Rect11 = RECTA(0, 590, 590, 620)


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


def drawText(string, x, y):
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()  # remove the previous transformations
    # glScale(0.13,0.13,1)  # Try this line
    glTranslate(x, y, 0)  # try comment this line
    glScale(0.11, 0.11, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:  # render character by character starting from the origin
        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, c)


def Test_Ball_Wall(ball, wall):  # Collision Detection between Ball and Wall
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    if ball.right >= wall.right - 10:
        return FROM_RIGHT
    elif ball.left <= wall.left + 10:
        return FROM_LEFT
    elif ball.top >= wall.top - 10:
        return FROM_TOP
    elif ball.bottom <= wall.bottom:
        return FROM_BOTTOM
    else:
        return None


def Test_Ball_Player(ball, player):  # Collision Detection between Ball and Bat
    if ball.bottom <= player.top and \
            ball.left >= player.left and \
            ball.right <= player.right:
        return True
    return False


def Test_Ball_me(ball, me):  # Collision Detection between Ball and Bat
    count = 0
    for i in range(0, 120):
        count += 500
        if ball.left >= me[i].left and \
                ball.top >= me[i].bottom and \
                ball.right <= me[i].right and \
                ball.bottom <= me[i].top:
            me[i] = RectLevel(count, 0, 0, 0)
            return True
    return False


def MouseMotion(x, y):  # returns the mouse coordinates in "pixel"
    global mouse_x
    if x >= 90:
        mouse_x = x - 48


def Timer(t):
    Display()
    glutTimerFunc(time_interval, Timer, 1)


def move():
    for i in range(120):
        me[i].bottom -= 0.02
        me[i].top -= 0.02


def Display():
    global playerResult
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY

    glClear(GL_COLOR_BUFFER_BIT)

    string = "score : " + str(playerResult)
    drawText(string, 200, 10)

    ball.left = ball.left + deltaX  # updating ball's coordinates
    ball.right = ball.right + deltaX
    ball.top = ball.top + deltaY
    ball.bottom = ball.bottom + deltaY

    glColor(1, 1, 1)  # White color

    DrawRectangle(ball)
    if Test_Ball_Wall(ball, wall) == FROM_RIGHT:
        deltaX = -2
        pygame.mixer.Sound("./sounds/wall.wav").play()

    if Test_Ball_Wall(ball, wall) == FROM_LEFT:
        deltaX = 2
        pygame.mixer.Sound("./sounds/wall.wav").play()

    if Test_Ball_Wall(ball, wall) == FROM_TOP:
        deltaY = -2
        pygame.mixer.Sound("./sounds/wall.wav").play()

    if Test_Ball_Wall(ball, wall) == FROM_BOTTOM:
        deltaY = 2
        pygame.mixer.Sound("./sounds/wall.wav").play()
        playerResult = playerResult - 2

    player.left = mouse_x - 40  # remember that "mouse_x" is a global variable
    player.right = mouse_x + 40

    glColor(1, 1, 1)
    DrawRectangle(player)

    if Test_Ball_Player(ball, player):
        deltaY = -2
        pygame.mixer.Sound("./sounds/bat.wav").play()

    if Test_Ball_me(ball, me):
        deltaY = -2
        playerResult = playerResult + 1
        pygame.mixer.Sound("./sounds/brick.wav").play()

    # to draw the borders
    glColor(1, 1, 1)
    DrawRectangle(Rect1)
    DrawRectangle(Rect2)
    glColor(0, 0, 0)
    DrawRectangle(Rect3)
    DrawRectangle(Rect4)
    glColor(0.5, 0.1, 0)
    DrawRectangle(Rect5)
    DrawRectangle(Rect6)
    glColor(1, 0.5, 0)
    DrawRectangle(Rect7)
    DrawRectangle(Rect8)
    glColor(0, 0, 0.7)
    DrawRectangle(Rect9)
    DrawRectangle(Rect10)

    for i in range(240):  # to draw the all rect in levels
        glColor(1, 1, 0)
        DrawRectangle(me[i])
    threading.Timer(10, move).start()

    if Test_Ball_Player(ball, player):
        deltaY = 2
    glutSwapBuffers()
