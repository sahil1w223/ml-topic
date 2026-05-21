import sqlite3

connection = sqlite3.connect('database.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()


# Create a table named 'users' if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')
connection.commit()

# Insert data into the 'users' table
cursor.execute("insert into users(id,name,email) values(1,'John Doe','john.doe@example.com')")
connection.commit()

# Query the 'users' table to retrieve all records
cursor.execute("select * from users")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("insert into users(id,name,email) values(2,'Jane Smith','jane.smith@example.com')")
connection.commit()

cursor.execute("select * from users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# delete a record from the 'users' table
cursor.execute("delete from users where id=1")
connection.commit()

cursor.execute("select * from users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update a record in the 'users' table
cursor.execute("update users set name='Jane Doe' where id=2")
connection.commit()

cursor.execute("select * from users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the database connection
connection.close()