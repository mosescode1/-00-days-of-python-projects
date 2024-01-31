from turtle import Turtle, Screen

my_Turtle = Turtle()
my_Screen = Screen()

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         my_Turtle.color(c)
#         my_Turtle.forward(steps)
#         my_Turtle.right(30)
#########################################
# my_Turtle.color('red')
# my_Turtle.fillcolor('Black')
# my_Turtle.begin_fill()
# while True:
#     my_Turtle.forward(300)
#     my_Turtle.left(200)
#     if abs(my_Turtle.pos()) < 1:
#         break
# my_Turtle.end_fill()

############################################
# my_Turtle.goto(-150, -150)
# my_Turtle.pencolor('green')
# my_Turtle.pendown()
# my_Turtle.forward(100)

my_Screen.onclick(my_Turtle.goto)
