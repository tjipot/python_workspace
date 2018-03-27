import json

filename = 'number.json'
with open(filename, 'r') as file_obj:
	numbers = json.load(file_obj)

print(numbers)
 