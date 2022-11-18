import turtle

t = turtle.Turtle()
t.pensize(5)
t.penup()

def draw_rectangle(s_node,hori_edge,ver_edge,pen_color,fill_color):
    #hori_edge : canh nam ngang
    #ver_edge : canh thang dung
    
    t.goto(s_node)
    t.pendown()
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    
    for i in range(0,2):
        t.forward(hori_edge)
        t.left(90)
        t.forward(ver_edge)
        t.left(90)
        
    t.end_fill()
    t.penup()

draw_rectangle((-200,-400),200,400,"blue","red")
draw_rectangle((-150,-400),100,150,"blue","orange")
draw_rectangle((0,-400),200,400,"blue","red")
draw_rectangle((50,-400),100,150,"blue","orange")    
draw_rectangle((-200,0),200,400,"blue","red")
draw_rectangle((-150,0),100,150,"blue","orange")
draw_rectangle((0,0),200,400,"blue","red")
draw_rectangle((50,0),100,150,"blue","orange")
draw_rectangle((200,-400),500,400,"blue","gray")
draw_rectangle((400,-400),50,150,"blue","green")
draw_rectangle((450,-400),50,150,"blue","green")

turtle.done()