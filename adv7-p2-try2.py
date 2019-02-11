import copy
import pprint
import string

path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv7.txt"

def remove_step(remove_from, remove_this_step):
    for id, steps in remove_from.items():
        if remove_this_step in steps:
            remove_from[id].remove(remove_this_step)

with open(path) as f:
    lines = f.read().splitlines()

#Steg med lista på steg som kommer före.
# Ex A: [B,C]. Steg B och C måste göras innan A.
steps = {}
for line in lines:
    step_before = line[5]
    step_to_do = line[36]
    if step_to_do not in steps:
        steps[step_to_do] = []
    if step_before not in steps: #För att få med steg utan föregående steg
        steps[step_before] = []
    if step_before not in steps[step_to_do]:
        steps[step_to_do].append(step_before)
#
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(steps)

steps_original = copy.deepcopy(steps)

continue_ = True
step_queue = []
while continue_:
    next_step = None
    if steps == {}:
        continue_ = False
    for pending_step, steps_before in steps.items():
        if steps_before == []:
            if not next_step:
                next_step = pending_step
            if next_step > pending_step:
                next_step = pending_step
    step_queue.append(next_step)
    remove_step(steps, next_step)
    del steps[next_step]
    if steps == {}:
        continue_ = False

steps = copy.deepcopy(steps_original)
workers = [{"task": '', "time": 0} for _ in range(5)]

task_times = {ch: num + 61 for num, ch in enumerate(string.ascii_uppercase)}

q = [pending_step for pending_step, steps_before in steps.items() if steps_before == []]
for a in q: del steps[a]

for worker_id, worker in enumerate(workers):
    if worker["task"] == '' and q != []:
        workers[worker_id]["task"] = q.pop()
        workers[worker_id]["time"] = task_times[workers[worker_id]["task"]]

print(workers)



# print(workers)
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(steps)
