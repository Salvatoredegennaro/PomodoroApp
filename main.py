from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time_cl = None
reps = 0


def reset():
    window.after_cancel(time_cl)
    canvas.itemconfig(timer, text="00:00")
    lb1.config(text="Timer")
    lb2.config(text="")


def start():
    global reps
    reps += 1

    work_break_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        lb1.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        lb1.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        lb1.config(text="Work", fg=GREEN)
        count_down(work_break_sec)


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time_cl
        time_cl = window.after(1000, count_down, count - 1)
    else:
        start()
        mark = ""
        work_sessions = math.floor(reps/2)
        for x in range(work_sessions):
            mark += "✔"
        lb2.config(text=mark)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=2, column=2)


lb1 = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW, highlightthickness=0)
lb1.grid(row=1, column=2)

lb2 = Label(fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
lb2.grid(row=4, column=2)

bt1 = Button(text="Start", command=start)
bt1.grid(row=3, column=1)

bt2 = Button(text="Reset", command=reset)
bt2.grid(row=3, column=3)


window.mainloop()