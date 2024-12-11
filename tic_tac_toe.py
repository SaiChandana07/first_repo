# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if the current player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6],  # Diagonal 2
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (no more moves)
def check_full(board):
    return " " not in board

# Function to take player input and make a move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter a position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("This position is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    board = [" "] * 9  # Board represented by a list of 9 spaces
    current_player = "X"  # Player X starts the game

    while True:
        print_board(board)
        player_move(board, current_player)

        # Check for a winner
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie (no more spaces and no winner)
        if check_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()