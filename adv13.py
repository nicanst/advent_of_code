def print_path(positions):

    path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv13-short2.txt"

    with open(path) as file:
        file_lines = file.read().splitlines()

    for y, line in enumerate(file_lines):
        for x, ch in enumerate(line):
            pos_char = None
            for pos in positions:
                if pos["x"] == x and pos["y"] == y:
                    pos_char = pos["d"]
            if pos_char == None:
                print(ch, end="")
            else:
                print(pos_char, end="")
        print()
    print()






def step_forward(positions):

    path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv13.txt"

    with open(path) as file:
        file_lines = file.read().splitlines()

    up = "^"
    down = "v"
    right = ">"
    left = "<"
    all = ("^", "v", ">", "<")

    hori = ("-","/",">","<","\\")
    vert = ("|","/","^","v","\\")
    turn = ("le", "st", "ri")


    for pos in positions:
        if pos["d"] == up:
            pos["y"] -= 1
            if file_lines[pos["y"]][pos["x"]] == "/":
                pos["d"] = right
            elif file_lines[pos["y"]][pos["x"]] == "\\":
                pos["d"] = left
            elif file_lines[pos["y"]][pos["x"]] == "+":
                if pos["t"] == "le":
                    pos["d"] = left
                    pos["t"] = "st"
                elif pos["t"] == "st":
                    pos["d"] = up
                    pos["t"] = "ri"
                elif pos["t"] == "ri":
                    pos["d"] = right
                    pos["t"] = "le"

        elif pos["d"] == down:
            pos["y"] += 1
            if file_lines[pos["y"]][pos["x"]] == "\\":
                pos["d"] = right
            elif file_lines[pos["y"]][pos["x"]] == "/":
                pos["d"] = left
            elif file_lines[pos["y"]][pos["x"]] == "+":
                if pos["t"] == "le":
                    pos["d"] = right
                    pos["t"] = "st"
                elif pos["t"] == "st":
                    pos["d"] = down
                    pos["t"] = "ri"
                elif pos["t"] == "ri":
                    pos["d"] = left
                    pos["t"] = "le"
        elif pos["d"] == right:
            pos["x"] += 1
            if file_lines[pos["y"]][pos["x"]] == "\\":
                pos["d"] = down
            elif file_lines[pos["y"]][pos["x"]] == "/":
                pos["d"] = up
            elif file_lines[pos["y"]][pos["x"]] == "+":
                if pos["t"] == "le":
                    pos["d"] = up
                    pos["t"] = "st"
                elif pos["t"] == "st":
                    pos["d"] = right
                    pos["t"] = "ri"
                elif pos["t"] == "ri":
                    pos["d"] = down
                    pos["t"] = "le"
        elif pos["d"] == left:
            pos["x"] -= 1
            if file_lines[pos["y"]][pos["x"]] == "\\":
                pos["d"] = up
            elif file_lines[pos["y"]][pos["x"]] == "/":
                pos["d"] = down
            elif file_lines[pos["y"]][pos["x"]] == "+":
                if pos["t"] == "le":
                    pos["d"] = down
                    pos["t"] = "st"
                elif pos["t"] == "st":
                    pos["d"] = left
                    pos["t"] = "ri"
                elif pos["t"] == "ri":
                    pos["d"] = up
                    pos["t"] = "le"

    return positions


path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv13.txt"

with open(path) as file:
    file_lines = file.read().splitlines()
all = ("^", "v", ">", "<")
positions = []
for y, line in enumerate(file_lines):
    # print(y, line)
    for x, ch in enumerate(line):
        if ch in all:
            positions.append({"x": x, "y": y, "d": ch, "t": "le"})

pos1 = step_forward(positions)
for _ in range(1000):
    pos1 = step_forward(pos1)
    for idxa, a in enumerate(pos1):
        for idxb, b in enumerate(pos1):
            if idxa != idxb and a["x"] == b["x"] and a["y"] == b["y"]:
                print(a["x"], a["y"])


# for _ in range(50):
#     pos1 = step_forward(pos1)
#     print_path(pos1)




        # if ch in all:
        #     if ch == up:
        #         up_func()
        #     if ch == down:
        #         down_func()
        #     if ch == right:
        #         right_func()
        #     if ch == left:
        #         left_func()
