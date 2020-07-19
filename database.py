import sqlite3

conn = sqlite3.connect('strawberries.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Product (
				product_ID varchar not null,
				phase varchar,
				status varchar,
				message text,
				image blob,
				temperature real)
			''')

cursor.execute("Select * from Product")
print(cursor.fetchall())


conn.commit()
conn.close()