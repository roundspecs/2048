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


def move_up():
    for j in range(0,4):
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


def move_down():
    for j in range(0,4):
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


def on_press(key):
    if key == keyboard.Key.left:
        move_left()
    elif key == keyboard.Key.right:
        move_right()
    elif key == keyboard.Key.up:
        move_up()
    elif key == keyboard.Key.down:
        move_down()
    elif key == keyboard.Key.esc:
        exit()
    return False


def user_input():
    with keyboard.Listener(on_press) as listener:
        listener.join()

# insert two number initially
insert_num(2)
insert_num(2)


while True:
    system('cls')
    print("Press esc to exit.")
    prev_board = deepcopy(board)
    show_board()
    user_input()
    if(prev_board != board):
        insert_num(2)
