# p10, this program asks for name and age, @20170108;

print('Hello, ', end = '')
print('What\'s your name?')
myName = input()
print('It\'s good to meet you, ' + myName + '!')
print('The length of your name is: ', end = '')
print(len(myName))

print('What\'s your age?')
myAge = input()
print('Your age is ' + myAge, end = ', ')
print('And you will be ' + str(int(myAge)+1) + ' in one year.')
