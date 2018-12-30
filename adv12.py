init_state = "#..#.#..##......###...###"
test1 = "...##"

# print(file_lines[1][0:5])
# print(file_lines[1][9:10], end="")

def next_generation(state):
    if type(state) is str:
        pots = {}
        for idx, ch in enumerate(state):
            pots[idx] = ch
    else:
        pots = state

    #for key in sorted(pots.keys()):
        #print(key, pots[key])

    first_key = None
    last_key = None
    for key in sorted(pots.keys()):
        first_key = key if first_key == None else first_key
        last_key = key if last_key == None or last_key < key else last_key

    for a in range(last_key + 1, last_key + 6):
        pots[a] = "."
    for b in range(first_key - 1, first_key - 6, -1):
        pots[b] = "."

    #for key in sorted(pots.keys()):
    #    print(key, pots[key])

    return_dick = {}
    path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv12-short.txt"
    with open(path) as file:
        file_lines = file.read().splitlines()
    for key in sorted(pots.keys()):
        part_of_line = ""
        is_in = False
        if (key - 2) in pots and (key + 2) in pots:
            for k in range(key - 2, key + 3):
                part_of_line += pots[k]
            for line in file_lines:
                #print(key, part_of_line, line[0:5], " ", end="")
                if part_of_line == line[0:5]:
                    #print("3","match", end="")
                    is_in = True
                #print()
        if is_in:
            return_dick[key] = "#"
        else:
            return_dick[key] = "."
    return return_dick



g = next_generation(init_state)
for _ in range(19):
    g = next_generation(g)

for key in sorted(g.keys()):
    if key > -1:
        print(g[key], end="")

#     first_key = None
#     last_key = None
#     for key in sorted(pots.keys()):
#         first_key = first_key or key
#         last_key = last_key or key
#         last_key = key if last_key < key else last_key
#
#     for a in range(last_key + 1, last_key + 6):
#         pots[a] = "."
#     for b in range(first_key - 1, first_key - 6, -1):
#         pots[b] = "."
#
#
#

#
#     return_dick = {}
#     for key in sorted(pots.keys()):
#         part_of_line = ""
#         is_in = False
#         if (key - 2) in pots and (key + 2) in pots:
#             for k in range(key - 2, key + 3):
#                 part_of_line += pots[k]
#             for line in file_lines:
#                 #print(key, part_of_line, line[0:5], " ", end="")
#                 if part_of_line == line[0:5]:
#                     #print("3","match", end="")
#                     is_in = True
#                 #print()
#         if is_in:
#             return_dick[key] = "#"
#         else:
#             return_dick[key] = "."
#     return return_dick
#
# gen1 = generationizer(init_state)
# gen2 = generationizer(gen1)
#
# for key2 in sorted(gen2.keys()):
#     print(key2,gen2[key2], end="")
