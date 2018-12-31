#(3)[7]
def print_board(board, elf1pos, elf2pos):
    for idx, score in enumerate(board):
        if idx == elf1pos:
            print(f"({score})", end="")
        elif idx == elf2pos:
            print(f"[{score}]", end="")
        else:
            print(score, end="")
    print()

def print_board2(board, start, stop):
    start = start - 0
    stop = stop - 1
    for idx, score in enumerate(board):
        if idx >= start and idx <= stop:
            print(score, end="")
    print()

def new_round(board):
    if board == []:
        board.append(elf1["score"])
        board.append(elf2["score"])
    else:
        score_sum = elf1["score"] + elf2["score"]

        if score_sum > 9:
            score_sum_string = str(score_sum)
            board.append(int(score_sum_string[0]))
            board.append(int(score_sum_string[1]))
        else:
            board.append(score_sum)
    elf1_move = elf1["score"] + 1
    elf2_move = elf2["score"] + 1
    elf1["pos"] = ((elf1_move + elf1["pos"]) % (len(board)))
    elf2["pos"] = ((elf2_move + elf2["pos"]) % (len(board)))
    elf1["pos"] = elf1["pos"] if elf1["pos"] < len(board) else 0
    elf2["pos"] = elf2["pos"] if elf2["pos"] < len(board) else 0
    elf1["score"] = board[elf1["pos"]]
    elf2["score"] = board[elf2["pos"]]
    #print_board(board, elf1["pos"], elf2["pos"])


elf1 = {}
elf1["score"] = 3
elf1["pos"] = 0

elf2 = {}
elf2["score"] = 7
elf2["pos"] = 1

board = []

while len(board) < 77250:
    new_round(board)

print_board2(board,77201,77211)
