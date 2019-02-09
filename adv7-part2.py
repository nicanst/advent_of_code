import copy

path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv7.txt"

def remove_stuff(dick, to_remove):
    for key, val in dick.items():
        if to_remove in val:
            dick[key].remove(to_remove)

with open(path) as f:
    lines = f.read().splitlines()

steps = {}
for line in lines:
    step_before = line[5]
    step_after = line[36]
    if step_before not in steps:
        steps[step_before] = []
    if step_after not in steps:
        steps[step_after] = []
    if step_before not in steps[step_after]:
        steps[step_after].append(step_before)

steps_copy = copy.deepcopy(steps)
continue_ = True
order = []
while continue_:
    empty_key = None
    if steps_copy == {}:
        continue_ = False
    for key, val in steps_copy.items():
        if val == []:
            if not empty_key:
                empty_key = key
            if empty_key > key:
                empty_key = key
    order.append(empty_key)
    remove_stuff(steps_copy, empty_key)
    del steps_copy[empty_key]
    if steps_copy == {}:
        continue_ = False
#
# for ch in order:
#     print(ch, end="")

import string
letter_sek = {ch: num + 61 for num, ch in enumerate(string.ascii_uppercase)}
# print(letter_sek)

worker = {w: "" for w in range(1,6)}
# print(worker)

#steps
#order
unfinished_steps = [ch for ch in order]
finished_steps = []
# print("dd",steps["Y"])
for seconds in range(500):
    # print("un", unfinished_steps)
    # print("fin", finished_steps)
    # print("SEKUNDER",seconds)
    # print(seconds, unfinished_steps)
    # print("fin", finished_steps)
    for w,w2 in worker.items():
        print(w,"-",w2,end="")
    if unfinished_steps == []:
        print("SEKUNDER",seconds)
        break

    if finished_steps == [] and worker[1] == "":
        worker[1] = unfinished_steps.pop(0)
        finished_steps.append(worker[1])
    for k, v in worker.items():
        # print(seconds, k, v)
        #check if a worker is free
        # print(v)
        if v == "H":
            print("wnhhhhh")
        if v == "":
            delete_it = False
            for ch in unfinished_steps:
                # if ch == "H":
                #     print("dd",steps[ch])
                # all_finished = False
                # if steps[ch] != []:
                #     all_finished = True
                #     for a in steps[ch]:
                #         if not a in finished_steps:
                #             all_finished = False

                if steps[ch] == []:
                    worker[k] = ch
                    delete_it = True
                else:
                    all_finished = True
                    for a in steps[ch]:
                        if not a in finished_steps:
                            all_finished = False
                    if all_finished:
                        worker[k] = ch
                        delete_it = True
                if delete_it:
                    print("unfinish",seconds,unfinished_steps.pop(unfinished_steps.index(ch)))


        elif v != "":
            # for e, t in worker.items():
            #     print("Grrj2", seconds, e, t)
            # print("GREJEN ", v, letter_sek[v])
            letter_sek[v] -= 1
            # print("llll",letter_sek[v],v)
            if letter_sek[v] <= 0:
                # print("test",seconds, v)
                finished_steps.append(v)
                worker[k] = ""

print(steps["H"])
print(unfinished_steps)
print("fin", finished_steps)
print(steps)
