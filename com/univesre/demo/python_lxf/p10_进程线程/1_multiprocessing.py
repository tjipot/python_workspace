# @Nov 14, 2016 @HYe
# Multi_Process

from multiprocessing import Process
import os

# Codes of subprocess
def run_proc(name):
	print('Running Child Process %s (%s)...' %(name, os.getpid()))

if __name__ == '__main__': # '__name__' is this module's attribute, Python Interpreter will set this attribute the value of '__main__' if the program runs from this file; 
	print('Parent Process %s.' %os.getpid()) # Get process id(pid), module os's functionality;
	p = Process(target=run_proc, args=('test',)) # Create a process with two args: the underlying function, the args of that function;
	print('Child Process Will Start')
	p.start() # Start of a process
	print('Test Expression..')
	p.join() # Wait until the finish of subprocess: synchronization between processes;
	print('Child Process Ended.')

	# Results when comment out p.join():
	# Parent Process 2713.
	# Child Process Will Start
	# Test Expression..
	# Child Process Ended.
	# Running Child Process test (2714)...