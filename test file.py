from Tic_Tac_Toe import *

def test_one_player(repeat, bot1 = bot, bot2 = dumb_bot):
    """
    quickly see how many times one bot wins over a nother
    by default bot1 is the smart one and bot2 only knows how to complete its two in a row for a win or block
    """
    bot1_wins = 0 # bot1 is 'X'
    bot2_wins = 0 # bot2 is 'O'
    draw = 0
    for i in range(repeat):

        winner = no_player_no_draw(bot1, bot2)
        if winner == 'X':
            bot1_wins += 1
        elif winner == None:
            draw += 1
        else:
            bot2_wins += 1
            print_board(winner)
    print('Bot1 wins:', bot1_wins)
    print('Bot2 wins:', bot2_wins)
    print('Draws    :', draw)


def in_lst(board, list):
    for i in list:
        if board == i[0]:
            return True
    return False


def common_boards(repeat, bot1 = bot, bot2 = dumb_bot):
    board_dict = []
    for i in range(repeat):
        board = no_player_no_draw(return_mode='boards')

        if in_lst(board, board_dict):
            for i in board_dict:
                if board == i[0]:
                    i[1] += 1
                    break
        else:
            board_dict.append([board, 1])

    for i in board_dict:
        print_board(i[0])
        print('Appeared', i[1], 'times')
        print('\n')


def main():
    mode = 'winner'
    while True:
        repeat = input('Number of tests to run: ')
        if repeat == 'winner':
            mode = 'winner'
            continue
        elif repeat == 'board':
            mode = 'board'
            continue
        elif repeat == '':
            break
        if mode == 'winner':
            test_one_player(int(repeat))
        elif mode == 'board':
            common_boards(int(repeat))


if __name__ == '__main__':
    main()