import turtle
import pandas as pd
from text import Text


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv('./50_states.csv')
all_states = data.state.to_list()
guessed_states = []
# missing_states = []
while len(guessed_states) < 50:

    answer_state = (screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt='What is another states name?')).title()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer_state)

    # if answer_state == 'Exit':
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
    #     new_data = pd.DataFrame(missing_states)
    #     new_data.to_csv('States_to_learn.csv')
    #     break

    #List comprehension version of code above
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if (state not in guessed_states)]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('States_to_learn.csv', index=False)
        break




screen.exitonclick()