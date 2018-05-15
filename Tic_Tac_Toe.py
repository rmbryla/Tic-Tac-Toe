from bot import *
from draw_game import *

def make_game_list():
    return [[7,8,9],
            [4,5,6],
            [1,2,3]]


def print_board(game_list):

    for i in range(0, 3):
        line = ''
        for j in game_list[i]:
            line += '| ' + str(j) + ' '
        print(line + '|')
        if i == 0 or i == 1:
            print('-------------')


def player_turn(game_list, x, index):
    for i in game_list:
        for j in range(0, 3):
            if i[j] == index:
                i[j] = x
                return True
    return False


def check_win(game_list):
    for i in game_list:
        if i[0] == i[1] and i[1] == i[2]:
            return True

    for i in range(0, 3):
        if game_list[0][i] == game_list[1][i] and game_list[1][i] == game_list[2][i]:
            return True

    if game_list[0][0] == game_list[1][1] and game_list[1][1] == game_list[2][2]:
        return True

    if game_list[0][2] == game_list[1][1] and game_list[2][0]== game_list[1][1]:
        return True

    return False


def is_draw(board):
    for i in board:
        for j in i:
            if type(j) == int:
                return False
    return True


def two_player():
    win = False
    board = make_game_list()
    print_board(board)
    turn = 'X'
    draw_blank()
    while win is False:
        print("It is " + turn + "'s turn")
        index = input('Where do you want to play?')
        print('\n')
        if not index.isdigit():
            print('invalid location to play')
            print_board(board)
            continue
        if not player_turn(board, turn, int(index)):
            print('invalid location to play')
            print_board(board)
            continue
        draw_at(int(index), turn)
        print_board(board)
        win = check_win(board)
        if win is True:
            print('Congratulations,', turn, 'has won!')
        if is_draw(board):
            print("It's a draw!")
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

def one_player(bot):
    turn = random.choice(['X', 'O'])
    #turn = 'O' # if you make turn 'X' you will always go first, 'O' the bot will go first
    win = False
    print('You are X')
    if turn == 'X':
        print('You will make the first move')
    else:
        print('The bot will make the first move')
    board = make_game_list()
    print_board(board)
    draw_blank()
    while win is False:

        if turn == 'O':
            index = bot(board, turn)
            print('O played play at', index)
        else:
            index = input('Where do you want to play?')

        print('\n')
        index = str(index)

        if not index.isdigit():
            print('invalid location to play')
            print_board(board)
            continue
        if not player_turn(board, turn, int(index)):
            print('invalid location to play')
            print_board(board)
            continue
        draw_at(int(index), turn)
        print_board(board)
        win = check_win(board)
        if win is True:
            print('Congratulations,', turn, 'has won!')
        elif is_draw(board):
            print("It's a draw!")
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


def no_player(bot1, bot2):
    turn = random.choice(['X', 'O'])
    win = False
    draw_blank()
    board = make_game_list()
    while not win:
        if turn == 'X':
            index = bot1(board, turn)
        elif turn == 'O':
            index = bot2(board, turn)
        player_turn(board, turn, index)
        draw_at(index, turn)
        win = check_win(board)

        if win is True:
            print('Congratulations,', turn, 'has won!')
            return winner(board)
        elif is_draw(board):
            print("It's a draw!")
            return None
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


def no_player_no_draw(bot1 = bot, bot2 = dumb_bot, return_mode = 'winner'):
    # made for the test file so it was faster and didn't spam the console
    turn = random.choice(['X', 'O'])
    win = False
    board = make_game_list()
    while not win:
        if turn == 'X':
            index = bot1(board, turn)
        elif turn == 'O':
            index = bot2(board, turn)
        player_turn(board, turn, index)
        win = check_win(board)
        if win is True:
            won = winner(board)
            if return_mode == 'winner':
                if won == 'O':
                    return 'O'
                return 'X'
            return board
        elif is_draw(board):
            if return_mode == 'winner':
                return None
            return board
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


def winner(board):
    for i in board:
        if i[0] == i[1] and i[1] == i[2] and i[0] == 'X':
            return 'X'

    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] == 'X':
            return 'X'

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == 'X':
        return 'X'

    if board[0][2] == board[1][1] and board[2][0]== board[1][1] and board[1][1] == 'X':
        return 'X'

    return 'O'


def main():
    while True:
        turtle.speed(5)
        print('1) Two player')
        print('2) One player (HARD)')
        print('3) One player (EASY)')
        print('4) No players (smart vs smart)')
        print('5) No players (smart vs dumb)')
        print('6) No players (dumb vs dumb)')
        selection = input('Make your selection (hit enter to quit): ')
        print('\n')
        turtle.clear()
        if selection == '1':
            two_player()
        elif selection == '2':
            one_player(bot)
        elif selection == '3':
            one_player(dumb_bot)
        elif selection == '4':
            no_player(bot, bot)
        elif selection == '5':
            no_player(bot, dumb_bot)
        elif selection == '6':
            no_player(dumb_bot, dumb_bot)
        elif selection == '':
            break
        else:
            print('Invalid selection')
        print('\n')


if __name__ == '__main__':
    main()
