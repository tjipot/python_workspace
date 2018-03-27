'''用with打开一个文件时, 让Python解释器处理文件的open和close'''
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
"""删除因EOF而产生的空字串(显示时为空行)"""