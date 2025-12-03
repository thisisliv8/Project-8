# ...existing code...
'''
Livingston Assensoh
I refactored my code and increased it from two houses to eight houses, from two trees to three, a sun, added a moon, and a sky full of stars. I placed them far apart as if they were on different streets.
'''
"""Import turtle graphics and math into python"""
import turtle
import math

"""Set up the turtle and scene settings"""
def setup_turtle():
    """Initialize turtle with standard settings"""
    screen = turtle.Screen()
    screen.title("Turtle Graphics Project 2")
    screen.bgcolor("CornflowerBlue")
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    return t, screen

def jump_to(t, x, y):
    """Move turtle to location without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_rectangle(t, width, height):
    """Draw a rectangle from current position (lower-left corner)"""
    t.setheading(0)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_triangle(t, width):
    """Draw an equilateral triangle with base = width (base along current heading)"""
    t.setheading(0)
    for _ in range(3):
        t.forward(width)
        t.left(120)

def draw_star(t, x, y, size):
    """Draw a 5-point star at (x, y)"""
    jump_to(t, x, y)
    t.setheading(0)
    t.color("yellow", "yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_tree(t, x, y, trunk_w=20, trunk_h=40, canopy_r=30):
    """Draw a tree whose trunk lower-left corner is at (x,y).
    The circular canopy is centered above the trunk so it sits on top."""
    # Draw trunk (lower-left at x,y)
    jump_to(t, x, y)
    t.setheading(0)
    t.color("saddlebrown", "saddlebrown")
    t.begin_fill()
    draw_rectangle(t, trunk_w, trunk_h)
    t.end_fill()

    # Compute canopy center so it is horizontally centered above trunk
    cx = x + trunk_w / 2
    cy = y + trunk_h + canopy_r  # center y for the canopy

    # Move to the point where turtle.circle will draw a circle centered at (cx, cy)
    jump_to(t, cx, cy - canopy_r)
    t.setheading(0)
    t.color("forestgreen", "forestgreen")
    t.begin_fill()
    t.circle(canopy_r)
    t.end_fill()



"""Draw a rectangle used for house base and tree trunks"""
def draw_house(t, x, y, width, height, fill_color, roof_color):
# Draw base (assumes (x,y) is lower-left corner)
    jump_to(t, x, y)
    t.setheading(0)
    t.color("black", fill_color)
    t.begin_fill()
    draw_rectangle(t, width, height)
    t.end_fill()

 # Draw roof: start at top-left corner of base so base of triangle matches rectangle
    jump_to(t, x, y + height)
    t.setheading(0)
    t.color("black", roof_color)
    t.begin_fill()
    draw_triangle(t, width)
    t.end_fill()

def draw_sun(t, x, y):
    jump_to(t, x, y)
    t.setheading(0)
    t.color("orange", "yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

def draw_moon(t, x, y):
    jump_to(t, x, y)
    t.setheading(0)
    t.color("lightgray", "lightgray")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def draw_all_trees(t):
    draw_tree(t, -320, -100)
    draw_tree(t, 120, -130)
    draw_tree(t, 480, -120)

def draw_star_field(t):
    for x in range(-200, 200, 25):
        draw_star(t, x, 150, 12)

def draw_scene(t):
    # sky objects
    draw_sun(t, 300, 300)
    draw_moon(t, -300, 180)
    draw_star_field(t)

    
# houses (use valid color names without spaces)
    draw_house(t, -600, -90, 90, 70, "burlywood", "sienna")
    draw_house(t, -400, -90, 90, 70, "khaki", "maroon")
    draw_house(t, -250, -150, 100, 80, "tan", "red")
    draw_house(t, -100, -100, 120, 100, "peachpuff", "salmon")
    draw_house(t, 50, -50, 90, 70, "lightblue", "navy")
    draw_house(t, 200, -120, 110, 90, "lightgreen", "darkgreen")
    draw_house(t, 350, -80, 100, 80, "lavender", "purple")
 # two additional houses to the right, same spacing pattern
    draw_house(t, 500, -90, 100, 80, "wheat", "sienna")
    
    # trees
    draw_all_trees(t)

# Run the program 
if __name__ == "__main__":
    t, screen = setup_turtle()
    draw_scene(t)
    t.hideturtle()
    turtle.done()
# ...existing code...