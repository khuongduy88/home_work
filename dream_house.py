import turtle

#khai bao bien 
skk = turtle.Turtle()

skk.pensize(5)
skk.speed(10)
skk.penup()

#ve mat truoc ngoi nha
skk.goto(-400,-100)
skk.pendown()
skk.fillcolor("green")
skk.begin_fill()
for i in range(4):
    skk.forward(100)
    skk.right(90)

skk.end_fill()
skk.penup()

#ve cua nha
skk.goto(-330,-200)
skk.pendown()
skk.fillcolor("blue")
skk.begin_fill()
for i in range (2):
    skk.left(90)
    skk.forward(80)
    skk.left(90)
    skk.forward(40)

skk.end_fill()
skk.penup()

#ve mai nha tam giac
skk.goto(-300,-100)
skk.pendown()
skk.fillcolor("green")
skk.begin_fill()
for i in range(3):
    skk.left(120)
    skk.forward(100)

skk.end_fill()
skk.penup()

#ve chieu dai mai nha
skk.pendown()
skk.fillcolor("green")
skk.begin_fill()
skk.left(30)
for i in range(2):
    skk.forward(300)
    skk.left(90)
    skk.forward(100)
    skk.left(90)
    
skk.end_fill()
skk.penup()

#ve chieu dai ngoi nha
skk.pendown()
skk.fillcolor("green")
skk.begin_fill()
for i in range(2):
    skk.forward(300)
    skk.right(120)
    skk.forward(100)
    skk.right(60)
    
skk.end_fill()
skk.penup()


#ve cua so
skk.forward(100)
skk.right(120)
skk.forward(30)
skk.left(120)

skk.pendown()
skk.fillcolor("yellow")
skk.begin_fill()
for i in range(2):
    skk.forward(100)
    skk.right(120)
    skk.forward(40)
    skk.right(60)

skk.end_fill()
skk.penup()

#ve cay coi
skk.goto(200,-300)
skk.right(30)
skk.pendown()
skk.fillcolor("gray")
skk.begin_fill()
for i in range(2):
    skk.forward(20)
    skk.left(90)
    skk.forward(100)
    skk.left(90)
    
skk.end_fill()
skk.penup()

#ve 3 tan la
skk.goto(160,-200)
for i in range(3):
    skk.pendown()
    skk.fillcolor("yellow")
    skk.begin_fill()
    for i in range(3):
        skk.forward(100)
        skk.left(120)
    skk.end_fill()
    skk.penup()
    skk.left(60)
    skk.forward(100)
    skk.right(60)
    skk.back(50)

#ve mat troi
skk.goto(50,300)
skk.pendown()
skk.fillcolor("yellow")
skk.begin_fill()
skk.circle(60)
skk.end_fill()
skk.penup()

for i in range(8):
    skk.goto(50,360)
    skk.forward(60)
    skk.pendown()
    skk.forward(30)
    skk.penup()
    skk.right(45)

turtle.done