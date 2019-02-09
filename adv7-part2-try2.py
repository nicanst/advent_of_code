import copy
import string
import pprint

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



task_times = {ch: num + 61 for num, ch in enumerate(string.ascii_uppercase)}
workers = {w: "" for w in range(1,6)}
step_order = steps
finished_work = []
undone_work = order[:]

for second in range(30000):

    if undone_work == []:
        print("DDDDD", second)

    without_work = [worker_id for worker_id, task in workers.items() if task == ""]
    with_work = [worker_id for worker_id, task in workers.items() if task != ""]

    for id in with_work:
        task_times[workers[id]] -= 1
        # print(second, "|", task_times[workers[id]])


    if second == 0:
        tasks_free_to_do = {task for task in undone_work if step_order[task] == []}
        undone_work = [t for t in undone_work if t not in tasks_free_to_do]

    for task_left in undone_work:
        add_task = True
        for steps_before in step_order[task_left]:
            if steps_before not in finished_work:
                add_task = False
        if add_task:
            tasks_free_to_do.add(task_left)

    undone_work = [t for t in undone_work if t not in tasks_free_to_do]

    for w in without_work:
        if tasks_free_to_do != set():
            workers[w] = tasks_free_to_do.pop()

print(undone_work)
# pprint.pprint(step_order)






















# print(worker)
#
# #steps
# #order
# unfinished_steps = [ch for ch in order]
# finished_steps = []
# # print("dd",steps["Y"])
# for seconds in range(500):
#     # print("un", unfinished_steps)
#     # print("fin", finished_steps)
#     # print("SEKUNDER",seconds)
#     # print(seconds, unfinished_steps)
#     # print("fin", finished_steps)
#     for w,w2 in worker.items():
#         print(w,"-",w2,end="")
#     if unfinished_steps == []:
#         print("SEKUNDER",seconds)
#         break
#
#     if finished_steps == [] and worker[1] == "":
#         worker[1] = unfinished_steps.pop(0)
#         finished_steps.append(worker[1])
#     for k, v in worker.items():
#         # print(seconds, k, v)
#         #check if a worker is free
#         # print(v)
#         if v == "H":
#             print("wnhhhhh")
#         if v == "":
#             delete_it = False
#             for ch in unfinished_steps:
#                 # if ch == "H":
#                 #     print("dd",steps[ch])
#                 # all_finished = False
#                 # if steps[ch] != []:
#                 #     all_finished = True
#                 #     for a in steps[ch]:
#                 #         if not a in finished_steps:
#                 #             all_finished = False
#
#                 if steps[ch] == []:
#                     worker[k] = ch
#                     delete_it = True
#                 else:
#                     all_finished = True
#                     for a in steps[ch]:
#                         if not a in finished_steps:
#                             all_finished = False
#                     if all_finished:
#                         worker[k] = ch
#                         delete_it = True
#                 if delete_it:
#                     print("unfinish",seconds,unfinished_steps.pop(unfinished_steps.index(ch)))
#
#
#         elif v != "":
#             # for e, t in worker.items():
#             #     print("Grrj2", seconds, e, t)
#             # print("GREJEN ", v, letter_sek[v])
#             letter_sek[v] -= 1
#             # print("llll",letter_sek[v],v)
#             if letter_sek[v] <= 0:
#                 # print("test",seconds, v)
#                 finished_steps.append(v)
#                 worker[k] = ""
#
# print(steps["H"])
# print(unfinished_steps)
# print("fin", finished_steps)
# print(steps)
