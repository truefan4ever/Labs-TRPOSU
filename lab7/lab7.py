import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import *
import sys
import time
from tkinter import *
import sqlite3
from tkinter import messagebox as ms
from random import choice
from string import ascii_letters

string = ''
info = []


class Main(tk.Frame):
    """Creating start window"""
    def __init__(self, root):
        super().__init__(root)
        self.init_main()


    def init_main(self):
        # buttons
        btn1 = tk.Button(root, width=15, height=2, text="Guest", font='Times 16',command=self.open_dialog1) #creating the button
        btn1.place(x=60, y=20) #placing the button
        btn1['overrelief'] = GROOVE #button relief when the cursor is over it

        btn2 = tk.Button(root, width=15, height=2, text="Store Manager", font='Times 16', command=self.open_dialog2)
        btn2.place(x=60, y=100)
        btn2['overrelief'] = GROOVE

        btn3 = tk.Button(root, width=15, height=2, text="Admin", font='Times 16',command=self.open_dialog3)
        btn3.place(x=60, y=180)
        btn3['overrelief'] = GROOVE

        
    def open_dialog1(self):
        """Openning Guest`s window"""
        Guest()


    def open_dialog2(self):
        """Openning Manager`s window"""
        ManagerLogIn()

    def open_dialog3(self):
        """Openning Admin`s window"""
        AdminLogIn()


class Guest(tk.Toplevel):
    """Guest`s window"""
    def __init__(self):
        super().__init__(root)
        self.init_child()

        
    def init_child(self):
        self.title('Navigation system') #the title of the window
        self.geometry('300x300+400+300') #the size
        self.resizable(False, False) #the window is not resizable

        self.number = StringVar()
        self.name = StringVar()

        #entries
        self.entry_number = tk.Entry(self, textvariable=self.number) #creating the entry widget
        self.entry_number.place(x=20, y=45) #pacing the entry widget
        self.entry_number['state'] = DISABLED #widget state

        self.entry_name = tk.Entry(self, textvariable=self.name)
        self.entry_name.place(x=20, y=155)
        self.entry_name['state'] = DISABLED

        #labels
        label_description = tk.Label(self, text='Enter the number:') #creating the label
        label_description.place(x=20, y=10) #palcing the label

        label_name_store = tk.Label(self, text='Enter the name:')
        label_name_store.place(x=20, y=120)

        self.label_info1 = tk.Label(self)
        self.label_info1.place(x=20, y=85)

        self.label_info2 = tk.Label(self)
        self.label_info2.place(x=20, y=180)

        #buttons
        self.btn_info = ttk.Button(self, text="Info", command=self.info_pressed)
        self.btn_info.place(x=200, y=45)
        self.btn_info.bind('<Button-1>')
        self.btn_info['state'] = DISABLED

        self.btn_find = ttk.Button(self, text="Find", command=self.find_pressed)
        self.btn_find.place(x=200, y=155)
        self.btn_find.bind('<Button-1>')
        self.btn_find['state'] = DISABLED

        btn_db = ttk.Button(self, text='Database', command=self.data_base)
        btn_db.place(x=100, y=250)
        btn_db.bind('<Button-1>')

        self.stores = {}

        self.bell()
        self.grab_set() 
        self.focus_set()
  

    def info_pressed(self):
        """Finding the number of the store in the dictionary"""
        try:
            for key, value in self.stores.items():
                if int(self.number.get()) == int(key):
                    self.label_info1.config(text=value.title()) #updating the label
        except ValueError:
            message = "Please enter correct number\n(1-st floor: 1**, 2-nd floor: 2**)"
            self.label_info1.config(text=message)


    def find_pressed(self):
        """Finding the name of the store in the dictionary"""
        for key, value in self.stores.items():
            if str(self.name.get()) == str(value):
                if int(key) < 106:
                    self.label_info2.config(text="Floor-1, store number: " + str(key))                
                elif int(key) > 106 and int(key) < 206:
                        self.label_info2.config(text="Floor-2, store number: " + str(key))
                break
            else:
                message = "Check the name!"
                self.label_info2.config(text=message)
        

    def data_base(self):
        """Working with the database"""
        self.entry_name['state'] = NORMAL #entry`s state
        self.entry_number['state'] = NORMAL
        self.btn_info['state'] = NORMAL #button`s state
        self.btn_find['state'] = NORMAL
        conn = sqlite3.connect('data_base.db') #making the connection with the database
        cursor = conn.cursor()
        query = 'SELECT number, name FROM stores' #SQL query to the database
        cursor.execute(query)
        data = cursor.fetchall() #getting data from the database
        for line in data: #writing data from the database to the dictionary
            key = str(line[0])
            value = line[1]
            if key != '' and value != '':
                self.stores[key] = value

        
class ManagerLogIn(tk.Toplevel):
    """Manager`s login window"""
    def __init__(self):
        super().__init__(root)
        self.init_child()
        
        
    def init_child(self):
        self.title('Store Manager')
        self.geometry('230x140+400+300')
        self.resizable(False, False)

        #labels
        label1 = tk.Label(self, text='Name:')
        label1.place(x=20, y=20)

        label2 = tk.Label(self, text='Password:')
        label2.place(x=20, y=50)

        self.username = StringVar()
        self.password = StringVar()
        
        #entries
        self.entry1 = ttk.Entry(self, textvariable=self.username)
        self.entry1.place(x=80, y=20)

        self.entry2 = ttk.Entry(self, textvariable=self.password, show="*")
        self.entry2.place(x=80, y=50)

        #buttons
        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=140, y=100)

        btn_ok = ttk.Button(self, text='OK', command=self.open_dialog4)
        btn_ok.place(x=40, y=100)
        btn_ok.bind('<Button-1>')

        self.bell()
        self.grab_set()
        self.focus_set()


    def open_dialog4(self):
        """Autentication, finding the name and the password in database """
        with sqlite3.connect('data_base.db') as db:
            cursor = db.cursor()
        find_user = ('SELECT * FROM stores WHERE username = ? and password = ?')
        cursor.execute(find_user, [(self.username.get()), (self.password.get())])
        result = cursor.fetchall()
        if result:
            global string
            string = ''.join(choice(ascii_letters) for i in range(12))
            print(string)
            query = 'UPDATE stores SET random_string = ? WHERE username = ?'
            cursor.execute(query, [(string), (self.username.get())])
            db.commit()
            ManagerWindow()
            self.destroy()
        else:
            ms.showerror('Authentication Error!!', 'User not found.\nCheck the name and the password!')


class AdminLogIn(tk.Toplevel):
    """Admin`s login window"""
    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        self.title('Admin')
        self.geometry('230x140+400+300')
        self.resizable(False, False)

        #labels
        label1 = tk.Label(self, text='Login:')
        label1.place(x=20, y=20)

        label2 = tk.Label(self, text='Password:')
        label2.place(x=20, y=50)

        self.login = StringVar()
        self.password = StringVar()

        #entries
        self.entry1 = ttk.Entry(self, textvariable=self.login)
        self.entry1.place(x=80, y=20)

        self.entry2 = ttk.Entry(self, textvariable=self.password, show="*")
        self.entry2.place(x=80, y=50)

        #buttons
        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=140, y=100)

        btn_ok = ttk.Button(self, text='OK', command=self.open_dialog5)
        btn_ok.place(x=40, y=100)
        btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


    def open_dialog5(self):
        """Atentication"""
        with sqlite3.connect('data_base.db') as db:
            cursor = db.cursor()
        find_user = ('SELECT * FROM stores WHERE username = ? and password = ?')
        cursor.execute(find_user, [(self.login.get()),(self.password.get())])
        result = cursor.fetchall()
        if result:
            self.destroy()
            AdminWindow()
        else:
            ms.showerror('Authentication Error!', 'Check the login and the password!')


class ManagerWindow(tk.Toplevel):
    """Manager`s window"""
    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        self.title('Store Manager')
        self.geometry('230x200+400+300')
        self.resizable(False, False)

        #labels
        self.label1 = tk.Label(self)
        self.label1.place(x=20, y=10)

        self.label2 = tk.Label(self)
        self.label2.place(x=20, y=30)

        self.label3 = tk.Label(self)
        self.label3.place(x=20, y=50)

        self.label4 = tk.Label(self)
        self.label4.place(x=20, y=70)

        self.label5 = tk.Label(self)
        self.label5.place(x=20, y=90)

        self.label6 = tk.Label(self)
        self.label6.place(x=20, y=110)

        #buttons
        self.btn_state_change = tk.Button(self, text="Change the state", command=self.open_dialog1)
        self.btn_state_change.place(x=20, y=160)

        self.btn_join_stores = tk.Button(self, text="Join stores", command=self.open_dialog2)
        self.btn_join_stores.place(x=140, y=160)

        conn = sqlite3.connect('data_base.db')
        cursor = conn.cursor()
        find_info = ('SELECT * FROM stores WHERE random_string = ?')
        cursor.execute(find_info, [(string)])
        results = cursor.fetchall()
        for result in results:
            for res in result:
                global info
                info.append(res)
        self.label1.config(text="Store name: " + info[2].title())
        self.label2.config(text="Store number: " + str(info[0]))
        self.label3.config(text="Floor: " + str(info[1]))
        self.label4.config(text="Openning date: " + str(info[4]))
        self.label6.config(text="Size: " + str(info[3]))
        if str(info[5]) == '':
            message = " it`s still working"
            self.label5.config(text="Closing date: " + message)
        else:
            self.label5.config(text="Closing date: " + str(info[5]))
        
        self.grab_set()
        self.focus_set()


    def open_dialog1(self):
        """Runnig the state changing window"""
        StateChanging()


    def open_dialog2(self):
        """Running the store joining window"""
        if info[-1] == 0:  
            ms.showerror('Error!!', 'You can`t join the next empty\n store to yours, because it`s\n not empty!')
        else:
            StoreJoining()


class StateChanging(tk.Toplevel):
    """State changing window"""
    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        self.title('State changing')
        self.geometry('330x220+400+300')
        self.resizable(False, False)

        #labels
        label1 = tk.Label(self, text='Your store`s name: ' + info[2].title())
        label1.place(x=20, y=10)

        label2 = tk.Label(self, text='Enter a new name or delete the store:')
        label2.place(x=20, y=40)

        #entries
        self.entry_text = StringVar()
        self.entry = ttk.Entry(self, textvariable=self.entry_text)
        self.entry.place(x=20, y=70)

        self.var2 = IntVar()

        #checkbuttons
        self.checkbutton = tk.Checkbutton(self, text='Delete the store', variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton.place(x=180, y=70)

        #buttons
        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=220, y=170)

        btn_ok = ttk.Button(self, text='Accept', command=self.mesbox)
        btn_ok.place(x=130, y=170)
        btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


    def mesbox(self):
        """Deleting the store or updating its name"""
        if int(self.var2.get()) == 1:
            if messagebox.askyesno("Confirmation", 'Are you sure?') == True:
                conn = sqlite3.connect('data_base.db')
                cursor = conn.cursor()
                query = query = 'UPDATE stores SET name = ?, o_date = ?, c_date = ?, username = ?, password = ?, joining = ? WHERE number = ?'
                new_name = 'none'
                cursor.execute(query, [(new_name), (''), (''), (''), (''), (''), (info[0])])
                conn.commit()
            self.destroy()
        else:
            new_name = self.entry_text.get()
            print(new_name)
            conn = sqlite3.connect('data_base.db')
            cursor = conn.cursor()
            query = 'UPDATE stores SET name = ? WHERE number = ?'
            cursor.execute(query, [(new_name), (info[0])])
            conn.commit()
            self.destroy()


class StoreJoining(tk.Toplevel):
    """Store joining window"""
    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        self.title('Store joining')
        self.geometry('230x140+400+300')
        self.resizable(False, False)

        #labels
        label2 = tk.Label(self, text='You can join the next empty\n store to yours.')
        label2.place(x=30, y=20)

        #buttons
        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=140, y=100)

        btn_ok = ttk.Button(self, text='Join', command=self.joining)
        btn_ok.place(x=40, y=100)
        btn_ok.bind('<Button-1>')
        
        self.grab_set()
        self.focus_set()

    def joining(self):
        """Joining the stores and updating the database"""
        conn = sqlite3.connect('data_base.db')
        cursor = conn.cursor()
        query = ('UPDATE stores SET size = ? WHERE number = ?')
        cursor.execute(query, [(2), (info[0])])
        conn.commit()
        delete = ('DELETE FROM stores WHERE number = ?')
        delete_data = info[0] + 1
        cursor.execute(delete, [delete_data])
        conn.commit()
        query2 = ('UPDATE stores SET number = ? WHERE number = ?')
        cursor.execute(query2, [(info[0] + 1), (info[0] + 2)])
        conn.commit()
        self.destroy()


class AdminWindow(tk.Toplevel):
    """Admin`s window"""
    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        self.title('Admin')
        self.geometry('230x140+400+300')
        self.resizable(False, False)

        #labels
        label1 = tk.Label(self, text='This is admin window:')
        label1.place(x=20, y=20)

        #buttons
        btn_show = ttk.Button(self, text='DB info', command=self.show)
        btn_show.place(x=20, y=50)

        btn_change = ttk.Button(self, text="Change the store state", command=self.open_dialog1)
        btn_change.place(x=20, y=80)

        btn_info = ttk.Button(self, text='Store info', command=self.open_dialog2)
        btn_info.place(x=20, y=110)

        self.bell()
        self.grab_set()
        self.focus_set()


    def open_dialog1(self):
        """Running admin`s state changing window"""
        AdminWindow2()


    def open_dialog2(self):
        """Running guest`s window with information"""
        Guest()


    def show(self):
        """Printing all the information about the database in the console"""
        conn = sqlite3.connect('data_base.db')
        cursor = conn.cursor()
        query = ("SELECT * FROM stores")
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)
        

class AdminWindow2(tk.Toplevel):
    """Admin`s state changing window"""
    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        self.title('State changing')
        self.geometry('330x220+400+300')
        self.resizable(False, False)

        #labels
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

        #entries
        self.entry_text = StringVar()
        self.entry = ttk.Entry(self, textvariable=self.entry_text)
        self.entry.place(x=40, y=130)

        #comboboxes
        self.combobox_value = StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.combobox_value, state='readonly')
        self.combobox.place(x=40, y=100)

        #checkbuttons
        self.var2 = IntVar()
        self.checkbutton = tk.Checkbutton(self, text='Clean the store', variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton.place(x=200, y=100)

        #buttons
        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=220, y=170)

        btn_ok = ttk.Button(self, text='Accept', command=self.mesbox)
        btn_ok.place(x=130, y=170)
        btn_ok.bind('<Button-1>')

        self.bell()
        self.grab_set()
        self.focus_set()
        

    def floor_selection(self):
        """Floor selection by the radiobutton"""
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
            

    def mesbox(self):
        """Deleting the store or updating its name"""
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


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Start page")
    root.geometry('300x300+400+300')
    root.resizable(False, False)
    root.mainloop()
