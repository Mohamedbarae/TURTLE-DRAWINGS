
import turtle

t=turtle.Turtle()


#je décale le curseur de la tortue du centre pour avoir plus d'espaces au cas où les carrés sont grands 
t.speed(0)
 
t.penup()
t.left(180)
t.forward(200)
t.right(180)
t.pendown()

t.speed(0)
 
t.penup()
t.left(180)
t.forward(300)
t.right(180)
t.right(90)
t.forward(300)
t.left(90)
t.pendown()


def carres () :
    s = 20

    for i in range (0,15) :
        s= s+50
        t.forward(s)
        t.left(90)
        t.forward(s)
        t.left(90)
        t.forward(s)
        t.left(90)
        t.forward(s)
        t.left(90)


carres()

turtle.done()







