filename = "alice_in_wonderland.txt"

# 10.3.5
# with open(filename) as file_obj:
# 	contents = file_obj.read()

# Codes with try-except:
# try:
# 	with open(filename) as file_obj:
# 		contents = file_obj.read()
# except FileNotFoundError:
# 	msg = "Sorry, the file '" + filename + "' does not exits!"
# 	print(msg)

# 10.3.6
title = "alice_in_wonderland.txt"

try:
	with open(filename) as file_obj:
		contents = file_obj.read()
except FileNotFoundError:
	errorMsg = "Sorry, the file " + filename + " does not exist!"
	print(errorMsg)
else:
	# Calculate Word Count
	words = contents.split()
	num_words = len(words)
	print("'alice_in_wonderland.txt' contains about " + str(num_words) + " words.")

