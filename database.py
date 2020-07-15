import sqlite3

conn = sqlite3.connect('strawberries.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Product (
				productID varchar PRIMARY KEY not null,
				phase varchar,
				status varchar,
				message text,
				image blob,
				temperature real)
			''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Test (
				fruit varchar,
				size varchar, 
				color varchar)
			''')

cursor.execute("Select * from Test")
print(cursor.fetchall())


conn.commit()
conn.close()