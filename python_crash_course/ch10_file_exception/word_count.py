# 10.3.7
def count_words(filename):
	'''Calculate how many words a file contains'''
	try:
		with open(filename) as file_obj:
			contents = file_obj.read()
	except FileNotFoundError:
		msg = "The file '" + filename + "' does not exist!"
		print(msg)
	else:
		words = contents.split()	# 数组
		num_words = len(words)
		print("The file '" + filename + "' has about " + str(num_words)
			+ " words.")

filename = "alice_in_wonderland.txt"
count_words(filename)


