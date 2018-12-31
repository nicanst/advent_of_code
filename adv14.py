#(3)[7]
def print_board(board, elf1pos, elf2pos):
    print("d", board)
    for idx, score in enumerate(board):
        if idx == elf1pos:
            print("(", score, ")", end="")
        elif idx == elf2pos:
            print("[", score, "]", end="")
        else:
            print(score, end="")


elf1 = {}
elf1["score"] = 3
elf1["pos"] = 0

elf2 = {}
elf2["score"] = 7
elf2["pos"] = 1

board = []
board.append(elf1["score"])
board.append(elf2["score"])


print_board(board, elf1["pos"],elf2["pos"])
