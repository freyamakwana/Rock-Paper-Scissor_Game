from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from random import randint

# Main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(bg="peach puff")

# Add buttons
button_rock = Button(root, width=16, height=3, text="ROCK", font=("TIMES", 20, "bold"), bg="brown4", fg="black", command=lambda: choice_update("rock"))
button_rock.grid(row=2, column=1)

button_paper = Button(root, width=16, height=3, text="PAPER", font=("TIMES", 20, "bold"), bg="brown4", fg="black", command=lambda: choice_update("paper"))
button_paper.grid(row=2, column=2)

button_scissor = Button(root, width=16, height=3, text="SCISSOR", font=("TIMES", 20, "bold"), bg="brown4", fg="black", command=lambda: choice_update("scissor"))
button_scissor.grid(row=2, column=3)

player_indicator = Label(root, font=('Times', 40, "bold"), text="PLAYER", bg="indianred1", fg="black")
computer_indicator = Label(root, font=('Times', 40, "bold"), text="COMPUTER", bg="indianred1", fg="black")
computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)


def updateMessage(a):
    final_message['text'] = a


def Computer_Update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)


def Player_Update():
    final = int(player_score["text"])
    final += 1
    player_score["text"] = str(final)


def winner_check(p, c):
    if p == c:
        updateMessage("It's a Tie")
    elif p == "rock":
        if c == "paper":
            updateMessage("Computer WINS!")
            Computer_Update()
        else:
            updateMessage("Player WINS!")
            Player_Update()
    elif p == "paper":
        if c == "scissor":
            updateMessage("Computer WINS!")
            Computer_Update()
        else:
            updateMessage("Player WINS!")
            Player_Update()
    elif p == "scissor":
        if c == "rock":
            updateMessage("Computer WINS!")
            Computer_Update()
        else:
            updateMessage("Player WINS!")
            Player_Update()
    else:
        pass


to_select = ["rock", "paper", "scissor"]


def choice_update(a):
    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=rock2_img)
    elif choice_computer == "paper":
        label_computer.configure(image=paper2_img)
    else:
        label_computer.configure(image=scissor2_img)

    if a == "rock":
        label_player.configure(image=rock_img)
    elif a == "paper":
        label_player.configure(image=paper_img)
    else:
        label_player.configure(image=scissor_img)

    winner_check(a, choice_computer)


final_message = Label(root, font=('Times', 40, 'bold'), bg='red', fg='white')
final_message.grid(row=3, column=2)

# Pictures of rock paper scissors
rock_img = Image.open("rock1.png").resize((150, 150))
rock_img = ImageTk.PhotoImage(rock_img)

paper_img = Image.open("paper1.png").resize((150, 150))
paper_img = ImageTk.PhotoImage(paper_img)

scissor_img = Image.open("scissor1.png").resize((150, 150))
scissor_img = ImageTk.PhotoImage(scissor_img)

rock2_img = Image.open("rock2.png").resize((150, 150))
rock2_img = ImageTk.PhotoImage(rock2_img)

paper2_img = Image.open("paper2.png").resize((150, 150))
paper2_img = ImageTk.PhotoImage(paper2_img)

scissor2_img = Image.open("scissor2.png").resize((150, 150))
scissor2_img = ImageTk.PhotoImage(scissor2_img)

# Insert picture
label_player = Label(root, image=rock_img)
label_computer = Label(root, image=rock2_img)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

computer_score = Label(root, text=0, font=('Times', 60, 'bold'), fg="red")
player_score = Label(root, text=0, font=('Times', 60, "bold"), fg="red")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

root.mainloop()
