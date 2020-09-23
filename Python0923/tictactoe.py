def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()
board = [" ", " ", " ", 
         " ", " ", " ", 
         " ", " ", " "]

while True:
    x = int(input("Input(1-9):"))
    i = x - 1
    board[i] = "o"
    print_board(board)

    if board[0] == "o" and board[1] == "o" and board[2] == "o" \
    or board[3] == "o" and board[4] == "o" and board[5] == "o" \
    or board[6] == "o" and board[7] == "o" and board[8] == "o" \
    or board[0] == "o" and board[3] == "o" and board[6] == "o" \
    or board[1] == "o" and board[4] == "o" and board[7] == "o" \
    or board[2] == "o" and board[5] == "o" and board[8] == "o" \
    or board[0] == "o" and board[4] == "o" and board[8] == "o" \
    or board[2] == "o" and board[4] == "o" and board[6] == "o" :
        print("o win!!")
        break

    import random
    while True:
        y = random.randint(0, 8)
        if board[y] == " ":
            break
    
    board[y] = "x"
    print_board(board)
    if board[0] == "x" and board[1] == "x" and board[2] == "x" \
    or board[3] == "x" and board[4] == "x" and board[5] == "x" \
    or board[6] == "x" and board[7] == "x" and board[8] == "x" \
    or board[0] == "x" and board[3] == "x" and board[6] == "x" \
    or board[1] == "x" and board[4] == "x" and board[7] == "x" \
    or board[2] == "x" and board[5] == "x" and board[8] == "x" \
    or board[0] == "x" and board[4] == "x" and board[8] == "x" \
    or board[2] == "x" and board[4] == "x" and board[6] == "x" :
        print("x win!!")
        break


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