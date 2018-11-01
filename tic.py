board=[' ' for i in range(10)]

def insert_letter(letter,position):
    board[position] = letter
def space_is_free(position):
    if board[position] == ' ':
        return True
    else:
        return False
def print_board(board):
    print("  |  |  ")
    print(board[1]," |",board[2]," |",board[3],sep="")
    print("---------")
    print("  |  |  ")
    print(board[4]," |",board[5]," |",board[6],sep="")
    print("---------")
    print("  |  |  ")
    print(board[7]," |",board[8]," |",board[9],sep="")
    print("---------")
    

def is_winner(symbol):
    if (board[1] == symbol and board[2] == symbol and board[3] == symbol) or(board[4] == symbol)

def player_move():
    pass
def comp_move();
    pass

def select_random():
    pass
def is_full():
    pass


def main():
    


game_state = True
while game_state:
    main()
    a=input('do u want to play again\y\n')
    if a == n:
        game_state = False