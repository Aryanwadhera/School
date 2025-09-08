import turtle
screen = turtle.Screen()
screen.title("ARYAN")
screen.setup(600, 400)

def draw_A(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(75)
    turtle.forward(80)
    turtle.right(150)
    turtle.forward(80)
    turtle.backward(30)
    turtle.right(105)
    turtle.forward(25)

def draw_R(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40) 
    turtle.left(135)
    turtle.forward(56.5)
    turtle.penup()

def draw_Y(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(40)
    turtle.left(45)
    turtle.forward(28)
    turtle.backward(28)
    turtle.right(90)
    turtle.forward(28)

def draw_N(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(80)
    turtle.right(135)
    turtle.forward(113)
    turtle.left(135)
    turtle.forward(80)



draw_A(-160, -40)
draw_R(-80, -40)
draw_Y(0, -40)
draw_A(80, -40)
draw_N(160, -40)

turtle.hideturtle()
turtle.done()
