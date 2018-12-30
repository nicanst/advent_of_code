path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv10-short.txt"


with open(path) as f:
    txt = f.read().splitlines()

li = []
for r in txt:
    li.append((int(r[10:12]), int(r[14:16])))
