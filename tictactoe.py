def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

board = [" ", " ", " ", 
         " ", " ", " ", 
         " ", " ", " "]

x = int(input("Input(1-9):"))
i = x - 1
board[i] = "o"
print_board(board)

import random
y = random.randint(0, 8)
board[y] = "x"
print_board(board)


# print("o| | |")
# print(" | | |")
# print(" | | |")

# print("====")

# print("o| | |")
# print(" | | |")
# print(" | | x")

# print("====")

# print("o|x|o")
# print("x|o|x")
# print("o|x|x")

# print("o win")