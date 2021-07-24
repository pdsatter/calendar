import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
import datetime

events = {}


def create_event(date, event):
    if events.get(date) is None:
        events[date] = event
    else:
        event_list = [e for e in events[date]]
        event_list = event_list.append(event)
        events[date] = tuple(event_list)


def get_events(date):  # works :)
    if events.get(date) is None: return ''
    return events[date]


def string_of_events(date):  # works :)
    if events.get(date) is None: return ''  # nothing planned, just return empty string
    if isinstance(events[date], str): return '\n' + events[date]  # so it doesn't iterate through letters

    event_string = ''
    for event in events[date]:
        event_string = "{}\n- {}".format(event_string, event)
    return event_string


def update_todo_list(date):
    Canvas.itemconfig(canvas_text, text="Events planned: {}".format(string_of_events(date)))


def update_date():
    return cal.get_date()


def add_event():
    key_to_add = update_date()
    event_to_add = event_string_variable.get()
    print(key_to_add, event_to_add)
    events[key_to_add] = event_to_add
    print('event added ' + enter_event_box.get() + 'on date: ' + update_date())


root = tk.Tk()
root.title('Calendar')
root.geometry("800x1000")

today = datetime.datetime.now()
cal = Calendar(root, selectmode='day', year=today.year, month=today.month, day=today.day)
cal.pack(fill="both", expand=True)

event_canvas = Canvas(root, width=450, height=300)
event_canvas.pack()

event_string_variable = StringVar()
enter_event_box = Entry(root, textvariable=event_string_variable, font=("Helvetica", 20), width=30, fg="gray", bd=0)
enter_event_box.pack()
enter_event_button = Button(root, text='submit', command=add_event())
enter_event_button.pack()

event_box_window = event_canvas.create_window(0, 10, anchor='nw', window=enter_event_box)
date_today = cal.get_date()
events[date_today] = ('Chill',)  # TODO: Remove, this is test
canvas_text = event_canvas.create_text(0, 60, justify='left', anchor=NW, font=("Helvetica", 20),
                                       text="  Events: {}".format(string_of_events(date_today)))

print(events)
root.mainloop()
