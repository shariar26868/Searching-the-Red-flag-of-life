import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

player_x, player_y = 1, 1  
score = 0  
power_ups = [(1, 3), (7, 7), (12, 8), (3, 3), (10, 3), (6, 12)]
window_width = 800
window_height = 800
game_over = False  
def draw_circle(x, y, radius, num_segments=50):
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        angle = 2 * math.pi * i / num_segments
        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)
        glVertex2f(x + dx, y + dy)
    glEnd()

def midpoint_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        glVertex2f(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def draw_maze():
    global game_over
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  
    rows = len(maze)
    cols = len(maze[0])
    cell_width = 2.0 / cols
    cell_height = 2.0 / rows
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1: 
                x1 = -1 + j * cell_width
                y1 = 1 - i * cell_height
                x2 = x1 + cell_width
                y2 = y1 - cell_height
                glBegin(GL_QUADS)  
                glVertex2f(x1, y1)
                glVertex2f(x2, y1)
                glVertex2f(x2, y2)
                glVertex2f(x1, y2)
                glEnd()
    start_x = 1  
    start_y = 1
    if maze[start_y][start_x] == 0:
        x1 = -1 + start_x * cell_width
        y1 = 1 - start_y * cell_height
        x2 = x1 + cell_width
        y2 = y1 - cell_height
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(x1, y1)
        glVertex2f(x2, y1)
        glVertex2f(x2, y2)
        glVertex2f(x1, y2)
        glEnd()
    end_x = 14  
    end_y = 10
    if maze[end_y][end_x] == 0:
        x1 = -1 + end_x * cell_width
        y1 = 1 - end_y * cell_height
        x2 = x1 + cell_width
        y2 = y1 - cell_height
        glColor3f(1.0, 0.0, 0.0)  
        glBegin(GL_QUADS)
        glVertex2f(x1, y1)
        glVertex2f(x2, y1)
        glVertex2f(x2, y2)
        glVertex2f(x1, y2)
        glEnd()
    center_x = -1 + player_x * cell_width + cell_width / 2
    center_y = 1 - player_y * cell_height - cell_height / 2
    player_radius = min(cell_width, cell_height) / 4  
    glColor3f(0.0, 0.0, 1.0)  
    draw_circle(center_x, center_y, player_radius)
    glColor3f(1.0, 1.0, 0.0)  
    for px, py in power_ups:
        power_up_center_x = -1 + px * cell_width + cell_width / 2
        power_up_center_y = 1 - py * cell_height - cell_height / 2
        power_up_radius = min(cell_width, cell_height) / 6
        draw_circle(power_up_center_x, power_up_center_y, power_up_radius)
    if game_over:
        display_game_over()
    glFlush()

def display_game_over():
    glColor3f(1.0, 0.0, 0.0)
    glRasterPos2f(-0.2, 0)  
    glPushMatrix()
    glScalef(10.0, 10.0, 1.0)  
    for char in "Game Over!":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))  
    glPopMatrix()  
    glutPostRedisplay()

def setup():
    glClearColor(1.0, 1.0, 1.0, 1.0) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def keyboard(key, x, y):
    global player_x, player_y, score, power_ups, game_over
    end_x, end_y = 14, 10  
    if game_over:  
        if key == b'q' or key == b'Q':  
            print("Game window closed.")
            glutLeaveMainLoop()
            return
        elif key == b'r' or key == b'R':  
            print("Game restarted.")
            reset_game()
            glutPostRedisplay()
        return
    if key == b'q' or key == b'Q':  
        print("Game window closed.")
        glutLeaveMainLoop()
        return
    elif key == b'r' or key == b'R':  
        print("Game restarted.")
        reset_game()
        glutPostRedisplay()
        return  
    new_x, new_y = player_x, player_y
    if key == b'w': 
        new_y -= 1
    elif key == b's': 
        new_y += 1
    elif key == b'a':  
        new_x -= 1
    elif key == b'd':  
        new_x += 1
    if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] == 0:
        player_x, player_y = new_x, new_y
        score += 1
        print(f"Steps taken: {score}")  
    if (player_x, player_y) in power_ups:
        power_ups.remove((player_x, player_y))
        score += 10  
        print("Power-up collected! Score:", score)
    if (player_x == end_x and player_y == end_y):
        print("You've reached the end! Game over! Thank you")
        print(f"Your Total Score is: {score}")  
        game_over = True  
        glutTimerFunc(2000, reset_game_after_delay, 0)  
    glutPostRedisplay()

def reset_game_after_delay(value):
    reset_game()
    glutPostRedisplay()

def reset_game():
    global player_x, player_y, score, power_ups, game_over
    player_x, player_y = 1, 1  
    score = 0
    power_ups = [(1, 3), (7, 7), (12, 8), (3, 3), (10, 3), (6, 12)]
    game_over = False

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Searching the Red flag of life")
    setup()
    glutDisplayFunc(draw_maze)
    glutKeyboardFunc(keyboard)  
    glutMainLoop()

if __name__ == "__main__":
    main()
