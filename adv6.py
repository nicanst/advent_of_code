path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv6-short.txt"

with open(path) as f:
    txt = f.read().splitlines()

xs = []
ys = []
for line in txt:
    x_temp, y_temp = line.split(", ")
    xs.append(int(x_temp))
    ys.append(int(y_temp))

xmax = 0
xmin = 100
for x2 in xs:
    if xmax < x2:
        xmax = x2
    if xmin > x2:
        xmin = x2

ymax = 0
ymin = 100
for y2 in ys:
    if ymax < y2:
        ymax = y2
    if ymin > y2:
        ymin = y2

for idx in range(len(xs)):
    print(xs[idx])
