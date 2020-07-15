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

				db_fields = []
				keys = []
				for data in strawberries_data:
					keys = list(data.keys())
					for k in keys:
						if k not in db_fields:
							db_fields.append(k)

				for data in strawberries_data:
					columns = ''
					values = ''
					for i, f in enumerate(db_fields):
						print("f: " + f)
						#print("data: " + str(data))
						#print("keys:" + str(data.keys()))
						curr_value = str(data[f])
						print("value:" + curr_value)
						if i == 0:
							columns += f'{f}'
							values += f'\'{curr_value}\''
						else:
							columns += f', {f}'
							values += ', '
							values += f'\'{curr_value}\''

					print("columns:" + columns)
					print("values:" + values)
					query = (f'INSERT INTO Product ({columns}) VALUES ({values})') 
					cursor.execute(query)

s = strawberries_registry()
print(s.insert_strawberries_data())