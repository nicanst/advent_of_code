path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv17-short.txt"

def p(map_of_ground):
    for y in range(15):
        for x in range(490,510):
            print(map_of_ground[(x, y)], end="")
        print()
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

# print(map_column,map_row)

map_of_ground = {}
for x in range(470,515):
    for y in range(20):
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

    # print()

map_of_ground[(500, 0)] = "+"

point = (500, 0)

def down(p): return (p[0], p[1] + 1)
def up(p): return (p[0], p[1] - 1)
def left(p): return (p[0] - 1, p[1])
def right(p): return (p[0] + 1, p[1])

def go_down(point, map_of_ground):
    x, y = point
    if y < 16:
        continue_ = True
        while continue_:
            x, y = down(point)
            if y < 16:
                if map_of_ground[down(point)] == ".":
                    point = down(point)
                    map_of_ground[point] = "|"
                else:
                    continue_ = False
                    return point
            else:
                return None
    else:
        return None

def go_right(point, map_of_ground):
    continue_ = True
    while continue_:
        if map_of_ground[down(point)] == ".":
            continue_ = False
            return (".", point)
        elif map_of_ground[right(point)] != "#":
            point = right(point)
            if map_of_ground[point] == ".":
                map_of_ground[point] = "|"
            else:
                map_of_ground[point] = "~"
        elif map_of_ground[right(point)] == "#":
            continue_ = False
            return ("#", point)

def go_left(point, map_of_ground):
    continue_ = True
    while continue_:
        if map_of_ground[down(point)] == ".":
            continue_ = False
            return (".", point)
        elif map_of_ground[left(point)] != "#":
            point = left(point)
            if map_of_ground[point] == ".":
                map_of_ground[point] = "|"
            else:
                map_of_ground[point] = "~"
        elif map_of_ground[left(point)] == "#":
            continue_ = False
            return ("#", point)

def walk(point, map_of_ground):
    x, y = point
    if (490 <= x <= 510) and y < 14:
        down_places = []
        point = go_down(point, map_of_ground)
        if point != None:
            x, y = point
            if (490 <= x <= 510) and y < 14:
                continue_ = True
                while continue_:
                    check1, point1 = go_right(point, map_of_ground)
                    check2, point2 = go_left(point, map_of_ground)
                    if check1 == "#" and check2 == "#":
                        point = up(point)
                    else:
                        if check1 == ".":
                            walk(point1, map_of_ground)
                        if check2 == ".":
                            walk(point2, map_of_ground)
            else:
                return None
        else:
            return None
    else:
        return None







walk(point, map_of_ground)
p(map_of_ground)




# def walk(point, map_of_ground):
#     continue_ = True
#     down_pathes = []
#     while down_continue:
#         if map_of_ground[down(point)] == ".":
#             point = down(point)
#             map_of_ground[point] = "|"
#             # print(1)
#         else:
#             down_continue = False
#             left_cont = True
#             while left_continue:
#                 if map_of_ground[down(point)]:
#                     down_pathes.append(point)
#                     left_cont = False
#                 elif map_of_ground[left(point)] != "#":
#                     point = left(point)
#                     map_of_ground[point] = "~"
#                 elif map_of_ground[left(point)] == "#":
#                     left_continue = False
#                     right_continue = True
#                     while right_continue:
#                             if map_of_ground[down(point)]:
#                                 down_pathes.append(point)
#                                 left_cont = False
#                             elif map_of_ground[left(point)] != "#":
#                                 point = left(point)
#                                 map_of_ground[point] = "~"

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
