
import turtle

t= turtle.Turtle()

t.speed(0)
t.color((1, 0, 0), (0, 1, 1))
t.begin_fill()

for i in range  (18) :
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(70)
    


for i in range  (18) :
    t.forward(40)
    t.left(70)
    t.forward(40)
    t.right(90)



t.end_fill()