from OpenGL.GL import *
from OpenGL.GLUT import *
import random

w, h = 500, 500
pointlist = []
pointSpeed = 0.001  # Initial speed of points
freeze = False
blink = False
blink_interval_frames = 30
blink_counter = 0

# Background color
background_color = (0.0, 0.0, 0.0)

# generating random points with random colors
def generate_point(x, y):
    color = (random.random(), random.random(), random.random())  # Random RGB color
    direction_x = random.choice([-1, 1])
    direction_y = random.choice([-1, 1])
    pointlist.append({
        'x': x,
        'y': y,
        'dx': direction_x,
        'dy': direction_y,
        'color': color,
        'original_color': color,
        'blink_state': False
    })

# mouse clicks
def mouseListener(button, state, x, y):
    global freeze
    if not freeze:
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            x = (x / w - 0.5) * 2
            y = (0.5 - y / h) * 2
            generate_point(x, y)
        elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            toggle_blink()

def toggle_blink():
    global blink
    blink = not blink

# Function to update points positions and handle boundary conditions
def update_points():
    global pointSpeed, blink_counter, blink_interval_frames
    if not freeze:
        if blink:
            blink_counter += 1
            if blink_counter >= blink_interval_frames:
                blink_counter = 0
                for point in pointlist:
                    point['blink_state'] = not point['blink_state']
        for i in range(len(pointlist)):
            point = pointlist[i]
            x, y = point['x'], point['y']
            dx, dy = point['dx'], point['dy']
            color = point['color']
            original_color = point['original_color']
            blink_state = point['blink_state']

            # Update positions
            x += dx * pointSpeed
            y += dy * pointSpeed

            # Boundary conditions - bounce off the walls
            if x <= -1 or x >= 1:
                dx *= -1
            if y <= -1 or y >= 1:
                dy *= -1

            # blinking effect
            if blink and blink_state:
                color = background_color
            else:
                color = original_color

            # Update point properties
            pointlist[i] = {'x': x, 'y': y, 'dx': dx, 'dy': dy, 'color': color, 'original_color': original_color, 'blink_state': blink_state}


def draw_points():
    glPointSize(5)
    glBegin(GL_POINTS)
    for point in pointlist:
        glColor3f(*point['color'])
        glVertex2f(point['x'], point['y'])
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_points()
    glutSwapBuffers()
    update_points()
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global pointSpeed
    if key == GLUT_KEY_UP:
        pointSpeed *= 2  # Increase speed
    elif key == GLUT_KEY_DOWN:
        pointSpeed /= 2  # Decrease speed

def keyboard(key, x, y):
    global freeze
    if key == b' ':
        freeze = not freeze  # Freeze/unfreeze points

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(w, h)
glutCreateWindow(b"Random Blinking Points")

glClearColor(*background_color, 0.0)  # background color
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
glutDisplayFunc(display)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouseListener)
glutMainLoop()