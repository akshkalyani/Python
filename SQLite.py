#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")


# In[2]:


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print("Table created successfully")

conn.close()


# In[3]:


import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print("Records created successfully")
conn.close()


# In[5]:


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()


# In[7]:


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()


# In[8]:


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print( "ID = ", row[0])
   print( "NAME = ", row[1])
   print( "ADDRESS = ", row[2])
   print( "SALARY = ", row[3], "\n")

print("Operation done successfully");
conn.close()


# In[1]:


CREATE TABLE [Departments] (
	[DepartmentId] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
    [DepartmentName] NVARCHAR(50)  NULL
);
CREATE TABLE [Students] (
	[StudentId] INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
	[StudentName] NVARCHAR(50)  NULL,
	[DepartmentId] INTEGER  NOT NULL,
	[DateOfBirth] DATE  NULL,
	FOREIGN KEY(DepartmentId) REFERENCES Departments(DepartmentId)
);


# In[2]:


import sqlite3

conn = sqlite3.connect('test1.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE Departments
         (DepartmentID INT PRIMARY KEY     NOT NULL,
         DepartmentNAME           TEXT    NOT NULL);''')
print("Table created successfully")

conn.execute('''CREATE TABLE Students
         (StudentID INT PRIMARY KEY     NOT NULL,
         StudentNAME           TEXT    NOT NULL, DepartmentID INT NOT NULL, DateOfBirth DATE NULL,FOREIGN KEY(DepartmentId) REFERENCES Departments(DepartmentId) );''')
print("Table created successfully")

conn.close()


# In[6]:


import sqlite3

conn = sqlite3.connect('test1.db')
print("Opened database successfully")

conn.execute("INSERT INTO Departments (DepartmentID,DepartmentNAME)       VALUES (101, 'CTech')");

conn.execute("INSERT INTO Departments (DepartmentID,DepartmentNAME)       VALUES (102, 'CINTEL')");
conn.execute("INSERT INTO Departments (DepartmentID,DepartmentNAME)       VALUES (103, 'DSBS')");
conn.execute("INSERT INTO Departments (DepartmentID,DepartmentNAME)       VALUES (104, 'NWC')");

conn.commit()
print("Records created successfully")
conn.close()


# In[7]:


import sqlite3

conn = sqlite3.connect('test1.db')
print("Opened database successfully")

conn.execute("INSERT INTO Students (StudentID,StudentNAME, DepartmentID, DateOfBirth)       VALUES (1001, 'RAM',101,14-03-1998 )");


conn.commit()
print("Records created successfully")
conn.close()


# In[8]:


import sqlite3

conn = sqlite3.connect('test1.db')
print("Opened database successfully")

conn.execute("INSERT INTO Students (StudentID,StudentNAME, DepartmentID, DateOfBirth)       VALUES (1002, 'SAM',101,14-03-1997 )");
conn.execute("INSERT INTO Students (StudentID,StudentNAME, DepartmentID, DateOfBirth)       VALUES (1003, 'kapoor',101,14-02-1998 )");
conn.execute("INSERT INTO Students (StudentID,StudentNAME, DepartmentID, DateOfBirth)       VALUES (1004, 'Arun',101,14-01-1998 )");

conn.commit()
print("Records created successfully")
conn.close()


# In[2]:


import sqlite3

conn = sqlite3.connect('test1.db')
print("Opened database successfully")

conn.execute("INSERT INTO Students (StudentID,StudentNAME, DepartmentID, DateOfBirth)       VALUES (1005, 'KAM',105,14-03-1997 )");


conn.commit()
print("Records created successfully")
conn.close()


# In[3]:


import sqlite3

conn = sqlite3.connect('test1.db')
print("Opened database successfully")

conn.execute("INSERT INTO Students (StudentID,StudentNAME, DepartmentID, DateOfBirth)       VALUES (1006, 'KAM',108,14-03-1997 )");


conn.commit()
print("Records created successfully")
conn.close()


# In[ ]:




