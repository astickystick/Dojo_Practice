# Function to check if a move is legal on a 3x3 board
def is_legal_move(board, row, col, direction):
    # Check boundaries and move gem
    if direction == 'up' and row > 0:
        board[row][col], board[row-1][col] = board[row-1][col], board[row][col]
    elif direction == 'down' and row < 2:
        board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
    elif direction == 'left' and col > 0:
        board[row][col], board[row][col-1] = board[row][col-1], board[row][col]
    elif direction == 'right' and col < 2:
        board[row][col], board[row][col+1] = board[row][col+1], board[row][col]
    else:
        return False  # Doesn't work 

    # Check for a line of 3 same gems horizontally or vertically
    if check_line(board, row, col) or check_line(board, row-1, col) or check_line(board, row+1, col) or check_line(board, row, col-1) or check_line(board, row, col+1):
        # Move is legal, revert the swap and return True
        revert_swap(board, row, col, direction)
        return True
    else:
        # Move is illegal, revert the swap and return False
        revert_swap(board, row, col, direction)
        return False

# Reverting a swap
def revert_swap(board, row, col, direction):
    if direction == 'up' and row > 0:
        board[row][col], board[row-1][col] = board[row-1][col], board[row][col]
    elif direction == 'down' and row < 2:
        board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
    elif direction == 'left' and col > 0:
        board[row][col], board[row][col-1] = board[row][col-1], board[row][col]
    elif direction == 'right' and col < 2:
        board[row][col], board[row][col+1] = board[row][col+1], board[row][col]

# Checking for a line of 3 same gems
def check_line(board, row, col):
    # Check if the position is within the board
    if 0 <= row < 3 and 0 <= col < 3:
        gem = board[row][col]
        # Check horizontally and vertically
        return (col > 0 and col < 2 and gem == board[row][col-1] == board[row][col+1]) or \
               (row > 0 and row < 2 and gem == board[row-1][col] == board[row+1][col])
    return False

# Example game board
board = [[1, 2, 3], [4, 4, 5], [5, 3, 4]]

# Test a move
# Example: moving the gem at position (1, 1) to the right
result = is_legal_move(board, 1, 1, 'right')
result



#Task 2 
# Checking if a move is legal on a 4x4 board
def is_legal_move(board, row, col, direction):
    # Check boundaries and move gem
    if direction == 'up' and row > 0:
        board[row][col], board[row-1][col] = board[row-1][col], board[row][col]
    elif direction == 'down' and row < 3:
        board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
    elif direction == 'left' and col > 0:
        board[row][col], board[row][col-1] = board[row][col-1], board[row][col]
    elif direction == 'right' and col < 3:
        board[row][col], board[row][col+1] = board[row][col+1], board[row][col]
    else:
        return False  # Invalid move

    # Check for a line of 4 same gems horizontally or vertically
    if check_line(board, row, col) or check_line(board, row-1, col) or check_line(board, row+1, col) or check_line(board, row, col-1) or check_line(board, row, col+1):
        # Move is legal, revert the swap and return True
        revert_swap(board, row, col, direction)
        return True
    else:
        # Move is illegal, revert the swap and return False
        revert_swap(board, row, col, direction)
        return False

# Adjusting the check_line function for a 4x4 grid
def check_line(board, row, col):
    # Check if the position is within the board
    if 0 <= row < 4 and 0 <= col < 4:
        gem = board[row][col]
        # Check horizontally and vertically
        return (col > 0 and col < 3 and gem == board[row][col-1] == board[row][col+1]) or \
               (row > 0 and row < 3 and gem == board[row-1][col] == board[row+1][col])
    return False

# Example 4x4 game board
board = [[1, 2, 3, 4], [4, 4, 5, 6], [5, 3, 4, 7], [8, 7, 6, 5]]

# Test on 4x4 board
# Example: moving the gem at position (1, 1) to the right
result = is_legal_move(board, 1, 1, 'right')

result, board


# Task 3 

# Function to check for 'L' shape
def check_l_shape(board, row, col, gem):
    # 'L' shape can be in four orientations
    # Each orientation has 3 gems in a line and 2 additional gems at a right angle at one end
    # Checking all orientations
    if row < len(board) - 2 and col < len(board[0]) - 1:
        if all(board[row][c] == gem for c in range(col, col + 2)) and \
           all(board[r][col] == gem for r in range(row + 1, row + 3)):
            return True
    if row < len(board) - 2 and col > 0:
        if all(board[row][c] == gem for c in range(col - 1, col + 1)) and \
           all(board[r][col] == gem for r in range(row + 1, row + 3)):
            return True
    # Vertical with horizontal tail
    if row < len(board) - 1 and col < len(board[0]) - 2:
        if all(board[row][c] == gem for c in range(col, col + 3)) and \
           board[row + 1][col] == gem:
            return True
    if row > 0 and col < len(board[0]) - 2:
        if all(board[row][c] == gem for c in range(col, col + 3)) and \
           board[row - 1][col] == gem:
            return True
    return False

# Function to check for 'T' shape
def check_t_shape(board, row, col, gem):
    # 'T' shape can be in four orientations
    # Each orientation has 3 gems in a line and 1 additional gem at the center extending perpendicular
    # Checking all orientations
    if row < len(board) - 1 and col < len(board[0]) - 2 and col > 0:
        if all(board[row][c] == gem for c in range(col - 1, col + 2)) and \
           board[row + 1][col] == gem:
            return True
    if row > 0 and col < len(board[0]) - 2 and col > 0:
        if all(board[row][c] == gem for c in range(col - 1, col + 2)) and \
           board[row - 1][col] == gem:
            return True
    # Vertical with horizontal tail
    if row < len(board) - 2 and col < len(board[0]) - 1:
        if all(board[r][col] == gem for r in range(row, row + 3)) and \
           board[row + 1][col + 1] == gem:
            return True
    if row < len(board) - 2 and col > 0:
        if all(board[r][col] == gem for r in range(row, row + 3)) and \
           board[row + 1][col - 1] == gem:
            return True
    return False

# Function to check if a move results in an 'L' or 'T' shape
def is_special_shape(board, row, col, gem):
    if check_l_shape(board, row, col, gem):
        return "L"
    if check_t_shape(board, row, col, gem):
        return "T"
    return None

# Example 4x4 game board with a potential 'T' shape
board = [[1, 2, 3, 4], [4, 4, 5, 6], [5, 3, 4, 7], [8, 7, 6, 5]]

# Test a move on the 4x4 board that should form a 'T' shape
result, shape = is_legal_move_extended(board, 2, 2, 'left')

result, shape, board

# Task 4 

import random

def remove_gems(board):
    #Remove gems involved in any given move and return the number of gems removed.
    removed_count = 0
    # For simplicity, assuming that a move results in a horizontal line of 3 or more gems
    for r in range(len(board)):
        for c in range(len(board[0]) - 2):
            if board[r][c] == board[r][c + 1] == board[r][c + 2] != 0:
                # Found a line of 3 or more
                count = 1
                while c + count < len(board[0]) and board[r][c] == board[r][c + count]:
                    board[r][c + count] = 0
                    count += 1
                    removed_count += 1
    return removed_count

def refill_board(board):
    #Refill the board with gems falling from above and add new random gems at the top.
    for c in range(len(board[0])):
        empty_rows = [r for r in range(len(board)) if board[r][c] == 0]
        for r in empty_rows:
            # Move gems down
            for above_row in range(r, 0, -1):
                board[above_row][c] = board[above_row - 1][c]
            # Add a new gem at the top
            board[0][c] = random.randint(1, 5)

def calculate_score(removed_count):
    #Calculate the score based on the number of gems removed.
    if removed_count == 3:
        return 10
    elif removed_count == 4:
        return 20
    elif removed_count >= 5:  # Assuming 5 or more is a bomb
        return 50
    return 0

def is_game_over(board):
    # Check if the game is over, so, no more moves or a set number of moves reached.
    return no_more_moves(board)

# Example game loop
board = [[1, 2, 3, 4], [4, 4, 5, 6], [5, 3, 4, 7], [8, 7, 6, 5]]
max_moves = 20
current_moves = 0
total_score = 0

while current_moves < max_moves and not is_game_over(board):
    # Make a move (for simplicity, assuming a move is made randomly)
    row, col = random.randint(0, 3), random.randint(0, 3)
    direction = random.choice(['left', 'right', 'up', 'down'])

    # Check if the move is legal
    legal, _ = is_legal_move(board, row, col, direction)
    if legal:
        removed_count = remove_gems(board)
        score = calculate_score(removed_count)
        total_score += score
        refill_board(board)
        current_moves += 1

# Print the final state of the board and the score
print("Game Over!")
print("Final Board State:")
for row in board:
    print(row)
print(f"Total Score: {total_score}")
print(f"Total Moves Played: {current_moves})
