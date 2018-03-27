# @Nov 11, 2016 @HYe
import os

print('Process (%s) start...' %os.getpid())
#从此步由两个进程分别执行了之后的代码了?!;
pid = os.fork() #fork()有两个返回, 0(子进程返回0=pid)和子进程id(父进程返回子进程id=pid), 终于搞懂了!;
if pid == 0:
	# 如果是0, 说明是由子进程返回(并执行), 由子进程执行中; pid就是process id的简写;
	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
	# 如果不是0, 说明由fork()返回的是父进程(是子进程ID值), 此时pid=fork()就是子进程ID(即下面的pid), 而os.getpid()就是子进程的
	print('I (%s) just created a child process (%s).' %(os.getpid(), pid))