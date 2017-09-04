# p79: converts a list into a string in a formation, @20170110;
# Result string: 'apples, bananas, tofu, and cats';

spam = ['apples', 'bananas', 'tofu', 'cats']

def formatAppending(aList):
    string = ''
    for ele in aList[0:len(aList)-1]:   # Not including 'cats'
        string = string + ele + ', '
    string += 'and ' + aList[len(aList)-1]  # Including 'cats'
    return string

print(formatAppending(spam))
