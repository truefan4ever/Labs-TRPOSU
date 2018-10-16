import sqlite3

# Connection with data base, if data base doesn`t exist, it will be created
conn = sqlite3.connect("dana_mall.db")

# Creating cursor model
cursor = conn.cursor()

# Creating table, if it daesn`t exist, it will be created
cursor.execute('CREATE TABLE IF NOT EXISTS shopping_center(Store INTEGER, Name TEXT)')


stores = [(101, "samsung"),
		  (102, "xiaomi"),
          (103, "green"),
          (104, "none"),
          (105, "none"),
          (201, "zara"),
          (202, "pull&bear"),
          (203, "bershka"),
          (204, "nike"),
          (205, "none")]

cursor.executemany("INSERT INTO shopping_center VALUES (?,?)", stores)
conn.commit()

cursor.close()
conn.close()