path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv4-sorted.txt"

with open(path) as file:
    file_lines = file.read().splitlines()

guard_dict = {}
idx_sleep = 0
idx_wake = 0
guard_nr = 0
idx_guard = 0
for idx, li in enumerate(file_lines):
    if "#" in li:
        guard_nr = int(li[26:30].strip("b"))
        if not guard_nr in guard_dict:
            guard_dict[guard_nr] = 0
        idx_guard = idx
    if "falls asleep" in li:
        sleep_mi = int(li[15:17])
        idx_sleep = idx
    if "wakes up" in li:
        wake_mi = int(li[15:17])
        idx_wake = idx
    if idx_guard < idx_sleep and idx_guard < idx_wake:
        if idx_wake > idx_sleep:
            guard_dict[guard_nr] += wake_mi - sleep_mi


sleepy_gard = 0
sleep_temp = 0
for k, v in guard_dict.items():

    print(k, 20859 / k)
    if v > sleep_temp:
        sleep_temp = v
        sleepy_guard = k

print("#" + str(sleepy_guard))


list_min = [0 for _ in range(60)]
idx_sleep = 0
idx_wake = 0
guard_nr = 0
for idx, a in enumerate(file_lines):
    if "#2389" in a:
        idx_guard = idx
    if "falls asleep" in a:
        sleep_mi = int(a[15:17])
        idx_sleep = idx
    if "wakes up" in a:
        wake_mi = int(a[15:17])
        idx_wake = idx

    if idx_guard < idx_sleep and idx_guard < idx_wake:
        if idx_wake > idx_sleep:
            for b in range(sleep_mi, wake_mi):
                list_min[b] += 1
#20859
print(list_min)
max_ = max(list_min)
minute = list_min.index(max_)
print(sleepy_guard, minute)
print("svar", minute * sleepy_guard)

# with open(path, "r") as f:
#     txt = f.read().splitlines()
#
# listh = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
# idx_sleep = 0
# idx_wake = 0
# guard_nr = 0
# idx_guard = 0
# for idx, a in enumerate(txt):
#     if "#2441" in a:
#         idx_guard = idx
#     if "falls asleep" in a:
#         sleep_mi = int(a[15:17])
#         idx_sleep = idx
#     if "wakes up" in a:
#         wake_mi = int(a[15:17])
#         idx_wake = idx
#
#     if idx_guard < idx_sleep and idx_guard < idx_wake:
#         if idx_wake > idx_sleep:
#             #print(idx_sleep, idx_wake)
#             for b in range(sleep_mi, wake_mi):
#                 #print(a)
#                 listh[b] += 1
#
# biggest = 0
# for id, c in enumerate(listh):
#     if c > biggest:
#         biggest = c
#         id_save = id
#     print(id, c)
#
# print(id_save * 2441)
#100081

# Hitta den som har mest sovtimmar: 2441
# guard_dict = {}
# idx_sleep = 0
# idx_wake = 0
# guard_nr = 0
# idx_guard = 0
# for idx, a in enumerate(txt):
#     if "#" in a:
#         guard_nr = int(a[26:30].strip("b"))
#         if not guard_nr in guard_dict:
#             guard_dict[guard_nr] = 0
#         idx_guard = idx
#     if "falls asleep" in a:
#         sleep_mi = int(a[15:17])
#         idx_sleep = idx
#     if "wakes up" in a:
#         wake_mi = int(a[15:17])
#         idx_wake = idx
#
#     if idx_guard < idx_sleep and idx_guard < idx_wake:
#         if idx_wake > idx_sleep:
#             guard_dict[guard_nr] += wake_mi - sleep_mi
#
# print(guard_dict)
# high = 0
# for key, val in guard_dict.items():
#     if high < val:
#         winner = key
#         high = val
# #2441
# print(winner)

# Quick-sort

# txt_sorted = []
# keep_going = True
# while keep_going:
#     keep_going = False
#     for idx, row in enumerate(txt):
#         if len(txt) > (idx + 1):
#             switch = False
#
#             mo = int(row[6:8])
#             d = int(row[9:11])
#             h = int(row[12:14])
#             mi = int(row[15:17])
#
#             mo2 = int(txt[idx + 1][6:8])
#             d2 = int(txt[idx + 1][9:11])
#             h2 = int(txt[idx + 1][12:14])
#             mi2 = int(txt[idx + 1][15:17])
#
#             if mo > mo2:
#                 switch = True
#             elif mo == mo2:
#                 if d > d2:
#                     switch = True
#                 elif d == d2:
#                     if h > h2:
#                         switch = True
#                     elif h == h2:
#                         if mi > mi2:
#                             switch = True
#
#             if switch:
#                 save = txt[idx + 1]
#                 txt[idx + 1] = txt[idx]
#                 txt[idx] = save
#                 keep_going = True
#
# for b in txt:
#     print(b)
