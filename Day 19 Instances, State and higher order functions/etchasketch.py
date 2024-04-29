import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)
def move_back():
    tim.backward(10)
def rotate_right():
    current_heading = tim.heading()
    tim.setheading(current_heading-10)
def rotate_left():
    current_heading = tim.heading()
    tim.setheading(current_heading+10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen() #Listener waits for the user to do something
screen.onkeypress(key='w', fun=move_forward)#When adding the function don't add () at end
screen.onkeypress(key='s', fun=move_back)
screen.onkeypress(key='d', fun=rotate_right)
screen.onkeypress(key='a', fun=rotate_left)
screen.onkey(clear_screen,'space')

screen.exitonclick()