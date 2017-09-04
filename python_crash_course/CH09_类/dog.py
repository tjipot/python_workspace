""" 类定义和执行语句会在同一个PY解释器环境中'运行' """
class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age  = age

	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over!")

""" 执行语句 """
my_dog = Dog('Willie', 6);
print("My dog's name is " + my_dog.name.title() + ".");
print("My dog is " + str(my_dog.age) + " years old");