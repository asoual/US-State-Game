import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.Turtle(image)
data = pandas.read_csv("50_states.csv")
states = data.state.str.lower()
x_cor = data.x.to_list()
y_cor = data.y.to_list()
list_states = states.to_list()
game_is_on = True
count = 0
guessed_state = []
while game_is_on:
    answer_state = screen.textinput(title = f"{count}/50 States Correct", prompt="What is another state's name?").lower()
    if any(answer_state in i for i in list_states):
        if answer_state not in guessed_state:
            count += 1
            state_index = list_states.index(answer_state)
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(x_cor[state_index], y_cor[state_index])
            turtle.write(answer_state.capitalize())
            guessed_state.append(answer_state)
    if count == 50:
        game_is_on = False
        print("Game Over! You have guessed all 50 states.")
    if answer_state == "exit":
        game_is_on = False
        print(f"Game Over! You have guessed {count} states.")
        missing_states = []
        for state in list_states:
            if state not in guessed_state:
                missing_states.append(state)
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.columns = ["Missing States"]
        missing_states_data.to_csv("missing_states.csv")