import pandas
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get pandas to read the states file. Turns csv file into a Data frame

state_data = pandas.read_csv("50_states.csv")

# get the state column into a list
us_states = state_data.state.to_list()

number_of_state = len(us_states)

state_dict = {}

for state in us_states:
    state_x = float(state_data[state_data.state == state].x)
    state_y = float(state_data[state_data.state == state].y)
    state_cor = (state_x, state_y)
    state_dict[state] = state_cor

# print(state_dict)

state_count = []

while len(state_count) < len(us_states):

    answer_state = screen.textinput(title=f"{len(state_count)}/{len(us_states)} states correct", prompt="What is "
                                                                                                        "another state "
                                                                                                        "name?").title()
    if answer_state == "Exit":
        break

    if answer_state in us_states:
        state_count.append(answer_state)

        cor = state_dict[answer_state]
        write_answer = Turtle()
        write_answer.penup()
        write_answer.hideturtle()
        write_answer.goto(cor)
        write_answer.write(arg=answer_state)

states_to_learn = [state for state in us_states if state not in state_count]

to_learn_data = pandas.DataFrame(states_to_learn)

to_learn_data.to_csv("states_to_learn.csv")


# screen.mainloop()
