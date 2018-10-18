import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import *
import sys
import time
from tkinter import *
import logging
import sqlite3

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
        self.var1 = IntVar()
        self.r_button1 = tk.Radiobutton(self, text='Floor 1', variable=self.var1, value=1, command=self.floor_selection)
        self.r_button1.place(x=40, y=40)

        self.r_button2 = tk.Radiobutton(self, text='Floor 2', variable=self.var1, value=2, command=self.floor_selection)
        self.r_button2.place(x=140, y=40)

        self.entry_text = StringVar()
        self.entry = ttk.Entry(self, textvariable=self.entry_text)
        self.entry.place(x=40, y=130)

        self.combobox_value = StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.combobox_value, state='readonly')
        self.combobox.place(x=40, y=100)


        
        self.var2 = IntVar()
        self.checkbutton = tk.Checkbutton(self, text='Clean the store', variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton.place(x=200, y=100)

        

        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=220, y=170)

        btn_ok = ttk.Button(self, text='Accept', command=self.mesbox)
        btn_ok.place(x=130, y=170)
        btn_ok.bind('<Button-1>')
        

    # def current_time(self):
    #     return self.time.strftime('%H:%M:%S')

    # def tick(self):
    #     self.clock.after(200, self.tick)
    #     self.clock['text'] = self.current_time


    def floor_selection(self):
        a = self.var1.get()
        if a == 1:
            conn = sqlite3.connect('data_base.db')
            cursor = conn.cursor()
            find_stores = ('SELECT * FROM stores WHERE floor = 1')
            cursor.execute(find_stores)
            results = cursor.fetchall()
            self.stores = {}
            for result in results:
                key = str(result[0])
                value = result[2]
                self.stores[key] = value
            combobox_values = list(self.stores.keys())
            self.combobox.config(values=combobox_values)
            
   
        elif a == 2:
            conn = sqlite3.connect('data_base.db')
            cursor = conn.cursor()
            find_stores = ('SELECT * FROM stores WHERE floor = 2')
            cursor.execute(find_stores)
            results = cursor.fetchall()
            self.stores = {}
            for result in results:
                key = str(result[0])
                value = result[2]
                self.stores[key] = value
            combobox_values = list(self.stores.keys())
            self.combobox.config(values=combobox_values)
            

    def combobox_choose(self):
        self.entry_textvariable = StringVar(self, value=str(self.stores.get(self.combobox.get())))
        self.entry.config(textvariable=self.entry_textvariable)
            

    def mesbox(self):
        if int(self.var2.get()) == 1:
            if messagebox.askyesno("Confirmation", 'Are you sure?') == True:
                conn = sqlite3.connect('data_base.db')
                cursor = conn.cursor()
                query = query = 'UPDATE stores SET name = ?, o_date = ?, c_date = ?, username = ?, password = ? WHERE number = ?'
                new_name = 'none'
                cursor.execute(query, [(new_name), (''), (''), (''), (''), (self.combobox_value.get())])
                conn.commit()

        else:
            new_name = self.entry_text.get()
            print(new_name)
            print(self.combobox_value.get())
            conn = sqlite3.connect('data_base.db')
            cursor = conn.cursor()
            query = 'UPDATE stores SET name = ? WHERE number = ?'
            cursor.execute(query, [(new_name), (self.combobox_value.get())])
            conn.commit()


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

        self.entry_text1 = StringVar()
        self.entry_text2 = StringVar()

        self.entry1 = ttk.Entry(self, textvariable=self.entry_text1)
        self.entry1.place(x=80, y=20)

        self.entry2 = ttk.Entry(self, textvariable=self.entry_text2)
        self.entry2.place(x=80, y=50)


        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=140, y=100)

        btn_ok = ttk.Button(self, text='OK', command=self.joining)
        btn_ok.place(x=40, y=100)
        btn_ok.bind('<Button-1>')

    def joining(self):
        conn = sqlite3.connect('data_base.db')
        cursor = conn.cursor()
        find_stores = ('SELECT * FROM stores ')
        cursor.execute(find_stores)
        results = cursor.fetchall()
        self.stores = {}
        for result in results:
            key = str(result[0])
            value = result[2]
            if key !='' and value !='':
                self.stores[key] = value
        
        for key1, value1 in self.stores.items():
            
            if self.entry_text1.get() == key1:
                if value1 != 'none':
                    print("full") 
                    b = 1
                else:
                    print("empty")

            if self.entry_text2.get() == key1:
                if value1 == 'none':
                    print("EMPTY")
                    c = 2
                    
                else:
                    print("FULL")
        print(b + c)

           

            



            





if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Navigation system")
    root.geometry('300x300+400+300')
    root.resizable(False, False)
    root.mainloop()