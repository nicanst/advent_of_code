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

print("asdffffffffff")
print(workers)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(steps)

task_times = {ch: num + 61 for num, ch in enumerate(string.ascii_uppercase)}
in_progress = []
ready_to_do = []
done_steps = []
for _ in range(200):
    print(done_steps,in_progress)
    for step, step_before in steps.items():
        if step_before == []:
            if not step in ready_to_do and not step in done_steps and not step in in_progress:
                ready_to_do.append(step)

    for worker_id, worker in enumerate(workers):
        if worker["step"] == '':
            if ready_to_do != []:
                workers[worker_id]["step"] = ready_to_do.pop()
                in_progress.append(workers[worker_id]["step"])
                workers[worker_id]["time"] += task_times[workers[worker_id]["step"]]

    min_time = 10000
    # to_delete = None
    for worker_id, worker in enumerate(workers):
        if worker["time"] < min_time and worker["time"] > 0 and worker["step"] != '':
            min_time = worker["time"]
            to_delete = worker["step"]
    for worker_id, worker in enumerate(workers):
        if worker["step"] == to_delete:
            worker["step"] = ''
    print("delete----",to_delete,min_time)
    remove_step(steps, to_delete)
    del steps[to_delete]
    done_steps.append(to_delete)


    max_time = 0
    for worker_id, worker in enumerate(workers):
        if worker["time"] > min_time:
            max_time = worker["time"]
        print(max_time)
    print(to_delete, workers)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(steps)
    print()
    print("MAX---",max_time)
#
# steps = copy.deepcopy(steps_original)
# workers = [{"task": '', "time": 0} for _ in range(5)]
#
# task_times = {ch: num + 61 for num, ch in enumerate(string.ascii_uppercase)}
#
# q = [pending_step for pending_step, steps_before in steps.items() if steps_before == []]
# for a in q: del steps[a]
#
# for worker_id, worker in enumerate(workers):
#     if worker["task"] == '' and q != []:
#         workers[worker_id]["task"] = q.pop()
#         workers[worker_id]["time"] = task_times[workers[worker_id]["task"]]
