from urllib import response

"""
Project: Tic-Tac-Toe Game
Name: Sebastiao Joao Matusse
"""

#Global variables
X = "X"
O = "O"
empty = " "
tie = "Tie"
NUM_SQUARES = 10



def main():
    try:
        player_one = X
        player_two = O
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

    except ValueError as val_err:
        print()
        print("Error:", val_err)
        print("Run the the program again and type a number.")
        print()


def prompt_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def create_board():
    """Create a new board
    """

    board = []
    for square in range(NUM_SQUARES):
        board.append(empty)
    return board

def display_board(board):
    
    print("\n\t", board[1], "|", board[2], "|", board[3])
    print("\t","-+-+-+-+-")
    print("\t", board[4], "|", board[5], "|", board[6])
    print("\t","-+-+-+-+-")
    print("\t", board[7], "|", board[8], "|", board[9])

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == empty:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
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

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def player_one_move(board, player_one):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, please choose another square")
    return move


def player_two_move(board, player_two):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, please choose another square")
    return move


def next_turn(turn):
    if turn == X:
        print("It is O's turn: ")
        return O
    else:
        print("It is X's turn: ")
        return X

def congrat_winer(the_winner, player_one, player_two):
    if the_winner != tie:
        print(the_winner, "won!\n")
    else:
        print("It is a draw\n")

main()