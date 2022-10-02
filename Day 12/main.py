#Been feeling very Lazy Lately so Tried this Turtle thingy lmao 

from turtle import *



# Grass
bgcolor("green")

# Sky
penup()
goto(-400, -100)
pendown()
color("deepskyblue")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

# Sun
penup()
goto(-320, 225)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()

# Cloud
penup()
goto(200, 200)
pendown()
color("white")
begin_fill()
circle(25)
end_fill()

penup()
goto(220, 240)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(230, 215)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(180, 225)
pendown()
begin_fill()
circle(25)
end_fill()

# House
penup()
goto(-100, -100)
pendown()
pensize(3)
color("chocolate", "orange") # (stroke, fill)
begin_fill()
for i in range(4):
    forward(170)
    left(90)
end_fill()

# Chimney
penup()
goto(20, 130)
pendown()
color("brown", "firebrick")
begin_fill()
for i in range(2):
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

# Roof
penup()
goto(-127, 70)
pendown()
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

# Window 1
penup()
goto(0, 0)
pendown()
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# Window 1 Cross - Horizontal Line 
penup()
goto(0, 25)
pendown()
color("black")
forward(50)

# Window 1 Cross - Vertical Line 
penup()
goto(25, 0)
pendown()
left(90)
forward(50)

# Window 2
penup()
goto(-80, 0)
pendown()
right(90)
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# Window 2 Cross - Horizontal Line 
penup()
goto(-80, 25)
pendown()
color("black")
forward(50)

# Window 2 Cross - Vertical Line 
penup()
goto(-55, 0)
pendown()
left(90)
forward(50)

# Door
penup()
goto(-40, -97)
pendown()
right(90)
color("brown")
begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

# Door Handle
penup()
goto(-30, -60)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()

hideturtle()
exitonclick()