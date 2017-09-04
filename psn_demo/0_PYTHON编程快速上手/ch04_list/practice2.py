# p79: char image grid, @20170110;

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def heartPrint(aList):
    for j in range(len(aList[0])):   # 0-5, last value in range is not included;
        for i in range(len(aList)):  # 0-8;
            print(aList[i][j], end='')
        print('')

heartPrint(grid)
