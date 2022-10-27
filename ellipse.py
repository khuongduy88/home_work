import turtle
skk = turtle.Turtle()

skk.pencolor("blue")
skk.pensize(3)
skk.right(45)
d = 150
r = 50
i=0
while i < 2:
    skk.circle(d,90)
    skk.circle(r,90)
    i+=1

turtle.done()