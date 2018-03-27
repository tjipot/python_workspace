# p88: modeling tictactoe, but without win/lose judgement, @20170110;

theBoard = {'topL':' ', 'topM':' ', 'topR':' ',
            'midL':' ', 'midM':' ', 'midR':' ',
            'lowL':' ', 'lowM':' ', 'lowR':' '}

'''theBoard = {'topL':'O', 'topM':'O', 'topR':'O',
            'midL':'X', 'midM':'X', 'midR':' ',
            'lowL':' ', 'lowM':' ', 'lowR':'X'}'''

def boardPrint(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

turn = 'X'
for i in range(9):  # Not including 9;
    boardPrint(theBoard)
    print('Turn for ' + turn + ', move which space(e.g. \'topL\')?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

boardPrint(theBoard)
