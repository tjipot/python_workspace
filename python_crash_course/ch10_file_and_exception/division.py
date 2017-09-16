# 10.3 异常

# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You can't divide by zero!")

# 10.3.3
# print("Give me two numbers, I'll divide them!")
# print("Enter 'q' to quit.")

# while True:
# 	first_number = input("\nFirst Number:")
# 	if first_number == 'q':
# 		break
# 	second_number = input("Second Number:")
# 	if second_number == 'q':
# 		break
# 	answer = int(first_number) / int(second_number)
# 	print(answer)


# 10.3.4
print("Give me two numbers, I'll divide them!")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst Number:")
	if first_number == 'q':
		break
	second_number = input("Second Number:")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You are dividing a number by zero!")
	else:
		print(answer)
