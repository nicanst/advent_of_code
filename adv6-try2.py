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
            step_counter[(x, y)] = {"s": 10000, "p": None, "d": False}
        for point_id, point_coord in enumerate(points):
            nr_of_steps = steps(point_coord,(x, y))
            if step_counter[(x, y)]["s"] > nr_of_steps:
                step_counter[(x, y)]["p"] = point_id
                step_counter[(x, y)]["s"] = nr_of_steps
                step_counter[(x, y)]["d"] = False
            elif step_counter[(x, y)]["s"] == nr_of_steps:
                step_counter[(x, y)]["d"] = True

ignore_list = set()
for x in range(xtop + 1):
    ignore_list.add(step_counter[(x, 0)]["p"])
    ignore_list.add(step_counter[(x, ytop)]["p"])

for y in range(ytop + 1):
    ignore_list.add(step_counter[(0, y)]["p"])
    ignore_list.add(step_counter[(xtop, y)]["p"])

# print(ignore_list)
# points_to_check = [id for id in range(len(points)) if id not in ignore_list]

sums = {}
for key, value in step_counter.items():
    if not value["d"]:
        if not value["p"] in ignore_list:
            if not value["p"] in sums:
                sums[value["p"]] = 1
            else:
                sums[value["p"]] += 1

highest = 0
for key, value in sums.items():
    highest = value if value > highest else highest
print(highest)






#
# for y in range(range_nr):
#     for x in range(range_nr):
#         if step_counter[(x, y)]["d"]:
#             print("..",end="")
#         elif step_counter[(x, y)]["s"] == 0:
#             print("??-",end="")
#         else:
#             print(step_counter[(x, y)]["p"],end="|")
#     print()
