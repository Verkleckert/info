import sys

# Define the Tic Tac Toe board
game_board = [None, None, None, None, None, None, None, None, None]
current_player = "X"

# Function to print the Tic Tac Toe board
def print_board():
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

# Function to print the current state of the board
def print_current_board():
    for i in range(3):
        print(f" {game_board[i*3] or ' '} | {game_board[i*3 + 1] or ' '} | {game_board[i*3 + 2] or ' '} ")
        if i < 2:
            print("-----------")

# Function to place a symbol on the board
def place_symbol(index, symbol):
    if game_board[index] is None:
        game_board[index] = symbol
        return True
    else:
        print(f"Cell {index + 1} is already occupied. Choose an empty cell.")
        return False

# Function to check for a win
def check_win(symbol):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(game_board[i*3 + j] == symbol for j in range(3)) or all(game_board[i + j*3] == symbol for j in range(3)):
            return True
    if all(game_board[i*4] == symbol for i in range(3)) or all(game_board[2 + i*2] == symbol for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full():
    return all(cell is not None for cell in game_board)

# Function for the minimax algorithm
def minimax(depth, maximizing_player):
    if check_win('O'):
        return -1
    elif check_win('X'):
        return 1
    elif is_board_full():
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if game_board[i] is None:
                game_board[i] = 'X'
                eval = minimax(depth + 1, False)
                game_board[i] = None
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if game_board[i] is None:
                game_board[i] = 'O'
                eval = minimax(depth + 1, True)
                game_board[i] = None
                min_eval = min(min_eval, eval)
        return min_eval

# Function to make a move using the minimax algorithm
def make_algorithm_move():
    best_move = -1
    best_eval = float('-inf')

    for i in range(9):
        if game_board[i] is None:
            game_board[i] = 'X'
            eval = minimax(0, False)
            game_board[i] = None

            if eval > best_eval:
                best_eval = eval
                best_move = i

    return best_move

# Function to change the player
def change_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

# Function to run the game
def run_game():
    while not check_win('X') and not check_win('O') and not is_board_full():
        print_current_board()
        if current_player == "X":
            user_input = int(input(f"Player {current_player}, choose a cell (1-9): ")) - 1
            while not (0 <= user_input <= 8) or not place_symbol(user_input, 'X'):
                user_input = int(input(f"Player {current_player}, choose a valid cell (1-9): ")) - 1
        else:
            print("Player O is thinking...")
            ai_move = make_algorithm_move()
            place_symbol(ai_move, 'O')
        change_player()

    print_current_board()

    winner = check_win('X') and 'X' or (check_win('O') and 'O' or 'Tie')
    print(f"The game is over. {winner} wins!")

# Run the game
if __name__ == "__main__":
    run_game()
