from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

deltaX = 1
deltaY = 1

time_interval = 10  # try  1000 msec

class RectLevel:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

    # creating list
new=[]  #list from class

for i in range (0,10):
    new.append(RectLevel(0,380,60,395))
for j in range (10,20):
    new.append(RectLevel(0,418,66,434))

for K in range (20,30):
    new.append(RectLevel(0,418,66,434))


# Any function it name is levels ..it Determined the size of rect
def levels():
    count = 10 #A counter that works as a step to separate each rectangle and another
    for i in range(0, 10):
        new[i].left = 60 + count
        new[i].right = 20 + count
        count = count + 45

def levels1():

      count=10
      for j in range(10,20):
           new[j].left=60+count
           new[j].right=20+count
           count=count+45


def levels2():
    count = 10
    for k in range(20, 30):
        new[k].left = 60 + count
        new[k].right = 20 + count
        count = count + 45


'''def block(left, bottom, right, top):
    glLoadIdentity()
    glBegin(GL_QUADS)
    count=10
    for i in range (0,2):
        glVertex(left[i]-count, bottom, 0)  # Left - Bottom
        glVertex(right[i]+count, bottom, 0)
        glVertex(right[i]+count, top, 0)
        glVertex(left[i]-count, top, 0)
        count
    glEnd()'''

#class to define attributes for Bat and boll
class RECTA:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


#initial position of the borders ,wall and ball
ball = RECTA(100, 100, 120, 120)  # initial position of the ball
wall = RECTA(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
player = RECTA(100,30,80,40)  # initial position of the bat
RectLeftDown=RECTA(0,300,100,0)  # initial position of the bat
RectRightDown=RECTA(0,300,95,0)
Rect1=RECTA(0,42,95,30)
Rect2=RECTA(0,42,95,30)
Rect3=RECTA(0,592,100,500)
Rect4=RECTA(0,592,100,500)
Rect5=RECTA(0, 595,0,582)
Rect6=RECTA(0,400,100,500)
Rect7=RECTA(0,300,100,400)
Rect8=RECTA(0,400,100,500)
Rect9=RECTA(0,400,100,300)

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

#def levels():
        #List[0].append(RectLevel(0,100,100,300))
        #List.left = 30  # remember that "mouse_x" is a global variable
        #List.right = 30
        #glColor(1, 0, 0)
        #DrawRectangle(List)




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

    # print(ball.right)

    if ball.right >= wall.right-12:
        return FROM_RIGHT
    if ball.left <= wall.left+12:
        return FROM_LEFT
    if ball.top >= wall.top-12:
        return FROM_TOP
    if ball.bottom <= wall.bottom:
        return FROM_BOTTOM

    # Otherwise this function returns None


def Test_Ball_Player(ball, player):  # Collision Detection between Ball and Bat
    if ball.bottom <= player.top and ball.left >= player.left and ball.right <= player.right:
        return True
    return False


# Key Board Messages
def keyboard(key, x, y):
    if key == b"q":
        sys.exit(0)


mouse_x = 0

def MouseMotion(x, y):  # returns the mouse coordinates in "pixel"
    global mouse_x
    if x>=90:
      mouse_x = x-48


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

    #string = "PC : " + str(pcResult)
    #drawText(string, 100, 10)
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

    if Test_Ball_Wall(ball, wall) == FROM_LEFT:
        deltaX = 1

    if Test_Ball_Wall(ball, wall) == FROM_TOP:
        deltaY = -1

    if Test_Ball_Wall(ball, wall) == FROM_BOTTOM:
        deltaY = 1
        pcResult = pcResult + 1

    player.left= mouse_x - 30  # remember that "mouse_x" is a global variable
    player.right = mouse_x + 30


    borders()
    levels()
    levels1()
    levels2()
    glColor(0, 0.5, 0)
    #block(200,400,250,420)
    #block(320,400,270,420)

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
    glColor(0, 1, 0)

    for i in range (0,10):   # to draw the first level
        DrawRectangle(new[i])

    for j in range (10,20):  # to draw the second level
        DrawRectangle(new[j])

    for k in range(20, 30):
        DrawRectangle(new[k])













    if Test_Ball_Player(ball, player) == True:
        deltaY = 1
        playerResult = playerResult + 1

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    # mouse coordinates inbetween [WINDOW_WIDTH=800,WINDOW_HEIGHT=500]
    # glutInitWindowSize (1100, 600) # try and notice the bat; mouse coordinates inbetween [1100,600] (where 1100 pixels = 800 in openGL)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Simple Ball Bat OpenGL game");
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(MouseMotion)
    #glutWireSphere(100,10,10)
    #glColor3f(0,1,1)

    init()
    glutMainLoop()


main()