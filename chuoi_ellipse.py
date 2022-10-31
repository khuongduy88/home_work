import turtle
skk = turtle.Turtle()
skk.pensize(3)
skk.speed(10)
#skk.pencolor((10,10,10))
color = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
d=150
r=50
arg=10
col_i=0
for i in range(0,360,arg):
    count =0
    if col_i==10 :
        col_i=0
    skk.color(color[col_i])
    while count <2:
        skk.circle(d,90)
        skk.circle(r,90)
        count +=1
    
    skk.right(arg)
    col_i+=1

turtle.done()