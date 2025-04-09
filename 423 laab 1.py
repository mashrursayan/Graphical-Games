from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window dimensions
W_WIDTH, W_HEIGHT = 800, 600

# Global variables
raindrops = []
rain_bend = 0.0
background_brightness = 1.0
class point:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0

def create_raindrops():
    """Initialize raindrops at random positions."""
    global raindrops
    raindrops = [[random.uniform(-1, 1), random.uniform(0, 2)] for _ in range(100)]

def update_raindrops():
    """Update the position of raindrops."""
    for drop in raindrops:
        drop[1] -= 0.02  # Move down
        drop[0] += rain_bend * 0.01  # Bend to the side
        if drop[1] < -1:  # Reset position when off-screen
            drop[1] = random.uniform(1, 2)
            drop[0] = random.uniform(-1, 1)

def draw_house():
    """Draw the house using GL_LINES and GL_TRIANGLES."""
    # Roof
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.5, 0.0)  # Orange
    glVertex2f(-0.5, 0.0)
    glVertex2f(0.5, 0.0)
    glVertex2f(0.0, 0.5)
    glEnd()

    # Walls
    glBegin(GL_LINES)
    glColor3f(0.8, 0.6, 0.4)  # Brown
    glVertex2f(-0.5, 0.0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, 0.0)
    glVertex2f(0.5, -0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

    # Door
    glBegin(GL_LINES)
    glColor3f(0.4, 0.2, 0.0)  # Dark brown
    glVertex2f(-0.1, -0.5)
    glVertex2f(-0.1, -0.2)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.1, -0.2)
    glVertex2f(-0.1, -0.2)
    glVertex2f(0.1, -0.2)
    glEnd()

def draw_raindrops():
    """Draw raindrops using GL_POINTS."""
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(0.2, 0.2, 1.0)  # Blue
    for drop in raindrops:
        glVertex2f(drop[0], drop[1])
    glEnd()

def handle_keys(key, x, y):
    """Handle key presses for day-night transition."""
    global background_brightness
    if key == b'n':  # Night
        background_brightness = max(0.0, background_brightness - 0.05)
    elif key == b'm':  # Day
        background_brightness = min(1.0, background_brightness + 0.05)

def special_keys(key, x, y):
    """Handle special keys for rain direction."""
    global rain_bend
    if key == GLUT_KEY_LEFT:  # Bend left
        rain_bend = max(rain_bend - 0.01, -0.5)
    elif key == GLUT_KEY_RIGHT:  # Bend right
        rain_bend = min(rain_bend + 0.01, 0.5)

def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(background_brightness, background_brightness, background_brightness, 1.0)
    draw_house()
    draw_raindrops()
    glutSwapBuffers()

def timer(value):
    """Animation timer."""
    update_raindrops()
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)  # 60 FPS

def init():
    """Initialize OpenGL settings."""
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Default to white background
    gluOrtho2D(-1, 1, -1, 1)  # Set up orthographic projection
def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    drawAxes()
    global ballx, bally, ball_size
    draw_points(ballx, bally, ball_size)
    drawShapes()

    glBegin(GL_LINES)
    glVertex2d(180,0)
    glVertex2d(180,180)
    glVertex2d(180,180)
    glVertex2d(0,180)
    glEnd()

    if(create_new):
        m,n = create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m,n)
        glEnd()


    glutSwapBuffers()


def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global ballx, bally,speed
    ballx=(ballx+speed)%180
    bally=(bally+speed)%180
def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()	

