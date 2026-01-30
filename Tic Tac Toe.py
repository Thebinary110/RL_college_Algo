import random

board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_win(p):
    win = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win:
        if board[a]==board[b]==board[c]==p:
            return True
    return False

def board_full():
    return ' ' not in board

def player_move():
    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos] == ' ':
        board[pos] = 'X'
    else:
        print("Invalid move")
        player_move()

def computer_move():
    free = [i for i in range(9) if board[i]==' ']
    pos = random.choice(free)
    board[pos] = 'O'

while True:
    print_board()
    player_move()

    if check_win('X'):
        print_board()
        print("You win!")
        break

    if board_full():
        print("Draw!")
        break

    computer_move()

    if check_win('O'):
        print_board()
        print("Computer wins!")
        break
