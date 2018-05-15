import random


def empty_board(board):
    for i in board:
        for j in i:
            if not type(j) == int:
                return False
    return True


def trapped(board):
    if board[0][0] == board[2][2] and board[2][2] != board[1][1]:
        return True
    if board[0][2] == board[2][0] and board[0][2] != board[1][1]:
        return True
    return False


def escape(board):
    if board[0][0] == board[2][2] and board[2][2] != board[1][1]:
        return random.choice(intersection(valid_locations(board), [2,4,6,8]))
    if board[0][2] == board[2][0] and board[0][2] != board[1][1]:
        return random.choice(intersection(valid_locations(board), [2,4,6,8]))
    return random.choice(valid_locations(board))

def valid_locations(board):
    list = []
    for i in board:
        for j in i:
            if type(j) == int:
                list.append(j)
    return list


def two_in_a_row(board):
    for i in board:
        if (i[0] == i[1] and type(i[2]) == int) or \
                (i[1] == i[2] and type(i[0]) == int) or \
                    (i[0] == i[2] and type(i[1]) == int):
            return True
    for i in range(0, 3):
        if (board[0][i] == board[1][i] and type(board[2][i]) == int) or \
                (board[1][i] == board[2][i] and type(board[0][i]) == int) or \
                    (board[0][i] == board[2][i] and type(board[1][i]) == int):
            return True
    if (board[0][0] == board[1][1] and type(board[2][2]) == int) or  \
            (board[2][2] == board[1][1] and type(board[0][0]) == int) or \
                (board[0][2] == board[1][1] and type(board[2][0]) == int) or \
                    (board[2][0] == board[1][1] and type(board[0][2]) == int) or \
                        (board[0][0] == board[2][2] and type(board[1][1]) == int) or \
                            (board [2][0] == board [0][2] and type(board[1][1]) == int):
        return True
    return False


def block(board, turn):
    for i in board: # two in a row
        if i[0] == i[1] and i[0] == turn:
            if type(i[2]) == int:
                return i[2]
        if i[1] == i[2] and i[1] == turn:
            if type(i[0]) == int:
                return i[0]
        if i[0] == i[2]:
            if type(i[1]) == int and i[0] == turn:
                return i[1]
            pass

    for i in range(0, 3): # two in a column
        if board[0][i] == board[1][i] and board[1][i] == turn:
            if type(board[2][i]) == int:
                return board[2][i]
            pass
        if board[0][i] == board[2][i] and board[0][i] == turn:
            if type(board[1][i]) == int:
                return board[1][i]
            pass
        if board[1][i] == board[2][i] and board[1][i] == turn:
            if type(board[0][i]) == int:
                return board[0][i]
            pass

    if board[0][0] == board[1][1] and board[1][1] == turn:
        if type(board[2][2]) == int:
            return board[2][2]
        pass

    if board[2][2] == board[1][1] and board[1][1] == turn:
        if type(board[0][0]) == int:
            return board[0][0]
        pass

    if board[2][2] == board[0][0] and board[2][2] == turn:
        if type(board[1][1]) == int:
            return board[1][1]
        pass

    if board[0][2] == board[1][1] and board[1][1] == turn:
        if type(board[2][0]) == int:
            return board[2][0]
        pass

    if board[2][0] == board[1][1] and board[1][1] == turn:
        if type(board[0][2]) == int:
            return board[0][2]
        pass

    if  board[2][0] == board[0][2] and board[2][0] == turn:
        if type(board[1][1]) == int:
            return board[1][1]
        pass

    """
    top checks for win
    bottom checks for block
    """


    for i in board: # two in a row
        if i[0] == i[1]:
            if type(i[2]) == int:
                return i[2]
        if i[1] == i[2]:
            if type(i[0]) == int:
                return i[0]
        if i[0] == i[2]:
            if type(i[1]) == int:
                return i[1]
            pass

    for i in range(0, 3): # two in a column
        if board[0][i] == board[1][i]:
            if type(board[2][i]) == int:
                return board[2][i]
            pass
        if board[0][i] == board[2][i]:
            if type(board[1][i]) == int:
                return board[1][i]
            pass
        if board[1][i] == board[2][i]:
            if type(board[0][i]) == int:
                return board[0][i]
            pass


    if board[0][0] == board[1][1]:
        if type(board[2][2]) == int:
            return board[2][2]
        pass

    if board[2][2] == board[1][1]:
        if type(board[0][0]) == int:
            return board[0][0]
        pass

    if board[2][2] == board[0][0]:
        if type(board[1][1]) == int:
            return board[1][1]
        pass

    if board[0][2] == board[1][1]:
        if type(board[2][0]) == int:
            return board[2][0]
        pass

    if board[2][0] == board[1][1]:
        if type(board[0][2]) == int:
            return board[0][2]
        pass

    if  board[2][0] == board[0][2]:
        if type(board[1][1]) == int:
            return board[1][1]
        pass
    if intersection(valid_locations(board), [1,3,7,9]) == []:
        return random.choice(valid_locations(board))
    return random.choice(intersection(valid_locations(board), [1,3,7,9]))


def play_adjacent(board):
    if type(board[0][1]) == str:
        return random.choice([9,7])
    if type(board[1][0]) == str:
        return random.choice([1,7])
    if type(board[1][2]) == str:
        return random.choice([3,9])
    if type(board[2][1]) == str:
        return random.choice([1,3])
    return random.choice(intersection(valid_locations(board), [1,3,7,9]))


def two_sides(board):
    if board[0][1] == board [1][0]:
        return True
    if board[0][1] == board [1][2]:
        return True
    if board[1][0] == board [2][1]:
        return True
    if board[1][2] == board [2][1]:
        return True


def open_corners(board):
    return intersection(valid_locations(board), [1,3,7,9])


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    lst3.sort()
    return lst3


def turn_count(board, turn):
    count = 0
    for i in board:
        for j in i:
            if j == turn:
                count += 1
    return count


def corner_center(board, turn):
    if turn_count(board, turn) > 2:
        return False
    if board[1][1] == turn:
        if board[0][0] == turn:
            return True
        if board[0][2] == turn:
            return True
        if board[2][0] == turn:
            return True
        if board[2][2] == turn:
            return True
    return False


def best_corner(board):
    if type(board[1][1]) == str:
        if board[0][0] == board[1][1]:
            if type(board[0][1]) == str:
                return 1
            if type(board[1][0]) == str:
                return 9
        if board[0][2] == board[1][1]:
            if type(board[0][1]) == str:
                return 3
            if type(board[1][2]) == str:
                return 7
        if board[2][0] == board[1][1]:
            if type(board[2][1]) == str:
                return 7
            if type(board[1][0]) == str:
                return 3
        if board[2][2] == board[1][1]:
            if type(board[2][1]) == str:
                return 9
            if type(board[1][2]) == str:
                return 1
        if intersection(valid_locations(board), [1,3,7,9]) == []:
            return random.choice(valid_locations(board))
        return random.choice(intersection(valid_locations(board), [1,3,7,9]))


def board_dict(board):
    dict = {}
    dict['middle'] = board[1][1]
    dict['top'] = board[0][1]
    dict['bottom'] = board[2][1]
    dict['left'] = board[1][0]
    dict['right'] = board[1][2]
    dict['top left'] = board[0][0]
    dict['top right'] = board[0][2]
    dict['bottom left'] = board[2][0]
    dict['bottom right'] = board[2][2]
    return dict



def center(list, turn):
    board = board_dict(list)
    if board['middle'] == turn:
        return True
    return False


def trapped2(list, turn):
    if turn == 'X':
        opp = 'O'
    else:
        opp = 'X'
    board = board_dict(list)
    if not center(list, turn):
        return False
    if center(list, turn):
        if turn_count(list, turn) == 1:
            if board['left'] == board['top right'] and board['left'] == opp:
                return True
            if board['top left'] == board['right'] and board['top left'] == opp:
                return True
            if board['left'] == board['bottom right'] and board['left'] == opp:
                return True
            if board['bottom left'] == board['right'] and board['bottom left'] == opp:
                return True
            if board['bottom'] == board['top right'] and board['bottom'] == opp:
                return True
            if board['bottom'] == board['top left'] and board['bottom'] == opp:
                return True
            if board['top'] == board['bottom right'] and board['top'] == opp:
                return True
            if board['top'] == board['bottom left'] and board['top'] == opp:
                return True



def escape2(list, turn):
    if turn == 'X':
        opp = 'O'
    else:
        opp = 'X'
    board = board_dict(list)
    if center(list, turn):
        if turn_count(list, turn) <= 2:
            if board['left'] == board['top right'] and board['left'] == opp:
                return 7 #random.choice([7,8])
            if board['top left'] == board['right'] and board['top left'] == opp:
                return 9 #random.choice([9,8])
            if board['left'] == board['bottom right'] and board['left'] == opp:
                return 1 #random.choice([1,2])
            if board['bottom left'] == board['right'] and board['bottom left'] == opp:
                return 3 #random.choice([2,3])
            if board['bottom'] == board['top right'] and board['bottom'] == opp:
                return 3 #random.choice([6,3])
            if board['bottom'] == board['top left'] and board['bottom'] == opp:
                return 1 #random.choice([1,4])
            if board['top'] == board['bottom right'] and board['top'] == opp:
                return 9 #random.choice([9,6])
            if board['top'] == board['bottom left'] and board['top'] == opp:
                return 7 #random.choice([7,4])



def second_turn_check(list, turn):
    board = board_dict(list)
    if turn == 'X':
        opp = 'O'
    else:
        opp = 'X'
    if turn_count(list, 'X') == 1 and turn_count(list, 'O') == 1:
        if list[1][1] == turn:
            if board['top left'] == opp or board['top right'] == opp or \
                        board['bottom left'] == opp or board['bottom right'] == opp:
                return True
    return False



def second_turn_move(list, turn):
    board = board_dict(list)
    if turn == 'X':
        opp = 'O'
    else:
        opp = 'X'
    if board['middle'] == turn:
        if board['top left'] == opp:
            return 3
        if board['top right'] == opp:
            return 1
        if board['bottom left'] == opp:
            return 9
        if board['bottom right'] == opp:
            return 7


def bot(board, turn):

    if type(board[1][1]) == int:
        return 5

    if two_in_a_row(board):
        return block(board, turn)

    if trapped(board):
        return escape(board)

    if trapped2(board, turn):
        return escape2(board, turn)

    if intersection(valid_locations(board), [1,3,7,9]) == [1,3,7,9] and not empty_board(board):
        return play_adjacent(board)

    if corner_center(board, turn):
        return best_corner(board)

    if not two_in_a_row(board):
        if second_turn_check(board, turn):
            return second_turn_move(board, turn)
        if intersection(valid_locations(board), [1,3,7,9]):
            return random.choice(intersection(valid_locations(board), [1,3,7,9]))
        return random.choice(valid_locations(board))

    if corner_center(board, turn):
        return best_corner(board)

    return random.choice(valid_locations(board))


def dumb_bot(board, turn):
    if two_in_a_row(board):
        return block(board, turn)
    return random.choice(valid_locations(board))


def random_bot(board, turn):
    return random.choice(valid_locations(board))