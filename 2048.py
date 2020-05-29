import random
from pynput import keyboard
from os import system
from copy import deepcopy

board = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]


def show_board():
    print(f'''
┌───────┬───────┬───────┬───────┐
│{board[0][0]}\t│{board[0][1]}\t│{board[0][2]}\t│{board[0][3]}\t│
├───────┼───────┼───────┼───────┤
│{board[1][0]}\t│{board[1][1]}\t│{board[1][2]}\t│{board[1][3]}\t│
├───────┼───────┼───────┼───────┤
│{board[2][0]}\t│{board[2][1]}\t│{board[2][2]}\t│{board[2][3]}\t│
├───────┼───────┼───────┼───────┤
│{board[3][0]}\t│{board[3][1]}\t│{board[3][2]}\t│{board[3][3]}\t│
└───────┴───────┴───────┴───────┘
''')


def find_empty_sqrs():
    result = []
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == ' ':
                result.append((i, j))
    return result


def insert_num(num):
    empty_sqr = random.choice(find_empty_sqrs())
    board[empty_sqr[0]][empty_sqr[1]] = num


def score():
    sum = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] != ' ':
                sum += board[i][j]
    return sum


def board_filled():
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == ' ':
                return False
    return True


def hor_consec_check():
    for row in board:
        if (row[0] == row[1] or
            row[1] == row[2] or
                row[2] == row[3]):
            return True
    return False


def ver_consec_check():
    for j in range(0, 4):
        if (board[0][j] == board[1][j] or
            board[1][j] == board[2][j] or
                board[2][j] == board[3][j]):
            return True
    return False


def game_over():
    if board_filled():
        if (hor_consec_check() or
                ver_consec_check()):
            return False
        return True
    else:
        return False


# this function changes the board if user presses left key
def move_left():
    for row in board:
        i = 1
        while(i < 4):
            if row[i] == ' ':
                i += 1
                continue
            while(i > 0 and row[i-1] == ' '):
                row[i-1], row[i] = row[i], ' '
                i -= 1
                continue
            if (i > 0 and row[i-1] == row[i]):
                row[i-1] *= 2
                row[i] = ' '
            i += 1


# this function changes the board if user presses right key
def move_right():
    for row in board:
        i = 2
        while(i >= 0):
            if row[i] == ' ':
                i -= 1
                continue
            while(i < 3 and row[i+1] == ' '):
                row[i+1], row[i] = row[i], ' '
                i += 1
                continue
            if (i < 3 and row[i+1] == row[i]):
                row[i+1] *= 2
                row[i] = ' '
            i -= 1


# this function changes the board if user presses up key
def move_up():
    for j in range(0, 4):
        i = 1
        while(i < 4):
            if board[i][j] == ' ':
                i += 1
                continue
            while(i > 0 and board[i-1][j] == ' '):
                board[i-1][j], board[i][j] = board[i][j], ' '
                i -= 1
                continue
            if (i > 0 and board[i-1][j] == board[i][j]):
                board[i-1][j] *= 2
                board[i][j] = ' '
            i += 1


# this function changes the board if user presses down key
def move_down():
    for j in range(0, 4):
        i = 2
        while(i >= 0):
            if board[i][j] == ' ':
                i -= 1
                continue
            while(i < 3 and board[i+1][j] == ' '):
                board[i+1][j], board[i][j] = board[i][j], ' '
                i += 1
                continue
            if (i < 3 and board[i+1][j] == board[i][j]):
                board[i+1][j] *= 2
                board[i][j] = ' '
            i -= 1


# change the board according to the key pressed
def on_press(key):
    if key == keyboard.Key.left:
        move_left()
    elif key == keyboard.Key.right:
        move_right()
    elif key == keyboard.Key.up:
        move_up()
    elif key == keyboard.Key.down:
        move_down()
    return False


# passes the key pressed by user to on_press function
def user_input():
    with keyboard.Listener(on_press) as listener:
        listener.join()


# insert two new 2's in a random empty square
insert_num(2)
insert_num(2)


while not game_over():
    # clear the screen
    system('cls')
    # exit message
    print("Ctrl+C to exit.")
    # print score
    print(score())
    # a copy or the board before user input.. it will be used later to check if the board is changed
    prev_board = deepcopy(board)
    # show the board
    show_board()
    # change the board according the input of the user
    user_input()
    # if the board has changed, then insert a new 2 in a random empty square
    if(prev_board != board):
        insert_num(2)
# clear the screen
system('cls')
# print score
print('Score:', score())