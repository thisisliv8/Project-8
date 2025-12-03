'''
Livingston Assensoh
I drew a big house and a small house, two trees, a sun, and a sky full of stars. I placed them far apart as if they were on different streets.
'''
"""Import turtle graphics and math into python"""
import turtle
import math

"""Set up the turtle and scence settings"""
def setup_turtle():
    """Initialize turtle with standard settings"""
    screen = turtle.Screen()
    screen.title("Turtle Graphics Project 2")
    screen.bgcolor("CornflowerBlue")
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    return t, screen

"""Draw a rectangle used for house base and tree trunks"""
def draw_rectangle(t, width, height, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

"""Draw a triangle used for roofs"""
def draw_triangle(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()

"""Draw a circle used for the sun and  tree branches/leaves"""
def draw_circle(t, radius, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

"""Move turtle to locations without drawing lines"""
def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

"""Draw a tree with brown trunk and green leaves"""
def draw_tree(t, x, y):
    jump_to(t, x, y)
    t.color("saddle brown")
    t.begin_fill()
    draw_rectangle(t, 20, 40)
    t.end_fill()

    jump_to(t, x - 0, y + 1)
    t.color("forest green")
    t.begin_fill()
    draw_circle(t, 30)
    t.end_fill()

"""Draw the entire scene, house, stars, trees, and sun"""
def draw_scene(t):
    """Draw the full scene"""
    # Draw the sun
    jump_to(t, 250, 180)
    t.color("orange", "yellow")
    t.begin_fill()
    draw_circle(t, 40)
    t.end_fill()

    # Draw the big house
    jump_to(t, -100, -100)
    t.color("brown", "tan")
    t.begin_fill()
    draw_rectangle(t, 120, 100)
    t.end_fill()

    jump_to(t, -100, -100)
    t.color("dark red", "red")
    t.begin_fill()
    draw_triangle(t, 120)
    t.end_fill()

    # Draw the small house
    jump_to(t, 100, -50)
    t.color("sienna", "peach puff")
    t.begin_fill()
    draw_rectangle(t, 80, 60)
    t.end_fill()

    jump_to(t, 100, -50)
    t.color("maroon", "salmon")
    t.begin_fill()
    draw_triangle(t, 80)
    t.end_fill()

    # Draw the the two trees
    draw_tree(t, -180, -100)
    draw_tree(t, 220, -220)

    """ Draw the stars in the sky"""
    for x in range(-200, 200, 50):
        jump_to(t, x, 150)
        t.color("yellow", "yellow")
        t.begin_fill()
        for _ in range(5):
            t.forward(20)
            t.right(144)
        t.end_fill()

#Run the program 
if __name__ == "__main__":
    t, screen = setup_turtle()
    draw_scene(t)
    t.hideturtle()
    turtle.done()
