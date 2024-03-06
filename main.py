from tkinter import *


# ------------------------------ MECHANISM ------------------------------------ #
def start_button():
    global running
    running = True
    count()


def pause_button():
    global running
    running = False


def reset_button():
    global elapsed_time
    elapsed_time = 0
    canvas.itemconfig(time_text, text="00:00:00")


def count():
    global elapsed_time, running
    if running:
        # Convert elapsed time to hours, minutes, seconds
        hours = int(elapsed_time / 3600)
        minutes = int((elapsed_time % 3600) / 60)
        seconds = int(elapsed_time % 60)

        # Format the time as a string
        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        # Update the time on the canvas
        canvas.itemconfig(time_text, text=time_string)

        # Increment elapsed time
        elapsed_time += 1

        # Call count() again after 1 second
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

window.mainloop()

