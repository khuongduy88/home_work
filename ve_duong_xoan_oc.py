import turtle

skk=turtle.Turtle()

skk.pensize(5)
skk.pencolor("blue")

dis = 0
max_dis = 400
step = 0.5

while dis < max_dis:
    skk.forward(step)
    skk.right(30)
    dis = turtle.distance(skk)
    step +=1

turtle.done()