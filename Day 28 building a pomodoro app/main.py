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
CHECK_MARK = "✓"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text=f'00:00')
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text='Break time nerd', fg=PINK)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text='Break time nerd', fg=RED)
    else:
        count_down(WORK_MIN * 60)
        title.config(text='Get to work nerd', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = math.floor(count / 60)
    second = count % 60
    if second < 10:
        second = f'0{second}'
    canvas.itemconfig(timer_text, text=f'{minute}:{second}')
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps/ 2)):
            marks += CHECK_MARK
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text='00:00', fill='white', font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row= 1)

title = Label(text= 'Timer',font=(FONT_NAME,45), bg=YELLOW, fg=GREEN)
title.grid(column= 1,row=0)

start_b = Button(text='Start',command=start_timer)
start_b.grid(column=0, row=2)

reset_b = Button(text='Reset',command=reset_timer)
reset_b.grid(column=2, row=2)

check_marks = Label(font=(FONT_NAME,20), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1,row=2)




window.mainloop()