import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import *
import sys
import time
from tkinter import *
import logging

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()



    def init_main(self):

        # entries
        input_entry_number = tk.Entry(root)
        input_entry_number.place(x=20, y=45)

        input_entry_name = tk.Entry(root)
        input_entry_name.place(x=20, y=155)

        # labels
        label_description = tk.Label(root, text='Enter the number:')
        label_description.place(x=20, y=10)

        label_name_store = tk.Label(root, text='Enter the name:')
        label_name_store.place(x=20, y=120)

        self.label_info1 = tk.Label(root)
        self.label_info1.place(x=20, y=85)

        self.label_info2 = tk.Label(root)
        self.label_info2.place(x=20, y=180)

        # button
        btn_info = ttk.Button(root, text="Info")
        btn_info.place(x=200, y=45)
        btn_info.bind('<Button-1>')

        btn_find = ttk.Button(root, text="Find")
        btn_find.place(x=200, y=155)
        btn_find.bind('<Button-1>')

        btn_state_change = tk.Button(root, text="Change the state", command=self.open_dialog1)
        btn_state_change.place(x=50, y=250)

        btn_join_stores = tk.Button(root, text="Join stores",  command=self.open_dialog2)
        btn_join_stores.place(x=190, y=250)


    def open_dialog1(self):
        Child1()


    def open_dialog2(self):
        Child2()


class Child1(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('State changing')
        self.geometry('330x220+400+300')
        self.resizable(False, False)

        label1 = tk.Label(self, text='Choose the floor:')
        label1.place(x=20, y=10)

        label2 = tk.Label(self, text='Choose the number:')
        label2.place(x=20, y=70)

        # radiobuttons
        self.r_button1 = tk.Radiobutton(self, text='Floor 1')
        self.r_button1.place(x=40, y=40)

        self.r_button2 = tk.Radiobutton(self, text='Floor 2')
        self.r_button2.place(x=140, y=40)


        self.entry = ttk.Entry(self)
        self.entry.place(x=40, y=130)

        self.combobox = ttk.Combobox(self, values=[u'Store1', u'Store2'])
        self.combobox.current(0)
        self.combobox.place(x=40, y=100)

        self.var = IntVar()
        self.checkbutton = tk.Checkbutton(self, text='Clean the store', variable=self.var, onvalue=1, offvalue=0)
        self.checkbutton.place(x=200, y=100)

        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=220, y=170)

        btn_ok = ttk.Button(self, text='Accept', command=self.mesbox)
        btn_ok.place(x=130, y=170)
        btn_ok.bind('<Button-1>')


    def mesbox(self):
        if int(self.var.get()) == 1:
            messagebox.askyesno("Confirmation", 'Are you sure?')
        else:
            print("KEK")


class Child2(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Store joining')
        self.geometry('230x140+400+300')
        self.resizable(False, False)


        label1 = tk.Label(self, text='1-store')
        label1.place(x=20, y=20)

        label2 = tk.Label(self, text='2-store')
        label2.place(x=20, y=50)

        self.entry1 = ttk.Entry(self)
        self.entry1.place(x=80, y=20)

        self.entry2 = ttk.Entry(self)
        self.entry2.place(x=80, y=50)


        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=140, y=100)

        btn_ok = ttk.Button(self, text='OK')
        btn_ok.place(x=40, y=100)
        btn_ok.bind('<Button-1>')


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Navigation system")
    root.geometry('300x300+400+300')
    root.resizable(False, False)
    root.mainloop()