import random


board = [
    [' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ']
] 

def show_board():
    print(f'''
┌──┬──┬──┬──┐
│{board[0][0]} │{board[0][1]} │{board[0][2]} │{board[0][3]} │
├──┼──┼──┼──┤
│{board[1][0]} │{board[1][1]} │{board[1][2]} │{board[1][3]} │
├──┼──┼──┼──┤
│{board[2][0]} │{board[2][1]} │{board[2][2]} │{board[2][3]} │
├──┼──┼──┼──┤
│{board[3][0]} │{board[3][1]} │{board[3][2]} │{board[3][3]} │
└──┴──┴──┴──┘
''')
def find_empty_sqrs():
    result = []
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j]==' ':
                result.append((i,j))
    return result           

# print(find_empty_sqrs())





def insert_num(num):
    empty_sqr=random.choice(find_empty_sqrs())
    board[empty_sqr[0]][empty_sqr[1]] = num

insert_num(2)
show_board()
