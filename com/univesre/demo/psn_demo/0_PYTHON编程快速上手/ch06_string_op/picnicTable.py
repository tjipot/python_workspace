# p104: prints out picnic food list in the form of a table , @20170110;

def picnicPrint(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for key, value in itemsDict.items():
        print(key.ljust(leftWidth,'.') + str(value).rjust(rightWidth, '.'))

picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':8000}

picnicPrint(picnicItems, 12, 5)
picnicPrint(picnicItems, 16, 6)

'''
Results:
---PICNIC ITEMS--
apples.........12
cups............4
sandwiches......4
cookies......8000
-----PICNIC ITEMS-----
apples..............12
cups.................4
sandwiches...........4
cookies...........8000
'''
