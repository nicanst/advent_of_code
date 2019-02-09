path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv6.txt"

def steps(from_, to):
    from_x, from_y = from_
    to_x, to_y = to
    return abs(from_x - to_x) + abs(from_y - to_y)

with open(path) as f:
    lines = f.read().splitlines()

points = []
for idx, line in enumerate(lines):
    x, y = map(int, line.split(", "))
    points.append((x,y))

xtop, ytop = (0, 0)
for p in points:
    xtop = p[0] if xtop < p[0] else xtop
    ytop = p[1] if ytop < p[1] else ytop


step_counter = {}
for x in range(xtop + 1):
    for y in range(ytop + 1):
        if not (x, y) in step_counter:
            step_counter[(x, y)] = 0
        for point_id, point_coord in enumerate(points):
            step_counter[(x, y)] += steps(point_coord,(x, y))

area = 0
for key, value in step_counter.items():
    if value < 10000:
        area += 1
print(area)
