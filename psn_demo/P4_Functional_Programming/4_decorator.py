def log(func):
	def wrapper(*args, **kw):
		print('call %s():' %(func.__name__))
		return func(*args, **kw)
	#print('wrapper() Finished')
	return wrapper

@log
def now():
	print("2016-11-12")