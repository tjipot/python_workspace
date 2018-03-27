# p85: counts the number of each character in a paragraph, @20170110;

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
''' Result: {'e': 5, 'w': 2, 'a': 4, 'n': 4, 'k': 2, 'g': 2, ' ': 13,
    'r': 5, 'A': 1, 't': 6, '.': 1, 'h': 3, 'y': 1, 's': 3, 'i': 6,
    'p': 1, 'b': 1, 'o': 2, 'c': 3, 'd': 3, 'l': 3, ',': 1, 'I': 1}'''
