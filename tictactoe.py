
print ("\n"*20)

def display_board(board):
    
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("--"+"--"+ "--")
    print(board[4] +("|") + board[5] +("|") + board[6])
    print("--"+"--"+ "--")
    print(board[7] +("|") + board[8] +("|")+ board[9])

def player_input(player):
    user_input = False
    
    while user_input == False:
        marker = input(f"{player}\nDo you want to be 'X' or 'O'? ")
        if marker in ["X","O"]:
            user_input = True
        else:
            user_input = False
    return marker
            
def next_play():        
        if marker == "X":
            next_marker = "O"
        else:
            next_marker = "X"
        return next_marker
    
def get_position():
    user_entry = False
    while user_entry == False:
        position = (input("please select a number between '1' and '9'\n'1' is 'top-left','2' is 'top-middle', '3' is 'top-right'\n'4' is centre-left, '5'is 'centre-centre', 6 is 'centre-right'\n'7' is 'bottom-left', '8' is 'bottom-center and '9' is 'bottom-right'"))
        
        if position.isdigit and int(position)in range(1,10):
            user_entry = True
        else:
            user_entry = False
    return position
    
def place_marker(board, marker,position):
    
    if position == "1":
        board[1] = marker
    elif position == "2":
        board[2] = marker
    elif position == "3":
        board[3] = marker
    elif position == "4":
        board[4] = marker
    elif position == "5":
        board[5] = marker
    elif position == "6":
        board[6] = marker
    elif position == "7":
        board[7] = marker
    elif position == "8":
        board[8] = marker
    elif position == "9":
        board[9] = marker
    #return position
    print(board)
    display_board(board)

def win_check(board, mark):

    if ((board[1] == "X" and board[2] == "X" and board[3] == "X") or
        (board[4] == "X" and board[5] == "X" and board[6] == "X") or
        (board[7] == "X" and board[8] == "X" and board[9] == "X") or
        (board[1] == "X" and board[4] == "X" and board[7] == "X") or
        (board[2] == "X" and board[5] == "X" and board[8] == "X") or
        (board[3] == "X" and board[6] == "X" and board[9] == "X") or
        (board[1] == "X" and board[5] == "X" and board[9] == "X") or
        (board[3] == "X" and board[5] == "X" and board[7] == "X")):
        print( "X" + " wins")
        return "X" 
        
    elif ((board[1] == "O" and board[2] == "O" and board[3] == "O") or
        (board[4] == "O" and board[5] == "O" and board[6] == "O") or
        (board[7] == "O" and board[8] == "O" and board[9] == "O") or
        (board[1] == "O" and board[4] == "O" and board[7] == "O") or
        (board[2] == "O" and board[5] == "O" and board[8] == "O") or
        (board[3] == "O" and board[6] == "O" and board[9] == "O") or
        (board[1] == "O" and board[5] == "O" and board[9] == "O") or
        (board[3] == "O" and board[5] == "O" and board[7] == "O")):
        print( "O" + " wins")
        return "O"
        
    else:
        print ("Draw") 

def choose_first():
    import random
    from random import randint
    first_play = randint(1,2)
    if first_play ==1:
        return "Player1"
    else:
        return "Player2"
        
def space_check(board, position):
    
    if board[position] == "X" or board[position] == "O":
        return False
    else:
        return True

def full_board_check(board):
    if " " in board:
        return False 
    else:
        return True

def player_choice(board, marker, position):
    place_marker(board, marker, position)
    space_check(board, marker, position)

def replay():
    user_decision = False
    while user_decision == False:
        decision = input("Would you like to play again? Y or N? ")
        if decision in ["Y","N"]:
            user_decision = True
        else:
            user_decision = False
    
    return decision

def game():
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print('Welcome to Tic Tac Toe!')
    i = 0
    decide = True
    playset = []
    playset.append(player_input(choose_first()))
    if playset[0] == "X":
        playset = ["X","O","X","O","X","O","X","0","X","O"]
    else:
        playset = ["O","X","O","X","O","X","0","X","O","X"]
    
    place_marker(board, playset[0], get_position())

    while decide == True:
        print("\n"*20)
        display_board(board)
        win_check(board, "X")
        #break
        win_check(board, "O")
        #break
        #choose_first()
        #get_position()

        place_marker(board, playset[i+1], get_position())
        #next_play()
        full_board_check(board)
        if full_board_check(board) == True or win_check(board, "X")or win_check(board, "O"):
            decide = False
        i+=1
    else:
        if replay() == "Y":
            game()
        else:
            print("Thanks for playing")


game()