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
