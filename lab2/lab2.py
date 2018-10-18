import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
import sys
import time
from tkinter import *
import logging

logging.basicConfig(filename='navigationsystem.log', level=logging.INFO, format='%(asctime)s;%(message)s')

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





def saving():
    filename = asksaveasfilename()
    with open(filename, 'w') as f_obj:
        f_obj.write("Store:\n")
        for key, value in stores.items():
            f_obj.write(key + " : " + value.title() + "\n")
    f_obj.close()


stores = {}



def opening():
    openfile = askopenfilename()
    global stores
    with open(openfile) as file_object:
        for line in file_object:
            word = line.split(",")
            key = word[0]
            value = word[1]
            value = value[0:len(value) - 1]
            stores[key] = value
    print(stores)

    free_stores = 0
    for values in stores.values():
        if str(values) == "none":
            free_stores += 1
    print(free_stores)
    occupied_stores = len(stores) - free_stores
    progress_bar.config(maximum=len(stores))
    progress_bar.config(value=occupied_stores)
    print(occupied_stores)
    label_progress.config(text=str((100*occupied_stores)/len(stores)) + "% occupied")

    file_object.close()


def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)


def choosing_the_number():
    try:
        for key, value in stores.items():
            if int(number.get()) == int(key):
                label_info1.config(text=value.title())
                logging.info("input number: " + number.get() + "; output: " + value.title())
            # else:
            #     label_info.config(text="There are only 5 stores\n in each floor!")
                # logging.info("input: "  + store.get() + "; output: " + message)

    except ValueError:
        message = "Please enter correct number\n(1-st floor: 1**, 2-nd floor: 2**)"
        label_info1.config(text=message)
        logging.info("input number: " + number.get() + "; output: " + message)


def choosing_the_name():

    for key, value in stores.items():

        if str(name.get()) == str(value):
            if int(key) < 106:
                label_info2.config(text="Floor-1, store number: " + str(key))
                logging.info("input name: " + name.get() + "; output: " + "Floor-1, store number: " + str(key))
            elif int(key) > 106 and int(key) < 206:
                label_info2.config(text="Floor-2 store number: " + str(key))
                logging.info("input name: " + name.get() + "; output: " + "Floor-1, store number: " + str(key))
            break
        else:
            message = "Check the name!"
            label_info2.config(text=message)
            logging.info("input name: " + name.get() + "; output: " + message)
        # except TypeError:
        #     message = "Check the name!"
        #     label_info2.config(text=message)
        #  # print("Error")


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
label_description = tk.Label(root, text='Enter the number:')
label_description.place(x=20, y=10)

label_name_store = tk.Label(root, text='Enter the name:')
label_name_store.place(x=20, y=120)

label_progress = tk.Label(root)
label_progress.place(x=200, y=230)

label_info1 = tk.Label(root)
label_info1.place(x=20, y=85)

label_info2 = tk.Label(root)
label_info2.place(x=20, y=180)

# label_info3 = tk.Label(root)
# label_info3.place(x=20, y=200)

clock = tk.Label(root, font=('times', 11))
clock.place(x=20, y=230)

# progress bar
progress_bar = ttk.Progressbar(root,
                               orient="horizontal",
                               length=100,
                               mode="determinate")
progress_bar.place(x=90, y=230)


number = StringVar()
name = StringVar()
# entries
input_entry_number = Entry(textvariable=number)
input_entry_number.place(x=20, y=45)

input_entry_name = Entry(textvariable=name)
input_entry_name.place(x=20, y=155)


# button
btn_info = ttk.Button(root, text="Info", command=choosing_the_number)
btn_info.place(x=200, y=45)
btn_info.bind('<Button-1>')

btn_find = ttk.Button(root, text="Find", command=choosing_the_name)
btn_find.place(x=200, y=155)
btn_find.bind('<Button-1>')

# frame
frame_clock = Frame(root, bg='grey', bd=2)
frame_clock.place(x=20, y=130)


tick()

root.title("Navigation system")
root.geometry('300x270+400+300')
root.resizable(False, False)
root.mainloop()
