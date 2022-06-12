import turtle
t = turtle.Turtle()
t.shape("turtle")
turtle.title("Crazy Turtles")
t.color("yellow","blue")
t.pensize(2)
t.speed(0)

t.penup()
size=2
for  i in range(100):
  t.stamp()
  size = size + 2
  t.forward(size)
  t.right(30)
turtle.done()
  