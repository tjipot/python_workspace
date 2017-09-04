# p82: usage of a dict, stores a new birthday if not exists, @20170110;

birthdays = {'Alice':'Apr 1', 'Bob':'Dec 1', 'Carol':'Mar 4'}

while True:
    print('Enter a name, blank to quit:')
    name = input()
    if name == '':
        print('You are quited.')
        break   # Jump out of while loop; 
    if name in birthdays:
        print(name + "'s birthday is in " + birthdays[name] + '.')
    else:
        print('I don\'t have birthday infomation for ' + name + '.')
        print('What\'s ' + name + '\'s birthday? Pls type in:')
        bday = input()
        birthdays[name] = bday
        print(name + '\'s birthday is updated.')
