#!/usr/bin/env python
import tkinter
import random


# declaring globals
display, root, key, grid, flag = [1] * 5
checked = [0, 0, 0]
inputs = [1, 1, -1]
first_move = False
moves_first = 0


def init():
    global display, root, key, grid, flag, first_move

    first_move = False

    print('with', inputs)

    display = []
    root = tkinter.Tk()
    key = {'blank': '  ',
           'x': 'X',
           'o': 'O'}
    grid = [[key.get('blank'), key.get('blank'), key.get('blank')],
            [key.get('blank'), key.get('blank'), key.get('blank')],
            [key.get('blank'), key.get('blank'), key.get('blank')]]
    flag = 1


def detect_win(grid):
    def detect_for(x):
        # checking every row
        for row in grid:
            count = 0
            for item in row:
                # print('hi', item)
                if item == x:
                    count += 1
            if count == 3:
                return True
        # checking every column
        for j in range(3):
            count = 0
            for i in range(3):
                if grid[i][j] == x:
                    count += 1
            if count == 3:
                return True
        # Checking diagonal i
        count = 0
        for i in range(3):
            if grid[i][i] == x:
                count += 1
        if count == 3:
            return True
        # checking the other diagonal(I want to die)
        count = 0
        for i in range(3):
            if grid[i][2-i] == x:
                count += 1
        if count == 3:
            return True

    if detect_for(key.get('x')):
        # print('X wins')
        return 'x'
    if detect_for(key.get('o')):
        # print('O wins')
        return 'o'
    # print(f"X: {detect_for(key.get('x'))}, O: {detect_for(key.get('o'))}")


def detect_draw(grid):
    for i in grid:
        for j in i:
            if j == key.get('blank'):
                return False

    return True


def highlight_win(grid):
    if detect_win(grid):
        for i in range(3):
            for j in range(3):
                tg = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
                for ii in range(3):
                    for ij in range(3):
                        tg[ii][ij] = grid[ii][ij]

                tg[i][j] = key.get('blank')
                if not detect_win(tg):
                    display[i][j]['fg'] = 'red'


def easy_ai(ch):
    n = 0
    for i in grid:
        for j in i:
            if j == key.get('blank'):
                n += 1
    if n == 0:
        return False

    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)

        if grid[i][j] == key.get('blank'):
            grid[i][j] = key.get(ch)
            display[i][j]['text'] = key.get(ch)
            return True


def grid_copy(array):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            result[i][j] = array[i][j]

    return result


def aix(my_grid):
    best = (1, 1)
    best_score = - float('inf')
    score = 0

    for i in range(3):
        for j in range(3):
            # this happens for every blank space
            if my_grid[i][j] == key.get('blank'):
                temp_grid1 = grid_copy(my_grid)
                # put o in blank space
                temp_grid1[i][j] = key.get('x')
                # check for win and return appropriate score
                result = detect_win(temp_grid1)
                if result:
                    if result == 'x':  # loss
                        # print('loss')
                        checked[2] += 1
                        return inputs[2], i, j
                    else:  # win
                        checked[0] += 1
                        return inputs[0], i, j
                if detect_draw(temp_grid1):  # draw
                    checked[1] += 1
                    return inputs[1], i, j

                # recursive shit
                to_check = ai(temp_grid1)
                score += to_check[0]  # updates score
                # if it is best move, update best
                if to_check[0] > best_score:
                    best_score = to_check[0]
                    best = (i, j)

    return score, best[0], best[1]


def ai(my_grid):
    best = (1, 1)
    best_score = - float('inf')
    score = 0

    for i in range(3):
        for j in range(3):
            # this happens for every blank space
            if my_grid[i][j] == key.get('blank'):
                temp_grid1 = grid_copy(my_grid)
                # put o in blank space
                temp_grid1[i][j] = key.get('o')
                # check for win and return appropriate score
                result = detect_win(temp_grid1)
                if result:
                    if result == 'x':  # loss
                        # print('loss')
                        checked[2] += 1
                        return inputs[2], i, j
                    else:  # win
                        checked[0] += 1
                        return inputs[0], i, j
                if detect_draw(temp_grid1):  # draw
                    checked[1] += 1
                    return inputs[1], i, j

                # recursive shit
                to_check = aix(temp_grid1)
                score += to_check[0]    # updates score
                # if it is best move, update best
                if to_check[0] > best_score:
                    best_score = to_check[0]
                    best = (i, j)

    return score, best[0], best[1]


def make_first_move(grid):
    if grid[1][1] == key.get('blank'):
        grid[1][1] = key.get('o')
        display[1][1]['text'] = grid[1][1]
    else:
        grid[0][0] = key.get('o')
        display[0][0]['text'] = grid[0][0]


def buttonpress(i, j):
    global grid, flag, checked, first_move
    flag += 1

    checked = [0, 0, 0]

    if (not detect_draw(grid)) and display[i][j]['text'] == key.get('blank') and not detect_win(grid):
        # if flag % 2 == 0:
        #     display[i][j]['text'] = key.get('o')
        #     root.title("X's turn")
        # else:
        #     display[i][j]['text'] = key.get('x')
        #     root.title("O's Turn")
        # flag += 1
        display[i][j]['text'] = key.get('x')
        grid[i][j] = display[i][j]['text']

        if not detect_win(grid):
            root.title("Computer is thinking")
            # easy_ai('o')
            if first_move:
                aim = ai(grid)
                _, aii, aij = aim
                if display[aii][aij]['text'] == key.get('blank'):
                    display[aii][aij]['text'] = key.get('o')
                    grid[aii][aij] = display[aii][aij]['text']

                print(checked, aim[0])
            else:
                make_first_move(grid)
                first_move = True

            root.title("X's turn")

        if detect_draw(grid):
            root.title("draw")
        winner = detect_win(grid)
        if winner == 'x':
            root.title("X wins")
        elif winner == 'o':
            root.title("O wins")

        highlight_win(grid)


def reset(event):
    # print(event.keycode)
    kc = event.keycode
    if kc == 103:
        buttonpress(0, 0)
    elif kc == 104:
        buttonpress(0, 1)
    elif kc == 105:
        buttonpress(0, 2)
    elif kc == 100:
        buttonpress(1, 0)
    elif kc == 101:
        buttonpress(1, 1)
    elif kc == 102:
        buttonpress(1, 2)
    elif kc == 97:
        buttonpress(2, 0)
    elif kc == 98:
        buttonpress(2, 1)
    elif kc == 99:
        buttonpress(2, 2)

    else:
        root.destroy()
        print('*' * 20)
        main()


def main():
    global display, root, first_move, moves_first

    init()

    # root = tkinter.Tk()
    root.focus_force()
    root.geometry('500x500')
    root.title("Tic-Tac-Toe")
    # root.iconphoto(tkinter.PhotoImage(file='icon.ico'))
    root['bg'] = 'white'
    root.bind("<Key>", reset)

    display = []

    # defining our list of lambdas for the buttons
    lambda_list = [[lambda: buttonpress(0, 0), lambda: buttonpress(0, 1), lambda: buttonpress(0, 2)],
                   [lambda: buttonpress(1, 0), lambda: buttonpress(1, 1), lambda: buttonpress(1, 2)],
                   [lambda: buttonpress(2, 0), lambda: buttonpress(2, 1), lambda: buttonpress(2, 2)]]

    # declaring the button array which is going to be our display
    for i in range(3):
        li = []
        for j in range(3):
            li.append(tkinter.Button(root, text=key.get('blank'), font="default 70", bg='white', command=lambda_list[i][j]))
        display.append(li)

    # populating our window
    for i in range(3):
        li = []
        for j in range(3):
            display[i][j].grid(row=i, column=j, sticky='nsew')

    # row and column config
    for i in range(3):
        root.grid_columnconfigure(i, weight=1)
        root.grid_rowconfigure(i, weight=1)

    # if the computer has to move first, it will move now
    if moves_first % 2:
        make_first_move(grid)
        first_move = True
    moves_first += 1

    root.mainloop()


if __name__ == '__main__':
    main()


