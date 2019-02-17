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

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(steps)

workers = [{"step": '', "time": 0} for _ in range(5)]
# print(workers)

# print(workers)
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(steps)

task_times = {ch: num + 61 for num, ch in enumerate(string.ascii_uppercase)}

# print(task_times["A"])

ticking = 0
in_progress = []
finished = []
while True:
    for worker_id, worker in enumerate(workers):
        if worker["time"] > 1:
            workers[worker_id]["time"] -= 1
        else:
            if worker["step"] != '':
                _temp_step = workers[worker_id]["step"]
                workers[worker_id]["step"] = ''
                finished.append(_temp_step)
                remove_step(steps, _temp_step)
                del steps[_temp_step]

    step_ready_to_do = []
    for step, step_before in steps.items():
        if step_before == []:
            if not step in in_progress and not step in finished:
                step_ready_to_do.append(step)
    # print(step_ready_to_do)
    for worker_id, worker in enumerate(workers):
        if step_ready_to_do != []:
            if worker["step"] == '':
                _temp_step = step_ready_to_do.pop()
                # print("d",_temp_step)
                workers[worker_id]["step"] = _temp_step
                in_progress.append(_temp_step)
                workers[worker_id]["time"] = task_times[_temp_step]

    # print(ticking, workers[0]["step"], workers[1]["step"], finished)

    continue_ = False
    for worker_id, worker in enumerate(workers):
        if worker["step"] != '':
            continue_ = True
    if not continue_:
        print(ticking)
        break
    ticking += 1
