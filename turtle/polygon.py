import turtle
t=turtle.Turtle()
t.shape("classic")
t.color("orange","yellow")
t.speed(0)

def hex(t,len) :

 t.fillcolor("light green")
 t.begin_fill()
 for i in range(6):

    t.forward(len)
    t.right(60)
 t.end_fill()
def hex1(t,len,count):
  for i in  range(count):
   hex(t,len)
   t.left(360/count)

hex1(t,150,6)
turtle.done()
