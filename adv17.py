path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv17.txt"

def p(map_of_ground):
    for y in range(100):
        for x in range(450,550):
            print(map_of_ground[(x, y)], end="")
        print()

with open(path) as f:
    lines = f.read().splitlines()

map_column = {}
map_row = {}
for line in lines:
    rawstring1, rawstring2 = line.split(", ")
    if "y=" in rawstring1:
        row = int(rawstring1.strip("y="))
        rawstring2 = rawstring2.strip("x=")
        from_, to_ = map(int, rawstring2.split(".."))
        if not row in map_row:
            map_row[row] = []
        map_row[row].append((from_,to_))

    if "x=" in rawstring1:
        col = int(rawstring1.strip("x="))
        rawstring2 = rawstring2.strip("y=")
        from_, to_ = map(int, rawstring2.split(".."))
        if not col in map_column:
            map_column[col] = []
        map_column[col].append((from_,to_))

print(map_column,map_row)

map_of_ground = {}
for x in range(700):
    for y in range(600):
        if x in map_column:
            xexist = False
            for range_ in map_column[x]:
                from_, to = range_
                if from_ <= y <= to:
                    xexist = True
            if xexist:
                map_of_ground[(x, y)] = "#"
        if y in map_row:
            yexist = False
            for range_ in map_row[y]:
                from_, to = range_
                if from_ <= x <= to:
                    yexist = True
            if yexist:
                map_of_ground[(x, y)] = "#"
        if (x,y) not in map_of_ground:
            map_of_ground[(x, y)] = "."

    print()

map_of_ground[(500, 0)] = "+"

point = (500, 0)

def down(p): return (p[0], p[1] + 1)
def up(p): return (p[0], p[1] - 1)
def left(p): return (p[0] - 1, p[1])
def right(p): return (p[0] + 1, p[1])

# for a in range(55):
#     if map_of_ground[down(point)] == ".":
#         point = down(point)
#         map_of_ground[point] = "~"
#         # print(1)
#     elif map_of_ground[left(point)] != "#":
#         point = left(point)
#         map_of_ground[point] = "~"
#         # print(2)
#     else:
#         continue_ = True
#         while continue_:
#             if map_of_ground[down(point)] == ".":
#                 # print(3)
#                 continue_ = False
#             elif map_of_ground[right(point)] == "#":
#                 # print(4)
#                 point = up(point)
#                 continue_ = False
#             else:
#                 point = right(point)
#                 map_of_ground[point] = "~"
#                 print(point)

p(map_of_ground)

# for _ in range(30):
#     if map_of_ground[x, y + 1] == ".":
#         map_of_ground[x, y + 1] = "~"
#         y += 1
#     elif map_of_ground[x - 1, y] == ".":
#         map_of_ground[x - 1, y] = "~"
#         x -= 1
#     elif map_of_ground[x - 1, y] == "#":
#         continue_ = True
#         while continue_:
#             if map_of_ground[x + 1, y] != "#":
#                 map_of_ground[x + 1, y] = "~"
#                 x += 1
#                 if map_of_ground[x, y - 1] == ".":
#                     continue_ = False
#             elif map_of_ground[x + 1, y] == "#":
#                 if map_of_ground[x + 1, y - 1] == ".":
#                     continue_ = False
#                 else:
#                     x += 1
#                     y -= 1
#                     continue_ = False
#     print(x,y)
