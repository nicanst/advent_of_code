
path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv4-sorted.txt"

with open(path) as file:
    file_lines = file.read().splitlines()

# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
guard_dick = {}
gidx = 0
sidx = 0
widx = 0
for idx, li in enumerate(file_lines):
    if "Guard #" in li:
        gidx = idx
        _, temp = li.split("#")
        guard = int(temp.strip(" begins shift"))
        if guard not in guard_dick:
            guard_dick[guard] = [0 for _ in range(60)]
    elif "falls asleep" in li:
        sidx = idx
        _, temp2 = li.split(":")
        temp2, _ = temp2.split("]")
        asleep = int(temp2)
    elif "wakes up" in li:
        widx = idx
        _, temp3 = li.split(":")
        temp3, _ = temp3.split("]")
        wakes = int(temp3)
        print(wakes)
    if gidx < sidx and gidx < widx:
        if sidx < widx:
            for min in range(asleep, wakes):
                guard_dick[guard][min] += 1

biggest_min = 0
biggest_guard = 0
best_min = 0
for key, min_list in guard_dick.items():
    if max(min_list) > biggest_min:
        biggest_min = max(min_list)
        biggest_guard = key
        best_min = min_list.index(max(min_list))
print(biggest_min, biggest_guard, best_min)
print("Svar:", biggest_guard * best_min)
