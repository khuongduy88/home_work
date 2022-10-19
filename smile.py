import turtle

#define pen size
skk=turtle.Turtle()
skk.pensize(5)

#define pen color
skk.pencolor("blue")

#define face size
facesize=250
skk.penup()
skk.goto(0,-facesize)
skk.fillcolor("pink")
skk.begin_fill()
skk.pendown()
skk.circle(facesize)
skk.penup()
skk.end_fill()

#for eyes
#mau nen mat la mau xanh
eye_size = 20

skk.goto(-100,50)
skk.fillcolor("green")
skk.pendown()
skk.begin_fill()
skk.circle(eye_size)
skk.end_fill()
skk.penup()

skk.goto(100,50)
skk.fillcolor("green")
skk.pendown()
skk.begin_fill()
skk.circle(eye_size)
skk.end_fill()
skk.penup()

#for nose
skk.goto(0,50)
skk.pendown()
skk.fillcolor("yellow")
skk.begin_fill()
skk.circle(-70,steps=3)
skk.end_fill()
skk.penup()

#smile
skk.goto(-100,-70)
skk.pendown()
skk.right(90)
skk.circle(100,180)


turtle.done()
