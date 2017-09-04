# @Nov 14, 2016 @HYe
# Process Pool
from  multiprocessing import Pool
import os, time, random

# Function that run as subprocess;
def long_time_task(name):
	print('Run task %s (%s)...' %(name, os.getpid()))
	start = time.time()				# Module Time function time(): start time;
	time.sleep(random.random() * 3)	# Generate random sleep time;
	end = time.time()   			# Finished Time;
	print('Task %s runs %0.2f seconds.' %(name, (end - start))) # Print out time period;

# If runs from this file;
if __name__ == '__main__':
	print('Parent process ID: %s.' %os.getpid()) # Current PID that running this statement;
	p = Pool(4)				# Create a pool containing 4 subprocesses: Pool(subprocess number);
	for i in range(5):		# Create 5 subprocesses;
		p.apply_async(long_time_task, args = (i,)) # Something like p=Process(target, args);
	print('Waiting for all subprocesses done...') # Although this line is after "apply_async" line, but it runs before that line, for the Python interpreter is not guaranteed the execution sequence of statement before all subprocesses is joined(p.join());
	p.close()	# close() must executed before join(): it tells Interpreter no subprocess could be added;
	p.join()	# When join() is called by a Pool object, the program will wait all subprocesses to be finished, after then, the following statements could run;
	print('All subprocesses finished.')

	# Running Result:
	# POSIX:desktop HY$ python3 1_pool.py    ## Terminal Command;
	# Parent process ID: 3008.
	# Waiting for all subprocesses done...
	# Run task 0 (3009)...
	# Run task 1 (3010)...
	# Run task 2 (3011)...
	# Run task 3 (3012)...
	# Task 0 runs 0.72 seconds.    ## After this line, task 4 could be run,
	# Run task 4 (3009)...         ## then prints out "Run task 4 ...";
	# Task 2 runs 0.78 seconds.
	# Task 1 runs 1.48 seconds.
	# Task 3 runs 1.97 seconds.
	# Task 4 runs 2.34 seconds.
	# All subprocesses finished.