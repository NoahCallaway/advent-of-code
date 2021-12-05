file_path = "data.txt"

import re
data = open(file_path).read().splitlines()

boards = []
#Create boards and order
board_number = 0
for line in data:
    if ',' in line:
        bingo_call = line.split(',')
    elif line == '':
        board_number += 1
        boards.append([])
    else:
        boards[board_number -1].append(re.findall(r"(\d+)", line))


def check_for_win(board):

    for column in range(len(board[0])):
        for row in range(len(board)):

            if board[row].count('X') == 5:
                return True

            if board[row][column] == 'X':
                if row == len(board) - 1:
                    return True
            else:
                break


def sum_uncalled(board):
    sum = 0
    for row in board:
        for item in row:
            if item != 'X':
                sum += int(item)
    return sum


wins = 0
for call in bingo_call:
    for k, board in enumerate(boards):
        for i, row in enumerate(board):
            for j, number in enumerate(row):
                if number == call:
                    board[i][j] = 'X'
                    if check_for_win(board) is True:
                        wins += 1
                        if wins == 1:
                            print('Part 1:', sum_uncalled(board) * int(call))
                        if wins == len(boards):
                            print('Part 2:', sum_uncalled(board) * int(call))
                        boards[k] = []
                        
    