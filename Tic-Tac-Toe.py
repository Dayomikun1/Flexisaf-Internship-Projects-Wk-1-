# Define the game board
board = [" " for _ in range(9)]  # List with 9 empty spaces representing the Tic-Tac-Toe grid

# Display the board
def display_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")

# Check if a player has won
def check_winner(player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if the game is a tie
def check_tie():
    return " " not in board

# AI Player makes a move (randomly selects an empty spot without using random module)
def ai_move():
    empty_spaces = [i for i, spot in enumerate(board) if spot == " "]
    # Use the current sum of the board positions to pseudo-randomly select a spot
    return empty_spaces[(sum(empty_spaces) % len(empty_spaces))]

# Main game loop
def play_game():
    current_player = "X"  # Player "X" starts
    while True:
        display_board()
        if current_player == "X":
            move = int(input("Player X, enter your move (0-8): "))
        else:
            move = ai_move()
            print(f"AI (Player O) chooses position {move}")
        
        if board[move] == " ":
            board[move] = current_player
        else:
            print("That spot is already taken. Try again.")
            continue
        
        if check_winner(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        elif check_tie():
            display_board()
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Call the main game loop
if __name__ == "__main__":
    play_game()
