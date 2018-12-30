init_state = "#..#.#..##......###...###"
test1 = "...##"

# print(file_lines[1][0:5])
# print(file_lines[1][9:10], end="")

def generationizer(init_state_string):
    if type(init_state_string) is not str:
        temp_string = ""
        for key in sorted(init_state_string.keys()):
            temp_string += init_state_string[key]
        init_state_string = temp_string


    path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv12-short.txt"
    with open(path) as file:
        file_lines = file.read().splitlines()

    pots = {}
    for idx, ch in enumerate(init_state_string):
        pots[idx] = ch

    for a in range(len(init_state_string),len(init_state_string)+5):
        pots[a] = "."
    for b in range(-1,-5,-1):
        pots[b] = "."

    return_dick = {}
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

gen1 = generationizer(init_state)
gen2 = generationizer(gen1)

for key2 in sorted(gen2.keys()):
    if key2 == 0: print("0", end="")
    print(gen2[key2], end="")
