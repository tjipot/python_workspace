# p64: how to use list, @20170110;

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)+1) + ', or enter nothing to stop:')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]    # list concatenation

print('The cat names are:', end='')
for cat in catNames:
    print(' ' + cat, end='')
