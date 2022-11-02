import turtle
import random as ra
import math as m

skk = turtle.Turtle()

d = int(input("input length edg : "))
r = int(input("input short edg : "))

skk.hideturtle()
skk.penup()
skk.goto(-d/2,-r/2)
skk.pensize(10)
skk.color("blue")
skk.speed(5)
skk.pendown()
for i in range(2):
    skk.forward(d)
    skk.left(90)
    skk.forward(r)
    skk.left(90)

skk.penup()
skk.goto(0,0)
skk.showturtle()
skk.shape("turtle")
skk.turtlesize(1)

#tinh goc cu hinh chu nhan tu tam
arg =m.degrees(m.atan(r/d))
print(arg)
skk.speed(1)
#vong lap cho rua chay
for i in range(10):
    
    arg_rand=ra.randint(0,360)
    skk.left(arg_rand)
    arg_i=skk.heading()# xac dinh goc hien tai cua rua 
    
    #xac dinh khoang cach xa nhat voi goc cua rua
    if (arg_i>=arg and arg_i <=180-arg) :
        dis_max =r/abs(2*m.sin(arg_i*m.pi/180))
        
    elif (arg_i >=180+arg and arg_i <=360-arg):
        dis_max =r/abs(2*m.sin(arg_i*m.pi/180))
    else:
        dis_max =d/abs(2*m.cos(arg_i*m.pi/180))
    
    skk.forward(dis_max-13)
    skk.left(180)
    skk.goto(0,0)
    
turtle.done()
    
    