path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv7.txt"

def remove_stuff(dick, to_remove):
    for key, val in dick.items():
        if to_remove in val:
            dick[key].remove(to_remove)

with open(path) as f:
    txt = f.read().splitlines()

dick = {}
for r in txt:
    if r[5] not in dick:
        dick[r[5]] = []
    if r[36] not in dick:
        dick[r[36]] = []
    if r[5] not in dick[r[36]]:
        dick[r[36]].append(r[5])

continue_ = True
li = []
while continue_:
    empty_key = None
    if dick == {}:
        continue_ = False
    for key, val in dick.items():
        if val == []:
            if not empty_key:
                empty_key = key
            if empty_key > key:
                empty_key = key
    li.append(empty_key)
    remove_stuff(dick, empty_key)
    del dick[empty_key]
    if dick == {}:
        continue_ = False

for ch in li:
    print(ch, end="")
