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
stack_nodes = []
stack_entries = []
entries = []
# #node data
# #2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# data_count = 0
keep_going = True
take_nodes = True
take_stack_entries = False
take_entries = False
phase = 0
while keep_going:
    if data == []:
        keep_going = False
    else:
        phase += 1
        popped = data.pop(0)
        if phase < 30:
            print(f"Fas: {phase} pop {popped}",
                    f"take_nodes: {take_nodes}",
                    f"take_stack_entries: {take_stack_entries}",
                    f"take_entries: {take_entries}",
                    sep="\n")
        if take_nodes:
            stack_nodes.append(popped)
        elif take_stack_entries:
            stack_entries.append(popped)
        elif take_entries:
            entries.append(popped)
        if phase < 30:
            print(f"stack_nodes: {stack_nodes}",
                    f"stack_entries: {stack_entries}",
                    f"entries: {entries}",
                    sep="\n")
            print()

    # #2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    # stack_nodes = []
    # stack_entries = []
        if take_nodes:
            take_nodes = False
            take_stack_entries = True
            take_entries = False
        elif take_stack_entries:
            if stack_nodes == [] or stack_nodes[-1] == 0:
                take_nodes = False
                take_stack_entries = False
                take_entries = True
                stack_nodes.pop()
            elif stack_nodes != [] and stack_nodes[-1] >= 1:
                stack_nodes[-1] -= 1
                take_nodes = True
                take_stack_entries = False
                take_entries = False
        elif take_entries:
            if stack_entries != []:
                stack_entries[-1] -= 1
            if stack_entries == [] or stack_entries[-1] <= 2:
                if stack_nodes == [] or stack_nodes[-1] == 0:
                    take_nodes = False
                    take_stack_entries = False
                    take_entries = True
                elif stack_nodes[-1] >= 1:
                    stack_nodes[-1] -= 1
                    if stack_nodes[-1] == 0:
                        stack_nodes.pop()
                    take_nodes = True
                    take_stack_entries = False
                    take_entries = False
            else:
                take_nodes = False
                take_stack_entries = False
                take_entries = True

        # if stack_nodes != [] and take_entries and stack_nodes[-1] == 0:
        #     stack_nodes.pop()

        if stack_entries != [] and stack_entries[-1] <= 2:
            stack_entries.pop()

print(sum(entries))
