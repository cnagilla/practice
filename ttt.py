# Python code for Tic Tac Toe

def display_board(board):
    for index,i in enumerate(board):
        print('|{0: ^5}'.format(i),end='')
        if (index+1)%3==0: print('|')

def marker():
    global gmarkers
    p1_m = '#'
    while p1_m not in gmarkers:
        p1_m = input('Please enter your marker choice (X or O): ')
    if p1_m == 'X': p2_m = 'O'
    else: p2_m='X'
    return p1_m,p2_m

def position_choice(board,marker):
    global gmarkers
    choice = 0
    overriding = False
    while choice not in range(1,10):
        choice = int(input('Please make a position choice(1-9): '))
    if board[choice-1] in gmarkers:
        print('Invalid position')
        return position_choice(board,marker)
    board[choice-1]=marker
    return board

def isgameover(board):
    # check rows
    if board[0] == board[1] == board[2]:
        return True,board[0]
    if board[3] == board[4] == board[5]:
        return True,board[3]
    if board[6] == board[7] == board[8]:
        return True,board[6]
    
    # Check columns
    if board[0] == board[3] == board[6]:
        return True,board[0]
    if board[1] == board[4] == board[7]:
        return True,board[1]
    if board[2] == board[5] == board[8]:
        return True,board[2]
    
    # Check criss-cross
    if board[0] == board[4] == board[8]:
        return True,board[0]
    if board[6] == board[4] == board[2]:
        return True,board[6]
    return False,'None'





board = list('TICTACTEE')
gmarkers = ['X','O']
markers = marker()

i=0
game_complete = False
display_board(board)
while not game_complete:
    board = position_choice(board,markers[i%2])
    display_board(board)
    i+=1
    status = isgameover(board)
    game_complete = status[0]
print ('Winner is - {}'.format(status[1]))
