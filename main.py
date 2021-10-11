import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)


df = pandas.read_csv("50_states.csv")
state = df.state
state_list = state.tolist()

guessed_states = []
score = 0

while len(guessed_states) < 50:

    screen.update()

    answer_state = screen.textinput(title="Guess the State", prompt=f"{len(guessed_states)}/50 (Enter exit to end the game)").title()

    if answer_state == "Exit":
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        answer_state_df = df[state == answer_state]
        x_cor = int(answer_state_df.x)
        y_cor = int(answer_state_df.y)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(x_cor, y_cor)
        new_turtle.write(answer_state, align="center", font=("Courier", 12, "normal"))

missing_states = [state for state in state_list if state not in guessed_states]

data_dict = {
    "Missing States": missing_states
}

df = pandas.DataFrame(data_dict)
df.to_csv("missing states.csv")



