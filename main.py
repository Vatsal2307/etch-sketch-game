from turtle import Turtle, Screen
import random

screen = Screen()
all_turtles = []
colors = ["red", "orange", "blue", "purple"]
y_pos = [-60, -30, 60, 30]
is_race_on = False
screen.setup(width=500, height=400, )
usr_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0, 4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-250, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if usr_bet:
    is_race_on = True
while is_race_on:
    for item in all_turtles:
        if item.xcor() > 230:
            is_race_on = False
            winning_color = item.pencolor()
            if winning_color == usr_bet:
                print(f"Congratulations you won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose. The {winning_color} turtle won!")

        rand_dist = random.randint(0, 10)
        item.forward(rand_dist)

screen.exitonclick()
