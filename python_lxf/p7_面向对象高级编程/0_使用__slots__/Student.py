class Student(object):
	# Using tuple, Define Attributes Name That Can Be Binded;
	__slots__ = ('name', 'age')
	
class GraduateStudent(Student):
	pass