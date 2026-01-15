from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

''' Learning listening 
def move():
    t.forward(10)
screen.listen()
screen.onkey(key = "space", fun = move)
screen.exitonclick()
'''
#Building the game

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def clockwise():
    t.right(5)

def anti_clockwise():
    t.left(5)

screen.listen()
screen.onkey( key = "w", fun = move_forwards)
screen.onkey( key = "s", fun = move_backwards)
screen.onkey( key = "a", fun = anti_clockwise)
screen.onkey( key = "d", fun = clockwise)

