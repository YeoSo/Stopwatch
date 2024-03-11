from tkinter import *
import time


# ------------------------------ MECHANISM ------------------------------------ #
def start_button():
    global start_time, running, elapsed_time
    if not running:
        start_time = time.time() - elapsed_time
        running = True
        toggle_buttons()
        count()


def pause_button():
    global running
    running = False
    toggle_buttons()


def reset_button():
    global elapsed_time
    elapsed_time = 0
    canvas.itemconfig(time_text, text="00:00:00")


def count():
    global elapsed_time, running
    if running:
        current_time = time.time()
        elapsed_time = current_time - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        canvas.itemconfig(time_text, text=formatted_time)
        window.after(1000, count)


# ------------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("Stopwatch")

canvas = Canvas(width=900, height=600, bg="black")
time_text = canvas.create_text(450, 240, text="00:00:00", fill="white", font=("NORMAL", 120))
hr_text = canvas.create_text(220, 350, text="hr", fill="white", font=("NORMAL", 35))
min_text = canvas.create_text(450, 350, text="min", fill="white", font=("NORMAL", 35))
sec_text = canvas.create_text(690, 350, text="sec", fill="white", font=("NORMAL", 35))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
start_button = Button(window, text="▶", font=("NORMAL", 30), command=start_button)
pause_button = Button(window, text="⏸", font=("NORMAL", 30), command=pause_button)
reset_button = Button(window, text="↺", font=("NORMAL", 30), command=reset_button)

canvas.create_window(330, 450, window=start_button)
canvas.create_window(450, 450, window=pause_button)
canvas.create_window(570, 450, window=reset_button)

elapsed_time = 0
running = False
start_time = 0


def toggle_buttons():
    if running:
        start_button.config(state=DISABLED)
        pause_button.config(state=NORMAL)
    else:
        start_button.config(state=NORMAL)
        pause_button.config(state=DISABLED)


toggle_buttons()

window.mainloop()
