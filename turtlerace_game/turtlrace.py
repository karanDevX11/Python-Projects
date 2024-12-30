import turtle as t
import random

screen  = t.Screen()
screen.setup(width=500, height= 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
print(user_bet)

x= -230
y= -100

all_turtles = []
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.color(colors[turtle_index])
    y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won the race. The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost the race. The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()