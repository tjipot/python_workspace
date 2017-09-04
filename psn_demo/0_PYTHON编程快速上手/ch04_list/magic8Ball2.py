# p70: randomly prints out one message, @20170110;

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

# New function: randint();
print(messages[random.randint(0, len(messages)-1)])
