import turtle

def drawShapes():
    window = turtle.Screen()
    window.bgcolor("grey")

    drawSquare()
    drawCricle()
    drawTriangle()

    window.exitonclick()

def drawSquare():
    turtleSquare = turtle.Turtle()
    turtleSquare.shape("turtle")
    turtleSquare.color("yellow")
    turtleSquare.speed(2)
    loopCtrl = 0
    while (loopCtrl < 4):
        turtleSquare.forward(100)
        turtleSquare.right(90)
        loopCtrl = loopCtrl + 1

def drawCricle():
    turtleCircle = turtle.Turtle()
    turtleCircle.shape("turtle")
    turtleCircle.color("yellow")
    turtleCircle.speed(2)
    turtleCircle.circle(100)

def drawTriangle():
    turtleSquare = turtle.Turtle()
    turtleSquare.shape("turtle")
    turtleSquare.color("yellow")
    turtleSquare.speed(2)
    loopCtrl = 0
    while loopCtrl < 3:
        turtleSquare.forward(100)
        turtleSquare.right(120)
        loopCtrl = loopCtrl + 1


drawShapes()

