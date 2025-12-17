board=[]
for i in range(9):
    board.append(" ")
    
def print_board():
    row1= f"| {board[0]} | {board[1]} | {board[2]} |"
    row2= f"| {board[3]} | {board[4]} | {board[5]} |"
    row3= f"| {board[6]} | {board[7]} | {board[8]} |"
    
    print(row1)
    print(row2)
    print(row3)
    
def check_winner(player):
    win_cond = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]

    for a, b, c in win_cond:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False

def check_tie():
    return " " not in board

def play_game(): 
    print("Welcome to Tic Tac Toe game!")
    print_board()
    player = "X"
    
    while True:
        try:
            print("Enter a number between 1-9")
            
            user_text = input("Choose a spot: ")
            choice = int(user_text) - 1
            
            if choice < 0 or choice > 8:
                print("Please pick a number between 1 to 9.")
                continue
            
            if board[choice] == " ":
                board[choice] = player
                print_board()
    
                if check_winner(player):
                    print(f"Player {player} wins!")
                    return
    
                if check_tie():
                    print("It's a tie!")
                    return
                    
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is taken!")
        
        except ValueError:
            print("Please enter a number between 1 and 9.")
    
play_game()
