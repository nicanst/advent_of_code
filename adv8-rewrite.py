path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv8-short.txt"

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
which_stack = "stack_nodes"
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
                    f"stack: {which_stack}",
                    sep="\n")
        if which_stack == "stack_nodes":
            stack_nodes.append(popped)
        elif which_stack == "stack_enteries":
            stack_entries.append(popped - 1)
        elif which_stack == "entries":
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
        if which_stack == "stack_nodes":
            which_stack = "stack_enteries"
        elif which_stack == "stack_enteries":
            if stack_nodes == [] or stack_nodes[-1] <= 0:
                which_stack = "entries"
                stack_nodes.pop()
            else:
                which_stack = "stack_nodes"
                stack_nodes[-1] -= 1
        elif which_stack == "entries":

            if stack_entries == [] or stack_entries[-1] > 0:
                if stack_entries != []:
                    stack_entries[-1] -= 1
                if stack_nodes == [] or stack_nodes[-1] == 0:
                    which_stack = "entries"
                    if stack_nodes != []:
                        stack_nodes.pop()
                else:
                    stack_nodes[-1] -= 1
                    which_stack == "stack_nodes"
            else:
                which_stack = "entries"

        # if stack_nodes != [] and take_entries and stack_nodes[-1] == 0:
        #     stack_nodes.pop()

        if stack_entries != [] and stack_entries[-1] <= 0:
            stack_entries.pop()

print(sum(entries))
