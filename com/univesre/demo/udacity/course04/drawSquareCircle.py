import turtle

def drawSquareCircle():
    window = turtle.Screen()
    window.bgcolor("grey")
    # A Turtle:
    turtleSqr = turtle.Turtle()
    turtleSqr.shape("turtle")
    turtleSqr.color("yellow")
    turtleSqr.speed(6)
    # Loop To Draw Squares:
    for i in range(0, 36):
        drawASingleSquare(turtleSqr)
        turtleSqr.right(10)
    window.exitonclick()
    
def drawASingleSquare(turtle):
    for i in range(0, 4):
        turtle.forward(100)
        turtle.right(90)

drawSquareCircle()