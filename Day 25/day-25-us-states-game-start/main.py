import turtle
import pandas as pd
from text import Text

states_df = pd.read_csv('./50_states.csv')
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

text = Text()
correct_guesses = []

game_is_on = True
while game_is_on:
    answer_state = (screen.textinput(title=f'{len(correct_guesses)}/50 States Correct', prompt='What is another states name?')).title()

    if len(correct_guesses) > 49:
        text.winning_text()
        game_is_on = False
    elif answer_state in states_df['state'].values and not (answer_state in correct_guesses):
        correct_guesses.append(answer_state)
        state = states_df[states_df.state == answer_state]
        x_cor = int(state['x'])
        y_cor = int(state.y)
        text.write_text(x_cor,y_cor,answer_state)
    if answer_state == 'Exit':
        break

missed_states = pd.DataFrame(columns=['Missed_states'])
for i, row in states_df.iterrows():
    state = row['state']
    if state in correct_guesses:
        continue
    else:
        index = len(missed_states.Missed_states)
        missed_states.at[index,'Missed_states'] = state
missed_states.to_csv('Missed States.csv', index= False)
screen.exitonclick()