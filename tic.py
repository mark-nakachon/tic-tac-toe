
import os

board=[' ' for i in range(10)]

def insert_letter(letter,position):
    board[position] = letter
def space_is_free(position):
    if board[position] == ' ':
        return True
    else:
        return False
def print_board():
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
    if (board[1] == symbol and board[2] == symbol and board[3] == symbol) or(board[4] == symbol and board[5] == symbol and board[6] == symbol) or (board[7] == symbol and board[8] == symbol and board[9] == symbol) or (board[1] == symbol and board[4] == symbol and board[7] == symbol) or(board[2] == symbol and board[5] == symbol and board[8] == symbol) or (board[3] == symbol and board[6] == symbol and board[9] == symbol) or (board[1] == symbol and board[5] == symbol and board[9] == symbol) or(board[3] == symbol and board[5] == symbol and board[7] == symbol):
        return True
    return False
       
def player_move():
    while True:
        a = input("enter a choice to place X:")
        try:
            a = int(a)
            if a == 0:
                print("sry enter between 1 to 9")
            if a >= 1 and a<=9 and space_is_free(a):
                return a
            else:
                print("sorry enter a correct position and number")
        except:
            print("sorry enter a correct number between 1 to 9")
        


def comp_move():
   #AI algorithm comes 
   # case 1:
    possible_moves = [x for x , c in enumerate(board) if x!=0 and c == ' ']

    board_copy = board[:]
    for i in ['O','X']:
        for j in possible_moves:
            board_copy[j] = i
            if is_winner(i):
                return j
            else:
                board_copy = ' '
    corners = [1,3,7,9]
    # check corners
    corners_open = []
    for i in possible_moves:
        if i in corners:
            corners_open.append(i)
    
    if len(corners_open > 0):
        return select_random(corners_open)

    edges = [2,4,6,8]
    edges_open =[]
    # check edges
    for i in possible_moves:
        if i in edges:
            edges_open.append(i)
    if len(edges_open > 0):
        return select_random(edges_open)

    # check center
    if board[5] == " ":
        return 5
    return 0
            
def select_random(l):
    import random
    move = random.randrange(0,len(l))
    return move
def is_full():
  if board.count(' ') > 1:
      return False
  else:
      return True    


def main():
    while(not is_full()):
        try:
            if not is_winner('O'):
                move = player_move()
                insert_letter('X',move)
                print_board()
                os.system('clear')
            else:
                print('srry user computer has won the game')
                return
            if not is_winner('X'):
                print('its computers move')
                move = comp_move()
                if move!=0:
                    insert_letter('O',move)
                    print_board()
                    os.system('clear')
                else:
                    print('game is a TIE')
                    return

            else:
                print("Congats Player u won the game")
                return
        except:
            print('try to enter a valid number')
    if is_full():
        print('game is a TIE')

game_state = True
while game_state:
    main()
    a=input('do u want to play again\y\n')
    if a == n:
        game_state = False