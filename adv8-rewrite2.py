path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv8.txt"

# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----
# 1 2
# 1,2:

with open(path) as f:
    lines = f.read().splitlines()
data = lines[0].split(" ")
data = [int(a) for a in data]

# print(data)
header_nodes = []
header_metadata = []
entries = []
# #node data
# #2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
#skriv till nodestack
#skriv till
# data_count = 0
keep_going = True
commando = "header_nodes"
phase = 0
while keep_going:
    if data == []:
        keep_going = False
    else:
        phase += 1
        popped = data.pop(0)
        if phase < 40:
            print(f"Fas: {phase} pop {popped}",
                    f"stack: {commando}",
                    sep="\n")
        if commando == "header_nodes":
            header_nodes.append(popped)
        elif commando == "header_metadata":
            header_metadata.append(popped)
        elif commando == "entries":
            entries.append(popped)
        if phase < 40:
            print(f"header_nodes: {header_nodes}",
                    f"header_metadata: {header_metadata}",
                    f"entries: {entries}",
                    sep="\n")
            print()

    # #2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    # header_nodes = []
    # header_metadata = []
        if commando == "header_nodes":
            commando = "header_metadata"
        elif commando == "header_metadata":
            if header_nodes == [] or header_nodes[-1] == 0:
                header_metadata[-1] -= 1
                commando = "entries"
                if header_nodes != []:
                    header_nodes.pop()
            else:
                assert header_nodes[-1] > 0, "header_nodes mindre än noll"
                commando = "header_nodes"
                header_nodes[-1] -= 1
        elif commando == "entries":
            if header_metadata[-1] == 0:
                header_metadata.pop()
                if header_nodes == [] or header_nodes[-1] == 0:
                    commando = "entries"
                    if header_metadata != []:
                        header_metadata[-1] -= 1
                    if header_nodes != []:
                        header_nodes.pop()
                else:
                    commando = "header_nodes"
                    # assert header_nodes[-1] > 0, "header_nodes mindre än noll"
                    header_nodes[-1] -= 1

            else:
                assert header_metadata[-1] > 0, "header_metadata mindre än noll"
                header_metadata[-1] -= 1
                commando = "entries"

        # if header_nodes != [] and take_entries and header_nodes[-1] == 0:
        #     header_nodes.pop()

print(sum(entries))
