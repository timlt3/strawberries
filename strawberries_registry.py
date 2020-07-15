import json
import sqlite3

class strawberries_registry:
	def __init__(self):
		self._db_path = 'strawberries.db'

	def insert_strawberries_data(self):

		with sqlite3.connect(self._db_path) as connection:
			cursor = connection.cursor()

			with open('test.json') as f:
				strawberries_data = json.loads(f.read())

				print(strawberries_data)

				columns = ''
				values = ''
				for i, key in enumerate(strawberries_data):
					print("data:" + key)
					print("value:" + strawberries_data[key])
					if i == 0:
						columns += f'{key}'
						values += f'\'{strawberries_data[key]}\''
					else:
						columns += f', {key}'
						values += ', '
						values += f'\'{strawberries_data[key]}\''

				print("columns:" + columns)
				print("values:" + values)
				query = (f'INSERT INTO Test ({columns}) VALUES ({values})') 
				cursor.execute(query)

s = strawberries_registry()
print(s.insert_strawberries_data())