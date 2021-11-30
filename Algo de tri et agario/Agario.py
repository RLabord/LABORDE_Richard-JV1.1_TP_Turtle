
import turtle
import random
import math

maTortue = turtle.Turtle()
maFenetre = turtle.Screen()

maFenetre.colormode(255)
maTortue.shape("circle")
maTortue.up()
maTortue.speed(0)
turtle.delay(0)
turtle.listen()

def goUp():
    maTortue.setheading(90)

def goLeft():
    maTortue.setheading(180)

def goDown():
    maTortue.setheading(270)

def goRight():
    maTortue.setheading(0)

turtle.onkeypress(goUp,"Up")
turtle.onkeypress(goLeft,"Left")
turtle.onkeypress(goDown,"Down")
turtle.onkeypress(goRight,"Right")

def distance(A, B):
    return(math.sqrt((float(A[0]) - float(B[0]))**2 + (float(A[1]) - float(B[1]))**2))

pas = 3
nbDeTortues = 6 
startingSquareWidth = 300
listeDeTortues = []

for i in range(nbDeTortues):
    tempTortue = turtle.Turtle()
    tempTortue.shape('circle')

   
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tempTortue.color((R, G, B))


    posX = random.random() * startingSquareWidth - startingSquareWidth//2
    posY = random.random() * startingSquareWidth - startingSquareWidth//2
    tempTortue.penup()
    tempTortue.setpos(posX, posY)
    tempTortue.pendown()

    listeDeTortues.append(tempTortue)
    tempTortue.up()
while 1:
    
    for k in listeDeTortues:
        k.forward(pas)

        facteurAleatoire = random.randint(0, 3)
        if facteurAleatoire == 0:
            k.left(90)
        elif facteurAleatoire == 1:
            k.right(90)
        else:
            pass

    facteurDeTaille = 12.0
    playerSpeed = 5
   
    maTortue.forward(playerSpeed)

    for k in listeDeTortues:
        for l in listeDeTortues:
            if (k.isvisible() and l.isvisible() and k != l and distance(k.position(), l.position()) <= facteurDeTaille * max(k.shapesize()[0], l.shapesize()[0])):
               
                if (k.shapesize()[0] >= l.shapesize()[0]):
                    k.speed(k.speed() + 1)
                    k.shapesize(k.shapesize()[0] * 1.5, k.shapesize()[1]* 1.5)
                    l.hideturtle()
                    l.penup()
                else:
                    l.speed(l.speed() + 1)
                    l.shapesize(l.shapesize()[0]* 1.5, l.shapesize()[1]* 1.5)
                    k.hideturtle()
                    k.penup()
        
        if (k.isvisible() and maTortue.isvisible() and k != maTortue and distance(k.position(), maTortue.position()) <= facteurDeTaille * max(k.shapesize()[0], maTortue.shapesize()[0])):
              
                if (k.shapesize()[0] > maTortue.shapesize()[0]):
                    k.shapesize(k.shapesize()[0] * 1.5, k.shapesize()[1]* 1.5)
                    maTortue.hideturtle()
                    maTortue.penup()
                else:
                    maTortue.shapesize(maTortue.shapesize()[0]* 1.5, maTortue.shapesize()[1]* 1.5)
                    k.hideturtle()
                    k.penup()
    
maTortue.up()


input()
