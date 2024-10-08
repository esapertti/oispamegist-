import random

# Pelilaudan alustus
def init_game():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# Uuden numeron lisääminen laatalle (2 tai 4)
def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

# Laudan tulostus
def print_board(board):
    for row in board:
        print("\t".join(str(cell) if cell != 0 else "." for cell in row))
    print()

# Laattojen yhdistäminen ja liikuttaminen
def compress(board):
    new_board = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][pos] = board[i][j]
                pos += 1
    return new_board

def merge(board):
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

# Liikuta laattoja tiettyyn suuntaan
def move_left(board):
    new_board = compress(board)
    new_board = merge(new_board)
    new_board = compress(new_board)
    return new_board

def rotate_90(board):
    return [[board[j][i] for j in range(4)] for i in range(4)][::-1]

def move_right(board):
    return rotate_90(rotate_90(move_left(rotate_90(rotate_90(board)))))

def move_up(board):
    return rotate_90(move_left(rotate_90(rotate_90(rotate_90(board)))))

def move_down(board):
    return rotate_90(rotate_90(rotate_90(move_left(rotate_90(board)))))

# Tarkista pelin päättyminen
def is_game_over(board):
    if any(0 in row for row in board):
        return False
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False
    return True

# Peli alkaa
def play_game():
    board = init_game()
    print_board(board)

    while True:
        move = input("Enter move (w/a/s/d): ").lower()
        if move == 'w':
            new_board = move_up(board)
        elif move == 'a':
            new_board = move_left(board)
        elif move == 's':
            new_board = move_down(board)
        elif move == 'd':
            new_board = move_right(board)
        else:
            print("Invalid move! Use w/a/s/d.")
            continue

        if new_board != board:
            board = new_board
            add_new_tile(board)
            print_board(board)
            if is_game_over(board):
                print("Game over!")
                break
        else:
            print("No move possible, try again!")

if __name__ == "__main__":
    play_game()
