# -*- coding: utf-8 -*-
"""
Command-Line Chess.
omgitskuei
Aug 26th 2021

A command-line game of hot-seat chess where players move pieces by entering
chess board square coordinates.

Sources:
Assignment prompt from;
'Automate the Boring Stuff with Python, 2nd Edition' by Al Sweigart, 2019
"""


def print_board(board: dict, show_coordinates: bool):
    # print_board(board, False)
    # [R][N][B][Q][K][B][N][R]
    # [P][P][P][P][P][P][P][P]
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]
    # [p][p][p][p][p][p][p][p]
    # [r][n][b][q][k][b][n][r]

    # print_board(board, False) # if dict is default, empty
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]
    # [_][_][_][_][_][_][_][_]

    # print_board(board, True)
    # [(0,0),R][(0,1),N][(0,2),B][(0,3),Q][(0,4),K][(0,5),B][(0,6),N][(0,7),R]
    # [(1,0),P][(1,1),P][(1,2),P][(1,3),P][(1,4),P][(1,5),P][(1,6),P][(1,7),P]
    # [(2,0),_][(2,1),_][(2,2),_][(2,3),_][(2,4),_][(2,5),_][(2,6),_][(2,7),_]
    # [(3,0),_][(3,1),_][(3,2),_][(3,3),_][(3,4),_][(3,5),_][(3,6),_][(3,7),_]
    # [(4,0),_][(4,1),_][(4,2),_][(4,3),_][(4,4),_][(4,5),_][(4,6),_][(4,7),_]
    # [(5,0),_][(5,1),_][(5,2),_][(5,3),_][(5,4),_][(5,5),_][(5,6),_][(5,7),_]
    # [(6,0),p][(6,1),p][(6,2),p][(6,3),p][(6,4),p][(6,5),p][(6,6),p][(6,7),p]
    # [(7,0),r][(7,1),n][(7,2),b][(7,3),q][(7,4),k][(7,5),b][(7,6),n][(7,7),r]

    # print_board(board, True) # if dict is default, empty
    # [(0,0),_][(0,1),_][(0,2),_][(0,3),_][(0,4),_][(0,5),_][(0,6),_][(0,7),_]
    # [(1,0),_][(1,1),_][(1,2),_][(1,3),_][(1,4),_][(1,5),_][(1,6),_][(1,7),_]
    # [(2,0),_][(2,1),_][(2,2),_][(2,3),_][(2,4),_][(2,5),_][(2,6),_][(2,7),_]
    # [(3,0),_][(3,1),_][(3,2),_][(3,3),_][(3,4),_][(3,5),_][(3,6),_][(3,7),_]
    # [(4,0),_][(4,1),_][(4,2),_][(4,3),_][(4,4),_][(4,5),_][(4,6),_][(4,7),_]
    # [(5,0),_][(5,1),_][(5,2),_][(5,3),_][(5,4),_][(5,5),_][(5,6),_][(5,7),_]
    # [(6,0),_][(6,1),_][(6,2),_][(6,3),_][(6,4),_][(6,5),_][(6,6),_][(6,7),_]
    # [(7,0),_][(7,1),_][(7,2),_][(7,3),_][(7,4),_][(7,5),_][(7,6),_][(7,7),_]
    for x in range(8, 0, -1):
        string = ''
        for y in range(1, 9):
            if show_coordinates:
                string = string + \
                         f'[({x}, {y}), ' + board[x, y] + ']'
            else:
                string = string + f'[' + board[x, y] + ']'
        print(string)


def print_board_alg(board: dict):
    # print_board_alg(board)
    #     a  b  c  d  e  f  g  h
    #  8 [R][N][B][Q][K][B][N][R] 8
    #  7 [P][P][P][P][P][P][P][P] 7
    #  6 [_][_][_][_][_][_][_][_] 6
    #  5 [_][_][_][_][_][_][_][_] 5
    #  4 [_][_][_][_][_][_][_][_] 4
    #  3 [_][_][_][_][_][_][_][_] 3
    #  2 [p][p][p][p][p][p][p][p] 2
    #  1 [r][n][b][q][k][b][n][r] 1
    #     a  b  c  d  e  f  g  h
    print('    a  b  c  d  e  f  g  h ')
    board_display = ""
    for x in range(8, 0, -1):
        board_display = board_display + f' {x} '
        for y in range(1, 9):
            board_display = board_display + f'[' + board[x, y] + ']'
        board_display = board_display + f' {x}'
        if x != 1:
            board_display = board_display + '\n'
    print(board_display)
    print('    a  b  c  d  e  f  g  h ')


def init_board(board: dict):
    for x in range(8, 0, -1):
        for y in range(1, 9):
            board.setdefault((x, y), '_')

    pawns_char = 'P'
    rooks_char = 'R'
    knight_char = 'N'
    bishop_char = 'B'
    queen_char = 'Q'
    king_char = 'K'
    first_col = 1
    last_col = 9

    # UPPER CASE for BLACK, lower case for white
    # spawn BLACK team pawns
    for x in range(first_col, last_col):
        board[2, x] = pawns_char
    # spawn white team pawns
    for x in range(first_col, last_col):
        board[7, x] = pawns_char.lower()

    vip_list = [rooks_char, knight_char, bishop_char,
                queen_char, king_char,
                bishop_char, knight_char, rooks_char]
    # spawn BLACK team vips
    for x in range(first_col, last_col):
        board[1, x] = vip_list[x - 1]
    # spawn BLACK team vips
    for x in range(first_col, last_col):
        board[8, x] = vip_list[x - 1].lower()
    return board


def get_square_alg_to_grid(square_str: str):
    char_to_num_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                        'g': 7, 'h': 8}
    row = int(square_str[0:1])
    col = char_to_num_dict[square_str[1:2]]
    square_tuple = (row, col)
    return square_tuple


def get_square_grid_to_alg(square_tuple: tuple):
    char_to_num_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f',
                        7: 'g', 8: 'h'}
    row, col = square_tuple
    return str(row) + char_to_num_dict.get(col)


def is_same_team(piece1: str, piece2: str):
    if piece1.islower() & piece2.islower():
        return True
    if piece1.isupper() & piece2.isupper():
        return True
    return False


def get_pawn_moves(pawn_coords: tuple,
                   chessboard: dict):
    piece_moved = chessboard[pawn_coords]
    valid_moves_list = []
    row, col = pawn_coords

    # WHITE
    if piece_moved.islower():
        color_int = row - 1
    # BLACK
    else:
        color_int = row + 1
    # can only move diagonal-forward queen-side if that square has
    # an enemy
    try:
        same = is_same_team(
            piece_moved,
            chessboard[(color_int, col - 1)])
        if (chessboard[(color_int, col - 1)] != "_") & (not same):
            valid_moves_list.append((color_int, col - 1))
    except KeyError:
        pass
    # can only move forward one square if that square is empty
    try:
        if chessboard[(color_int, col)] == "_":
            valid_moves_list.append((color_int, col))
    except KeyError:
        pass
    # can only move diagonal-forward king-side if that square has
    # an enemy
    try:
        same = is_same_team(
            piece_moved,
            chessboard[(color_int, col + 1)])
        if (chessboard[(color_int, col + 1)] != "_") & (not same):
            valid_moves_list.append((color_int, col + 1))
    except KeyError:
        pass
    # if this pawn is moving for the first time that game, they
    # can move forward two squares
    if (row == 7) & (piece_moved.islower()):
        valid_moves_list.append((color_int - 1, col))
    if (row == 2) & (piece_moved.isupper()):
        valid_moves_list.append((color_int + 1, col))
    return valid_moves_list


def get_rook_moves(rook_coords: tuple,
                   chessboard: dict):
    piece_moved = chessboard[rook_coords]
    valid_moves_list = []
    row, col = rook_coords
    # add all horizontal possible squares
    for x in range(1, 9, 1):
        if x != col:
            valid_moves_list.append((row, x))
    # remove horizontal possible squares that are blocked
    # remove queen-side (<--) after a piece is blocking
    blocked_flag = False
    for each_col in range(col - 1, 0, -1):
        # remove all squares after being blocked
        if blocked_flag:
            valid_moves_list.remove((row, each_col))
        else:
            # if tile is occupied by a piece (of either team), squares after
            # that one are blocked and not valid moves
            if chessboard[(row, each_col)] != "_":
                blocked_flag = True
                # remove current square because rook can't take own pieces
                if is_same_team(piece_moved, chessboard[(row, each_col)]):
                    valid_moves_list.remove((row, each_col))
    # remove king-side (-->) after a piece is blocking
    blocked_flag = False
    for each_col in range(col + 1, 9, 1):
        # remove all squares after being blocked
        if blocked_flag:
            valid_moves_list.remove((row, each_col))
        else:
            # if tile is occupied by a piece (of either team), squares after
            # that one are blocked and not valid moves
            if chessboard[(row, each_col)] != "_":
                blocked_flag = True
                # remove current square because rook can't take own pieces
                if is_same_team(piece_moved, chessboard[(row, each_col)]):
                    valid_moves_list.remove((row, each_col))

    # add all vertical possible squares
    for y in range(1, 9, 1):
        if y != row:
            valid_moves_list.append((y, col))
    # remove vertical possible squares that are blocked
    # remove black-side (v) after a piece is blocking
    blocked_flag = False
    for each_row in range(row - 1, 0, -1):
        # remove all squares after being blocked
        if blocked_flag:
            valid_moves_list.remove((each_row, col))
        else:
            # if tile is occupied by a piece (of either team), squares after
            # that one are blocked and not valid moves
            if chessboard[(each_row, col)] != "_":
                blocked_flag = True
                # remove current square because rook can't take own pieces
                if is_same_team(piece_moved, chessboard[(each_row, col)]):
                    valid_moves_list.remove((each_row, col))
    # remove white-side (^) after a piece is blocking
    blocked_flag = False
    for each_row in range(row + 1, 9, 1):
        # remove all squares after being blocked
        if blocked_flag:
            valid_moves_list.remove((each_row, col))
        else:
            # if tile is occupied by a piece (of either team), squares after
            # that one are blocked and not valid moves
            if chessboard[(each_row, col)] != "_":
                blocked_flag = True
                # remove current square because rook can't take own pieces
                if is_same_team(piece_moved, chessboard[(each_row, col)]):
                    valid_moves_list.remove((each_row, col))
    return valid_moves_list


def get_bishop_moves(bishop_coords: tuple,
                     chessboard: dict):
    piece_moved = chessboard[bishop_coords]
    valid_moves_list = []
    row, col = bishop_coords
    # step contains pairs where KEY is direction, VALUE is x,y step
    steps = {'8a': (1, -1), '8h': (1, 1), '1a': (-1, -1), '1h': (-1, 1)}
    # bishop moves go in 4 directions
    for x in range(0, 4, 1):
        if x == 0:
            # add bishop moves going from piece towards 8a direction
            row_step = steps.get('8a')[0]  # 1
            col_step = steps.get('8a')[1]  # -1
        elif x == 1:
            # add bishop moves going from piece towards 8h direction
            row_step = steps.get('8h')[0]  # 1
            col_step = steps.get('8h')[1]  # 1
        elif x == 2:
            # add bishop moves going from piece towards 1a direction
            row_step = steps.get('1a')[0]  # -1
            col_step = steps.get('1a')[1]  # -1
        elif x == 3:
            # add bishop moves going from piece towards 1h direction
            row_step = steps.get('1h')[0]  # -1
            col_step = steps.get('1h')[1]  # 1
        else:
            print("ERROR - GET_BISHOP_MOVES: error finding step pair")
            break
        offset = 1
        flag_blocked = False
        for y in range(1, 9 - row, 1):
            curr_sq_row = row + offset * row_step
            curr_sq_col = col + offset * col_step
            if not flag_blocked:
                if ((curr_sq_row == 0)
                        or (curr_sq_col == 0)):
                    break
                # stop adding more squares further down this diagonal direction
                if chessboard[(curr_sq_row, curr_sq_col)] != "_":
                    if is_same_team(piece_moved,
                                    chessboard[(curr_sq_row, curr_sq_col)]):
                        break
                    else:
                        flag_blocked = True
                valid_moves_list.append((curr_sq_row, curr_sq_col))
                offset = offset + 1
            else:
                break
    return valid_moves_list


def get_knight_moves(knight_coords: tuple,
                     chessboard: dict):
    valid_moves_list = []
    # step contains pairs where KEY is direction, VALUE is x,y step
    steps = {'white_white_queen': (2, -1), 'white_white_king': (2, 1),
             'black_black_queen': (-2, -1), 'black_black_king': (-2, 1),
             'queen_queen_white': (1, -2), 'queen_queen_black': (-1, -2),
             'king_king_white': (1, 2), 'king_king_black': (-1, 2)}
    # knights move in 4 directions, gets steps for row, col for each direction
    for x in range(0, 8, 1):
        if x == 0:
            row_step = steps.get('white_white_queen')[0]
            col_step = steps.get('white_white_queen')[1]
        elif x == 1:
            row_step = steps.get('white_white_king')[0]
            col_step = steps.get('white_white_king')[1]
        elif x == 2:
            row_step = steps.get('black_black_queen')[0]
            col_step = steps.get('black_black_queen')[1]
        elif x == 3:
            row_step = steps.get('black_black_king')[0]
            col_step = steps.get('black_black_king')[1]
        elif x == 4:
            row_step = steps.get('queen_queen_white')[0]
            col_step = steps.get('queen_queen_white')[1]
        elif x == 5:
            row_step = steps.get('queen_queen_black')[0]
            col_step = steps.get('queen_queen_black')[1]
        elif x == 6:
            row_step = steps.get('king_king_white')[0]
            col_step = steps.get('king_king_white')[1]
        elif x == 7:
            row_step = steps.get('king_king_black')[0]
            col_step = steps.get('king_king_black')[1]
        else:
            print("ERROR - GET_KNIGHT_MOVES: error finding step pair")
            break
        # TODO handle KeyError
        # knight moves ignore other pieces along its path, so don't need a loop
        # knight can move to empty square
        if (chessboard[(knight_coords[0] + row_step,
                        knight_coords[1] + col_step)] == "_"):
            valid_moves_list.append((knight_coords[0] + row_step,
                                     knight_coords[1] + col_step))
        # knight can move to enemy square
        elif not is_same_team(chessboard[knight_coords],
                              chessboard[(knight_coords[0] + row_step,
                                          knight_coords[1] + col_step)]):
            valid_moves_list.append((knight_coords[0] + row_step,
                                     knight_coords[1] + col_step))
        else:
            # knight cannot move to friendly square, already occupied
            print("this square occupied:", knight_coords[0] + row_step,
                  knight_coords[1] + col_step)
            pass
    return valid_moves_list


def get_queen_moves(queen_coords: tuple,
                    chessboard: dict):
    valid_moves_list = []
    steps = {'white_queen': (1, -1), 'white_king': (1, 1),
             'black_queen': (-1, -1), 'black_king': (-1, 1)}

    return valid_moves_list


def get_king_moves(king_coords: tuple,
                   chessboard: dict):
    valid_moves_list = []

    return valid_moves_list


def is_valid_move(prev_square: tuple,
                  next_square: tuple,
                  player: str,
                  chessboard: dict):
    piece_moved = chessboard[prev_square]
    piece_being_captured = chessboard[next_square]
    valid_moves_list = []

    # PAWN RULES
    if (piece_moved == 'p') or (piece_moved == 'P'):
        valid_moves_list = get_pawn_moves(prev_square, chessboard)
    # ROOK RULES
    elif (piece_moved == 'r') or (piece_moved == 'R'):
        valid_moves_list = get_rook_moves(prev_square, chessboard)
    # KNIGHT RULES
    elif (piece_moved == 'n') or (piece_moved == 'N'):
        valid_moves_list = get_knight_moves(prev_square, chessboard)
    # BISHOP RULES
    elif (piece_moved == 'b') or (piece_moved == 'B'):
        valid_moves_list = get_bishop_moves(prev_square, chessboard)
    # QUEEN RULES
    elif (piece_moved == 'q') or (piece_moved == 'Q'):
        valid_moves_list = get_queen_moves(prev_square, chessboard)
    # KING RULES
    elif (piece_moved == 'k') or (piece_moved == 'K'):
        valid_moves_list = get_king_moves(prev_square, chessboard)
    else:
        print('Piece type not found: ' + piece_moved)
        return False

    if hints:
        count_int = 1
        valid_moves_message = ''
        if len(valid_moves_list) == 0:
            print('Valid Moves = None')
        else:
            for each_square_tuple in valid_moves_list:
                each_square_str = get_square_grid_to_alg(each_square_tuple)
                valid_moves_message = valid_moves_message + each_square_str
                if count_int < len(valid_moves_list):
                    valid_moves_message = valid_moves_message + ", "
                else:
                    pass
                count_int = count_int + 1
            print("Valid moves = " + valid_moves_message)

    if next_square not in valid_moves_list:
        return False

    # reaching here means move is valid for the piece type
    # (king, queen, bishop, knight, rook, pawn)
    return True


def move_piece(prev_square: tuple,
               next_square: tuple):
    print('Moving ' +
          chessboard_dict[prev_square] +
          ' to ' + get_square_grid_to_alg(next_square))
    chessboard_dict[next_square] = chessboard_dict[prev_square]
    chessboard_dict[prev_square] = '_'


'''
-------------------------------------------------------------------------------
Main
-------------------------------------------------------------------------------
'''
# initialize vars
chessboard_dict = {}
game_over = True
turn = 1
active_player = 'White'
old_square_grid_tuple = None
new_square_grid_tuple = None
refresh_menu_input = True
hints = True
reenter_move = False

# init board for new game
chessboard_dict = init_board(chessboard_dict)

chessboard_dict[(5, 2)] = "n"

print('CmdL Chess')
print('Version 1.0')
print('by omgitskuei')

while refresh_menu_input:
    print('')
    print('MAIN MENU')
    print('-----------------------------------------------')
    print('Enter F to Play')
    print('Enter J for Tutorial')
    print('Enter L for Options')
    print('Enter Q to Quit')
    menu_input = input()
    if (menu_input.lower() == 'f') | (menu_input.lower() == 'q'):
        refresh_menu_input = not refresh_menu_input
    if menu_input.lower() == 'f':
        game_over = not game_over
    elif menu_input.lower() == 'j':
        print(
            'White pieces are notated by lower-case letters.\n'
            'Black pieces are notated by UPPER-case letters.\n'
            'k,K - king\n'
            'q,Q - queen\n'
            'b,B - bishop\n'
            'n,N - knight\n'
            'r,R - rook\n'
            'p,P - pawn\n'
            'Enter in coordinates for a square tile on the board using the\n'
            'syntax; [Row Letter][Column Number].\n'
            'Eg. "2a" is the default position of most queen-side Black pawn.\n'
            'To Exit the game, enter "q" or "quit" at any time.')
    elif menu_input.lower() == 'l':
        print('OPTIONS')
        print('-----------------------------------------------')
        print(f'Enter H to {"Disable" if hints else "Enable"} '
              f'Hints')
        print('Enter anything else to Go Back')
        menu_input = input()
        if menu_input.lower() == 'h':
            hints = not hints
    elif (menu_input.lower() == 'q') | (menu_input.lower() == 'quit'):
        exit(0)

while not game_over:
    # refresh board display on new turn
    if not reenter_move:
        print_board_alg(chessboard_dict)
    # reset flag
    reenter_move = False
    # if turn # is even, Black plays - odd, White plays
    if turn % 2 == 0:
        active_player = 'Black'
    else:
        active_player = 'White'
    # don't re-print turn's title on re-enter
    if not reenter_move:
        print(f'Turn {turn} - {active_player} --------------------------------')
    # collect user prompt for move
    old_square = input('Enter square coordinates to move piece: ')
    if (old_square == 'quit') | (old_square == 'q'):
        exit(0)
    new_square = input('Enter new coordinates for piece: ')
    if (new_square == 'quit') | (new_square == 'q'):
        exit(0)
    # convert user prompt into tuples for board lookup
    try:
        old_square_grid_tuple = get_square_alg_to_grid(old_square)
        new_square_grid_tuple = get_square_alg_to_grid(new_square)
    except ValueError as v:
        print('Cannot parse user input - Please try again.')
        reenter_move = True
        continue  # skips remaining code and returns to beginning of while loop
    except KeyError as k:
        print('That square is out of bounds - Please try again.')
        reenter_move = True
        continue

    # check general rules before validating move
    # cannot move an empty square
    if chessboard_dict[old_square_grid_tuple] == '_':
        reenter_move = True
        print('That square has no pieces to move - Please try again.')
        continue
    else:
        # cannot move your opponent's piece
        if ((chessboard_dict[old_square_grid_tuple].islower()
             and (active_player == 'Black'))
                or
                (chessboard_dict[old_square_grid_tuple].isupper()
                 and (active_player == 'White'))):
            print('Cannot move another player\'s piece - Please try again.')
            reenter_move = True
            continue
        # cannot take your own pieces
        if is_same_team(chessboard_dict[old_square_grid_tuple],
                        chessboard_dict[new_square_grid_tuple]):
            print('Cannot take your own pieces - Please try again.')
            reenter_move = True
            continue

    # check if move made is valid for the piece type
    if is_valid_move(old_square_grid_tuple,
                     new_square_grid_tuple,
                     active_player,
                     chessboard_dict):
        turn = turn + 1
        move_piece(old_square_grid_tuple, new_square_grid_tuple)
        reenter_move = False
        print('')
    else:
        print('Move invalid - Please enter a valid move.')
        reenter_move = True
