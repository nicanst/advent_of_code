# # d'ef print_path(positions):
# #
# #     path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv13-short2.txt"
# #
# #     with open(path) as file:
# #         file_lines = file.read().splitlines()
# #
# #     for y, line in enumerate(file_lines):
# #         for x, ch in enumerate(line):
# #             pos_char = None
# #             for pos in positions:
# #                 if pos["x"] == x and pos["y"] == y:
# #                     pos_char = pos["d"]
# #             if pos_char == None:
# #                 print(ch, end="")
# #             else:
# #                 print(pos_char, end="")
# #         print()
# #     print()
#
#
#
#
#
#
# def step_forward(positions):
#
#     path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv13.txt"
#
#     with open(path) as file:
#         lines = file.read().splitlines()
#
#
#     all_dirs = ("^", "v", ">", "<")
#     up, down, right, left = all_dirs
#
#     hori = ("-","/",">","<","\\")
#     vert = ("|","/","^","v","\\")
#     turn = ("le", "st", "ri")
#
#
#     for pos in positions:
#         if pos["d"] == up:
#             pos["y"] -= 1
#             if file_lines[pos["y"]][pos["x"]] == "/":
#                 pos["d"] = right
#             elif file_lines[pos["y"]][pos["x"]] == "\\":
#                 pos["d"] = left
#             elif file_lines[pos["y"]][pos["x"]] == "+":
#                 if pos["t"] == "le":
#                     pos["d"] = left
#                     pos["t"] = "st"
#                 elif pos["t"] == "st":
#                     pos["d"] = up
#                     pos["t"] = "ri"
#                 elif pos["t"] == "ri":
#                     pos["d"] = right
#                     pos["t"] = "le"
#
#         elif pos["d"] == down:
#             pos["y"] += 1
#             if file_lines[pos["y"]][pos["x"]] == "\\":
#                 pos["d"] = right
#             elif file_lines[pos["y"]][pos["x"]] == "/":
#                 pos["d"] = left
#             elif file_lines[pos["y"]][pos["x"]] == "+":
#                 if pos["t"] == "le":
#                     pos["d"] = right
#                     pos["t"] = "st"
#                 elif pos["t"] == "st":
#                     pos["d"] = down
#                     pos["t"] = "ri"
#                 elif pos["t"] == "ri":
#                     pos["d"] = left
#                     pos["t"] = "le"
#         elif pos["d"] == right:
#             pos["x"] += 1
#             if file_lines[pos["y"]][pos["x"]] == "\\":
#                 pos["d"] = down
#             elif file_lines[pos["y"]][pos["x"]] == "/":
#                 pos["d"] = up
#             elif file_lines[pos["y"]][pos["x"]] == "+":
#                 if pos["t"] == "le":
#                     pos["d"] = up
#                     pos["t"] = "st"
#                 elif pos["t"] == "st":
#                     pos["d"] = right
#                     pos["t"] = "ri"
#                 elif pos["t"] == "ri":
#                     pos["d"] = down
#                     pos["t"] = "le"
#         elif pos["d"] == left:
#             pos["x"] -= 1
#             if file_lines[pos["y"]][pos["x"]] == "\\":
#                 pos["d"] = up
#             elif file_lines[pos["y"]][pos["x"]] == "/":
#                 pos["d"] = down
#             elif file_lines[pos["y"]][pos["x"]] == "+":
#                 if pos["t"] == "le":
#                     pos["d"] = down
#                     pos["t"] = "st"
#                 elif pos["t"] == "st":
#                     pos["d"] = left
#                     pos["t"] = "ri"
#                 elif pos["t"] == "ri":
#                     pos["d"] = up
#                     pos["t"] = "le"
#
#     return positions

path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv13.txt"
with open(path) as file:
    file_lines = file.read().splitlines()

cart_symbols = ("^", "v", ">", "<")
cart_positions = []
for y, line_of_map in enumerate(file_lines):
    # print(y, line)
    for x, char_of_line in enumerate(line_of_map):
        if char_of_line in cart_symbols:
            cart_positions.append({"position": (x, y), "direction": char_of_line})

#     all_dirs = ("^", "v", ">", "<")
#     up, down, right, left = all_dirs
#
#     hori = ("-","/",">","<","\\")
#     vert = ("|","/","^","v","\\")
#     turn = ("le", "st", "ri")
