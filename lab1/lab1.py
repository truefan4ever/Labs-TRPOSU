import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
import sys
import time
from tkinter import *

# main loop
root = tk.Tk()
var = tk.IntVar()
frame = tk.Frame(root)
frame.grid()
FONT_TEXT = 'Mono'

# создание тулбара
m = Menu(root)  # создается объект Меню на главном окне
root.config(menu=m)  # окно конфигурируется с указанием меню для него


def new_win():
    win = Toplevel(root)


def close_win():
    root.destroy()


def about():
    win = Toplevel(root)
    lab = Label(win, text="This program is designed for TRPOSU\n "
              'Developed by student gr.622401 Tratsevskiy\n'
              '05/09/2018')
    lab.pack()


def help():
    win = Toplevel(root)
    lab1 = Label(win, text="If you have any questions, \n please contact kotofey_98@mail.ru")
    lab1.pack()


def floor_selection():
    a = var.get()
    if a == 1:
        diction = first_floor
        combobox_values = list(diction.keys())
        combobox.config(values=combobox_values)
        label_info.configure(text="You chose: " + str(diction.get(combobox.get())))
    elif a == 2:
        diction = second_floor
        combobox_values = list(diction.keys())
        combobox.config(values=combobox_values)
        label_info.configure(text="You chose: " + str(diction.get(combobox.get())))


def saving():
    filename = asksaveasfilename()
    with open(filename, 'w') as f_obj:
        f_obj.write("Floor 1:\n")
        for key, value in first_floor.items():
            f_obj.write(key + " : " + value + "\n")

        f_obj.write("Floor 2:\n")
        for key, value in second_floor.items():
            f_obj.write(key + " : " + value + "\n")
    f_obj.close()


first_floor = {}
second_floor = {}


def opening():
    openfile = askopenfilename()
    global first_floor
    global second_floor
    with open(openfile) as file_object:
        for line in file_object:
            word = line.split(",")
            if int(word[0]) < 6:
                key = word[0]
                value = word[1]
                value = value[0:len(value) - 1]
                first_floor[key] = value
            else:
                key = word[0]
                value = word[1]
                value = value[0:len(value) - 1]
                second_floor[key] = value
    file_object.close()


def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)


fm = Menu(m)  # создается пункт меню с размещением на основном меню (m)
m.add_cascade(label="File", menu=fm)  # пункт располагается на основном меню (m)
fm.add_command(label="Open...", command=opening)  # формируется список команд пункта меню
fm.add_command(label="New", command=new_win)
fm.add_command(label="Save...", command=saving)
fm.add_command(label="Exit", command=close_win)

hm = Menu(m)  # второй пункт меню
m.add_cascade(label="Help", menu=hm)
hm.add_command(label="Help", command=help)
hm.add_command(label="About", command=about)

# labels
label_description = tk.Label(root, text='Choose the floor:')
label_description.place(x=20, y=10)

label_store = tk.Label(root, text='Choose the store:')
label_store.place(x=20, y=70)

label_info = tk.Label(root)
label_info.place(x=20, y=100)

clock = Label(root, font=('times', 11))
clock.place(x=20, y=130)

# radiobuttons
r_button1 = tk.Radiobutton(root, text='Floor 1', variable=var, value=1, command=floor_selection)
r_button1.place(x=20, y=40)

r_button2 = tk.Radiobutton(root, text='Floor 2', variable=var, value=2, command=floor_selection)
r_button2.place(x=120, y=40)

# combobox
combobox = ttk.Combobox(root, state='readonly')
combobox.place(x=120, y=70)

# button
btn_info = ttk.Button(root, text="Info", command=floor_selection)
btn_info.place(x=200, y=130)
btn_info.bind('<Button-1>')

# frame
frame_clock = Frame(root, bg='grey', bd=2)
frame_clock.place(x=20, y=130)


tick()
root.title("Navigation system")
root.geometry('300x170+400+300')
root.resizable(False, False)
root.mainloop()
