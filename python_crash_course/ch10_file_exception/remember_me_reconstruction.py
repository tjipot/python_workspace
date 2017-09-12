# 10.4.3 重构: 功能分块

import json

def get_stored_username():
	"""如果存储了用户名, 就获取它"""
	filename = "username.json"
	try:
		with open(filename, 'r') as file_obj:
			username = json.load(file_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""提示输入用户名"""
	username = input("What's your name?")
	filename = 'username.json'
	with open(filename, 'w') as file_obj:
		json.dump(username, file_obj)
	return username

def greet_user():
	"""问候用户, 并指出名字"""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")


greet_user()