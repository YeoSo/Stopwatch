from tkinter import *


# 1. display time start from 00:00:00 (hr, min, sec)
# 2. start, pause, reset button

# ------------------------------ MECHANISM ------------------------------------ #
def start_button():
    pass


# ------------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("Stopwatch")

canvas = Canvas(width=900, height=600, bg="black")
time_text = canvas.create_text(450, 240, text="00:00:00", fill="white", font=("NORMAL", 120))
second_text = canvas.create_text(460, 350, text="hr           min          sec", fill="white", font=("NORMAL", 35))
canvas.grid(column=0, row=0)

# Buttons
# start_button = Button(text="Start", command=start_button)
# start_button.grid(column=0, row=0)

window.mainloop()
