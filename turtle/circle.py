import turtle
#rad=int(input("enter the radius of circle: "))
x=turtle.Turtle()
x.shape("turtle")
x.pencolor("green")
x.circle(100)
x.penup()
x.goto(-50,-50)
x.pendown()
x.circle(150)
x.fillcolor("yellow")
x.begin_fill()
x.end_fill()



turtle.done()
