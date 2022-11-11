#!/usr/bin/python

import sqlite3
conn = sqlite3.connect('test.db')
print("Database created")

conn.execute('''CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL
USERNAME    TEXT
NAME    TEXT
AGE INT);''')

print ('table created successfully')

conn.execute('''INSERT INTO COMPANY(ID,USERNAME,NAME,AGE)\
values(10123, akhs, Aksh Kalyani, 21''')

conn.commit()
print("Records updated")
conn.close()