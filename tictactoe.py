from termcolor import colored

X = colored("X",'red')
O = colored("O",'green')

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    line = "---+---+---"
    print(line)
    for row in board:
        print(f' {row[0]} | {row[1]} | {row[2]} ')
        print(line)


print_board(board)


def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True


    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True


    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def is_full(board):

    for row in board:
        if ' ' in row:
            return False
    return True


def get_position(prompt):
    while True:
        try:
            position = int(input(prompt))
            if position < 0 or position > 2:
                print("Please enter a number between 0 and 2")
            else:
                return position
        except ValueError:
            print("Please enter a valid number")


def get_move(current_player):
    print(f"Player {current_player}'s turn")
    while True:
        row = get_position("Enter a row (0-2): ")
        column = get_position("Enter a column (0-2): ")
        if board[row][column] == ' ':
            board[row][column] = current_player
            break
        else:
            print('This spot is already taken')


def main():
    current_player = X
    while True:
        get_move(current_player)
        print_board(board)

        if check_winner(board):
            print(f'Player {current_player} wins!')
            break

        if is_full(board):
            print('The board is full! It\'s a tie!')
            break


        current_player = O if current_player == X else X


if __name__ == '__main__':
    main()
