from tkinter import *
import tkinter.messagebox as msgbox
import math

root = Tk()
root.title('Pomodoro App')
root.config(padx=100, pady=50, bg='#ecf7e6')

FOCUS_TIME = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 15
STATE = 'FOCUS'
pomodoro = ''
count = 0


def start_timer():
    global STATE

    if (STATE == 'FOCUS'):
        status_label.config(text='Focusing')
        countdown(FOCUS_TIME * 60)
    elif (STATE == 'SHORTBREAK'):
        status_label.config(text='Short Break')
        countdown(SHORT_BREAK_TIME * 60)
    elif (STATE == 'LONGBREAK'):
        status_label.config(text='Long Break')
        countdown(LONG_BREAK_TIME * 60)

    start_button.grid_forget()

def countdown(time):
    global pomodoro, count, STATE

    
    minutes = math.floor(time/60)
    seconds = time % 60
    timer_label.config(text = f'{minutes:02}:{seconds:02}')
    if (time > 0):
        root.after(1000, countdown , time-1)
    elif (time <= 0 and STATE == 'FOCUS'):
        pomodoro += "🍅"
        count += 1
        pomodoro_count_label.config(text=pomodoro)
        if (count % 4 != 0):
            STATE = 'SHORTBREAK'
            status_label.config(text='Take a short break')
            start_button.grid(column=1, row=2)
            start_button.config(text='Start a short break')
        else:
            STATE = 'LONGBREAK'
            status_label.config(text='Take a long break')
            start_button.grid(column=1, row=2)
            start_button.config(text='Start a long break')
    else:
        STATE = 'FOCUS'
        status_label.config(text='Break finished')
        start_button.grid(column=1, row=2)
        start_button.config(text='Start focusing')

def exit_msg():
    msgbox.showinfo(title='', message='You did {} pomodoro this session'.format(count))
    root.destroy()

tomato = PhotoImage(file='tomato.png')

canvas_width = tomato.width()
canvas_height = tomato.height()
canvas_center_x = canvas_width // 2
canvas_center_y = canvas_height // 2

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='#ecf7e6', highlightthickness=0)
canvas.create_image(canvas_center_x, canvas_center_y, image=tomato) 
canvas.grid(column=1, row=1)

status_label = Label(root, text='Press Start to Start Focusing', bg='#ecf7e6', font=20)
status_label.grid(column=1, row=0)

timer_label = Label(root, text='', bg='#ecf7e6', font = 10)
timer_label.grid(column= 1, row = 3)

pomodoro_count_label = Label(root, text = '')
pomodoro_count_label.grid(column=1, row=4)

start_button = Button(root, text='Start Focusing', bg='#d13b3b', font=10, command=start_timer)
start_button.grid(column=1, row=2)

root.protocol('WM_DELETE_WINDOW', exit_msg)
root.mainloop()
