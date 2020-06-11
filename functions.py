from global_var import*
from classes import*
from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame
import threading

pygame.mixer.init()


# initial position of the borders ,wall and ball
ball = RECTA(50, 50, 65, 65)  # initial position of the ball
wall = RECTA(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
player = RECTA(100, 30, 80, 40)  # initial position of the bat
#me=RECTA(435,444,475,460)
Rect1 = RECTA(485,0 ,596, 250)
Rect2 = RECTA(5,0 ,20, 250)
Rect3 = RECTA(5,30,20, 40)
Rect4 = RECTA(485,30,596,40)
Rect5= RECTA(485,250 ,596, 350)
Rect6= RECTA(5,250 ,20, 350)
Rect7 = RECTA(485,350 ,596, 450)
Rect8 = RECTA(5,350 ,20, 450)
Rect9 = RECTA(485,450 ,596, 620)
Rect10 = RECTA(5,450,20,620)
Rect11 = RECTA(5,585,596, 620)



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


def Test_Ball_Brick(ball, me):  # Collision Detection between Ball and Brick
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM

def brickRemove(bricklist, bricknum):
    bricklist.pop(bricknum)


def Test_Ball_Player(ball, player):  # Collision Detection between Ball and Bat
    if ball.bottom <= player.top and ball.left >= player.left and ball.right <= player.right:
        return True
    return False

flag=False
def Test_Ball_me(ball, me):  # Collision Detection between Ball and Bat
    #global me
    #global flag
    count=0
    for i in range(0,40):
        count=count+500
        if ball.left >= me[i].left and ball.top >= me[i].bottom and ball.right >= me[i].right and ball.bottom<=me[i].top:
            #numbers=1
            me[i]=RectLevel(count,0,0,0)
            #flag=True
            return True
        #else:
            #numbers=0
    #flag=False
    return False



mouse_x = 0


def MouseMotion(x, y):  # returns the mouse coordinates in "pixel"
    global mouse_x
    if x >= 90:
        mouse_x = x - 48



def Timer(t):
    Display()
    glutTimerFunc( time_interval, Timer, 1 )


playerResult = 0
def Display():
    global playerResult
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY

    glClear(GL_COLOR_BUFFER_BIT)

    string = "score :  " + str(playerResult)
    drawText(string, 200, 10)

    ball.left = ball.left + deltaX  # updating ball's coordinates
    ball.right = ball.right + deltaX
    ball.top = ball.top + deltaY
    ball.bottom = ball.bottom + deltaY

    glColor(1, 1, 1)  # White color

    DrawRectangle(ball)
    if Test_Ball_Wall(ball, wall) == FROM_RIGHT:
        deltaX = -1
        pygame.mixer.Sound("./sounds/wall.wav").play()

    if Test_Ball_Wall(ball, wall) == FROM_LEFT:
        deltaX = 1
        pygame.mixer.Sound("./sounds/wall.wav").play()

    if Test_Ball_Wall(ball, wall) == FROM_TOP:
        deltaY = -1
        pygame.mixer.Sound("./sounds/wall.wav").play()

    if Test_Ball_Wall(ball, wall) == FROM_BOTTOM:
        deltaY = 1
        pygame.mixer.Sound("./sounds/wall.wav").play()



    player.left = mouse_x - 30  # remember that "mouse_x" is a global variable
    player.right = mouse_x + 30

    glColor(0, 0.5, 0)
    glColor(1, 1, 1)
    DrawRectangle(player)

    if Test_Ball_Player(ball, player):
        deltaY = 1
        pygame.mixer.Sound("./sounds/bat.wav").play()

    if Test_Ball_me(ball,me):
        deltaY=-1
        playerResult=playerResult+1
        pygame.mixer.Sound("./sounds/brick.wav").play()


    # to draw the borders
    glColor(1, 1, 1)
    DrawRectangle(Rect1)
    DrawRectangle(Rect2)
    glColor(0, 0, 1)
    DrawRectangle(Rect3)
    DrawRectangle(Rect4)

    glColor(0.5, 0.1, 0)
    DrawRectangle(Rect5)
    DrawRectangle(Rect6)
    glColor(1, 0.5, 0)
    DrawRectangle(Rect7)
    DrawRectangle(Rect8)
    glColor(0, 0.1, 1)
    DrawRectangle(Rect9)
    DrawRectangle(Rect10)
    glColor(0, 0, 1)
    DrawRectangle(Rect11)


    for i in range(0,40) :  # to draw the all rect in levels
        glColor(1, 1, 0)
        DrawRectangle(me[i])


    '''for i in range(0,10):
        if flag==False:
            glColor(1, 1, 0)
            DrawRectangle(me[i])'''




    if Test_Ball_Player(ball, player) == True:
        deltaY = 1
    glutSwapBuffers()
