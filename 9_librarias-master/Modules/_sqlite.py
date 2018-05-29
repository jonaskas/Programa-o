"""
sqlite
"""

import sqlite3
import os

conn = sqlite3.connect(':memory:') # Create a database in RAM
#conn = sqlite3.connect(filePath)

cursor = conn.cursor()
cursor.execute("""CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
    phone TEXT, email TEXT unique, password TEXT)""")

students = [ 
    ["Student1", "123456789", "student1@email.com", "123456"],
    ["Student2", "987654321", "student2@email.com", "654321"]]

query = """INSERT INTO users(name, phone, email, password)
    VALUES ({})""".format(",".join(["'" + x + "'" for x in students[0]]))
cursor.execute(query)

print(query, cursor.lastrowid)

query = """INSERT INTO users(name, phone, email, password)
    VALUES ({})""".format(",".join(["'" + x + "'" for x in students[1]]))
cursor.execute(query)

print(query, cursor.lastrowid)

print()
cursor.execute("""SELECT * FROM users""")
for row in cursor.fetchall():
    print('{}: {}, {}, {}'.format(row[0], row[1], row[2], row[3]))

conn.commit()

id = 1

print()
query = """UPDATE users SET password= 'ABCDEF', email='newemail@newemail.com' WHERE id = {}""".format(id)
cursor.execute(query)

cursor.execute("""SELECT * FROM users WHERE id={}""".format(id))
userInfo = cursor.fetchone()
print(userInfo)

print()
query = """DELETE FROM users WHERE id = 1"""
cursor.execute(query)

cursor.execute("""SELECT * FROM users""")
for row in cursor: # same as for row in cursor.fetchall():
    print('{}: {}, {}, {}'.format(row[0], row[1], row[2], row[3]))

conn.commit()

conn.close()

filePath = os.path.join('_temp', 'mydatabase.db')
try:
    db = sqlite3.connect(filePath)
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER
        PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, 
        password TEXT)""")
    db.commit()
except Exception as e:
    db.rollback()
    raise e
finally:
    db.close()
