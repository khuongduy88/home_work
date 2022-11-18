import turtle

t = turtle.Turtle()

t.pensize(5)
t.penup()

def draw_rectangle(s_node,hori_edge,ver_edge,pen_color,fill_color):
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

def draw_triangle(s_node,bottom_edge,hight,pen_color,fill_color):
    t.goto(s_node)
    t.pendown()
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    
    t.goto(s_node[0]+bottom_edge/2,s_node[1])
    t.goto(s_node[0],s_node[1]+hight)
    t.goto(s_node[0]-bottom_edge/2,s_node[1])
    t.goto(s_node)
    
    t.end_fill()
    t.penup()
    
    t.goto(s_node[0],s_node[1]+hight)

draw_rectangle((-200,-200),400,200,"blue","white")
draw_rectangle((-50,-200),150,100,"blue","white")
draw_triangle((-50,0),300,100,"blue","white")
draw_rectangle((300,-300),50,150,"gray","gray")

draw_triangle((325,-150),200,80,"blue","blue")
draw_triangle(t.pos(),150,50,"green","green")
draw_triangle(t.pos(),120,30,"yellow","yellow")

turtle.done()