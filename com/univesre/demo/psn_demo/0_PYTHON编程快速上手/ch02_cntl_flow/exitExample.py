# p41, demo of the usage of sys.exit(): the system call, @20170108;

import sys

print("Type 'exit' to exit:")
while True:
    response = input()
    if response == 'exit':
        sys.exit()  # Return to the OS;
    print('You typed \'' + response + '\',', end = ' ')
    print("Type 'exit' to exit:" )
