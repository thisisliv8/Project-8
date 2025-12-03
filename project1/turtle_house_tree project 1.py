from turtle import*
#Sets the drawing speed, pen size, and background color to yellow 
speed(4)
pensize(2)
bgcolor("yellow")

#A variable that controls whether the second tree is drawn
draw_second_tree= True 

#Draws red square base of the house
penup()
goto(-75,-150)
pendown()
color("red")
begin_fill()
for i in range(4): #Loop draws 4 sides of square 
   forward(150)
   left(90)
end_fill()

#This draws a black triangular roof
goto(-75,0)
pendown()
color("black")
begin_fill()
goto(0,100)
goto(75,0)
goto(-75,0)
end_fill()

#Draws a purple star 
penup()
color("purple")
goto(100,100)
pendown()

begin_fill()
for i in range(5): #Loop draws a 5 pointed star
    forward(100)
    right(144)
end_fill()

#Draws the blue trunk of the first tree 
penup()
goto(100,-155)
pendown()
color("blue")
begin_fill()
for i in range(2): #Draws rectagular tree trunk 
    forward(20)
    left(90)
    forward(60)
    left(90)
end_fill()

penup()
goto(110,-90)
pendown()
color("orange")
begin_fill()
circle(30)
end_fill()

penup()
goto(-200,-155)

#Conditional only draws second tree if true 
if draw_second_tree:
    #Draws the brown trunk  of the second tree 
    pendown()
    color("brown")
    begin_fill()
    for i in range(2): #Draws rectangular tree trunk 
        forward(20)
        left(90)
        forward(60)
        left(90)
    end_fill()

#Draws the tree leaves of the second tree a small, round orange circle 
penup()
goto(-190,-90)
pendown()
color("orange")
begin_fill()
circle(30)
end_fill()

done()
