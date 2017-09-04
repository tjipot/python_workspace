#! /usr/bin/env python3
# p111: prints list of list of string in table, @20170111;
# printTable.py - prints the strings in a formatted table;

tableData = [['apples', 'cherries', 'oranges', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(aTable):
    colWidth = maxLen(aTable)
    for outIndex in range(len(aTable[0])):
        for inIndex in range(len(aTable)):
            if inIndex == 0:
                print(aTable[inIndex][outIndex].rjust(colWidth[inIndex], '*'), end='+')
            else:
                print(aTable[inIndex][outIndex].ljust(colWidth[inIndex], '*'), end='+')
        print('')

def maxLen(listOfList):
    colWidth = [0] * len(listOfList)
    for outListIndex in range(len(listOfList)):
        tmpLen = 0
        # print(colWidth)
        for inList in listOfList[outListIndex]:
            if tmpLen < len(inList):
                tmpLen = len(inList)
        colWidth[outListIndex] = tmpLen
        # print(colWidth[outListIndex])
        # print(tmpLen)
    return colWidth

printTable(tableData)

'''
Result:
**apples+Alice+dogs*+
cherries+Bob**+cats*+
*oranges+Carol+moose+
*bananas+David+goose+

'''