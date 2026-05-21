import sqlite3

connection = sqlite3.connect('sales.db')
cursor = connection.cursor()

cursor.execute('''
create table if not exists sales(
               id integer primary key autoincrement,
               product_name text not null,
               quantity integer not null,
               price real not null,
               sale_date text not null)
''')

sales_data = [
    ('Laptop', 2, 1200.00, '2024-01-15'),
    ('Smartphone', 5, 800.00, '2024-01-20'),
    ('Headphones', 10, 150.00, '2024-01-25'),
    ('Tablet', 3, 500.00, '2024-01-30'),
    ('Smartwatch', 4, 200.00, '2024-02-05')
]

cursor.executemany('''
insert into sales(product_name, quantity, price, sale_date) values(?,?,?,?)''', sales_data)
connection.commit()


cursor.execute('select * from sales')
rows = cursor.fetchall()
for row in rows:
    print(row)
