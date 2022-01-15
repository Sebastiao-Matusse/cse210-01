from urllib import response


X = "X"
O = "O"

empty = " "
tie = "Tie"
NUM_SQUARES = 9
def display_instruct():

    pass

def prompt_y_n():

    pass

def prompt_board_num():

    pass

def main():
    player_one, player_two = pieces()
    turn = X
    board = create_board()
    display_board(board)

    while not winner(board):
        if turn == player_one:
            move = player_one_move(board, player_one)
            board[move] = player_one
        else:
            move = player_two_move(board, player_two)
            board[move] = player_two
        display_board(board)
        turn = next_turn(turn)
    
    the_winner = winner(board)
    turn = next_turn(turn)
    congrat_winer(the_winner, player_one, player_two)

def create_board():
    # Create a new board.

    board = []
    for square in range(NUM_SQUARES):
        board.append(empty)
    return board

def display_board(board):
    

    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t","-+-+-+-+-")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t","-+-+-+-+-")
    print("\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == empty:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5,),
                   (6, 7, 8),
                   (1, 4, 7),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner
        if empty not in board:
            return tie

def ask_yes_no(question):
    response = None
    while response not in ("y", "no"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    go_first = ask_yes_no("Do you require the fist move? (y/n): ")
    if go_first == "y" or go_first == "n":
        player_one = X
        player_two = O
    return player_one, player_two


def player_one_move(board, player_one):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, please choose another square")
    print("Fine...")
    return move


def player_two_move(board, player_two):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, please choose another square")
    print("Fine...")
    return move


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winer(the_winner, player_one, player_two):
    if the_winner != tie:
        print(the_winner, "won!\n")
    else:
        print("It is a tie\n")

main()