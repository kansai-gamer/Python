def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

def judge(board, marker):
    if board[0] == marker and board[1] == marker and board[2] == marker \
    or board[3] == marker and board[4] == marker and board[5] == marker \
    or board[6] == marker and board[7] == marker and board[8] == marker \
    or board[0] == marker and board[3] == marker and board[6] == marker \
    or board[1] == marker and board[4] == marker and board[7] == marker \
    or board[2] == marker and board[5] == marker and board[8] == marker \
    or board[0] == marker and board[4] == marker and board[8] == marker \
    or board[2] == marker and board[4] == marker and board[6] == marker :
        return True
    return False



board = [" ", " ", " ", 
         " ", " ", " ", 
         " ", " ", " "]

while True:
    x = int(input("Input(1-9):"))
    i = x - 1
    board[i] = "o"
    print_board(board)

    z = judge(board, "o")
    if z:
        print("o win!!")

    import random
    while True:
        y = random.randint(0, 8)
        if board[y] == " ":
            break
    
    board[y] = "x"
    print_board(board)
    z = judge(board, "x")
    if z:
        print("x win!!")

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