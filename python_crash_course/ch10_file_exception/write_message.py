# 10.2 写入文件
filename = "programming.txt"

with open(filename, 'a') as file_object:
	file_object.write("\nI love Python C!")
	file_object.write("\nI love Python Java!")
	file_object.write("\nI also love finding meaning in large datasets.")
	file_object.write("\nI love creating apps that can run in a browser.")