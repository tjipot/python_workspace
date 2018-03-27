# p101: a simple validation program, @20170110;

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Pls input a number for your age:')

while True:
    print('Select a new password, letters and numbers only:')
    password = input()
    if password.isalnum():
        break
    print('Pls input a password only with letters and numbers:')
