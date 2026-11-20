


import turtle
import math

t=turtle.Turtle()

#je décale le curseur de la tortue du centre pour avoir plus d'espaces au cas où les carrés sont grands 
t.speed(0)
 
t.penup()
t.left(180)
t.forward(300)
t.right(180)
t.pendown()


def carre(longueur) :  # fonction du carré 

    for i in range (0,4):

        t.forward(longueur)

        t.left(90)



def carres(nb_de_carres) : # fonction de n carrés 
    cote_ = 30
    for i in range (nb_de_carres) :

        carre(cote_)
        cote_ =  cote_+20
   
    # traçage de la diagonale = coté*sqrt(2)
    diagonal =(cote_-20)*math.sqrt(2)
    t.left(45)
    t.forward(diagonal)

carres(10)


turtle.done()




































