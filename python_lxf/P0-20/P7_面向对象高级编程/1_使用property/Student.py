# @property用法

class Student(object):
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('Score Must Be An Integer!')
		if value < 0 or value > 100:
			raise ValueError('Score Must Between 0 And 100')
		self._score = value

	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self, value):
		self._birth = value

	# age: Readonly Property
	@property
	def age(self):
		return 2016 - self._birth