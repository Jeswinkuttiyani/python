import turtle
x=turtle.Turtle()
turtle.colormode(255)
x.speed(0)
x.forward(10)
x.penup()
x.goto(-100,-100)
x.pendown()
x.fillcolor(150,75,0)
x.begin_fill()
for i in range(4):
    x.forward(200)
    x.left(90)
x.end_fill()


x.penup()
x.goto(-100,100)
x.pendown()
x.fillcolor(200,0,0)
x.begin_fill()
for i in range(3):
    x.forward(200)
    x.left(120)
x.end_fill()

x.penup()
x.goto(-40,-100)
x.pendown()
x.fillcolor(100,50,0)
x.begin_fill()
x.forward(70)
x.left(90)
x.forward(100)
x.left(90)
x.forward(70)
x.left(90)
x.forward(100)
x.left(90)
x.end_fill()



x.penup()
x.goto(250,200)
x.pendown()
x.fillcolor("orange")
x.begin_fill()
x.circle(80)
x.end_fill()

x.penup()
x.goto(-70, -100)  # Start in front of the door
x.pendown()
x.fillcolor(80, 80, 80)  # Gray color
x.begin_fill()
x.forward(130)  # Width of the road
x.right(90)
x.forward(200)  # Length extending downwards
x.right(90)
x.forward(130)
x.right(90)
x.forward(200)
x.right(90)
x.end_fill()

# Draw dashed centerline on the road
x.pensize(4)
x.pencolor("white")
x.penup()
x.goto(-5, -100)  # Start near the middle of the road
x.setheading(270)  # Face downward

for _ in range(10):  # Draw dashed line
    x.pendown()
    x.forward(15)
    x.penup()
    x.forward(15)

turtle.done()