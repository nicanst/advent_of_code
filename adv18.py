import copy

# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.deepcopy(old_list)
# old_list[0][0] = 2
#
# print("Old list:", old_list)
# print("New list:", new_list)



path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv18.txt"

with open(path) as file:
    file_lines = file.read().splitlines()

area = []
area2 = []
for line in file_lines:
    area.append([ch for ch in line])
for line in file_lines:
    area2.append([" " for ch in line])
y_max = len(area)
x_max = len(area[0])
for _ in range(10):

    for y, li in enumerate(area):
        for x, ch in enumerate(li):
            ground = 0
            trees = 0
            lumber = 0
            coords = ((x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y),
                    (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1))
            for coord in coords:
                x2, y2 = coord
                if x2 >= 0 and y2 >= 0 and x2 < x_max and y2 < y_max:
                    if area[y2][x2] == ".":
                        ground += 1
                    elif area[y2][x2] == "|":
                        trees += 1
                    elif area[y2][x2] == "#":
                        lumber += 1

            if area[y][x] == ".":
                if trees >= 3:
                    area2[y][x] = "|"
                else:
                    area2[y][x] = "."
            elif area[y][x] == "|":
                if lumber >= 3:

                    area2[y][x] = "#"
                else:
                    area2[y][x] = "|"
            elif area[y][x] == "#":
                # 8 0 l 3 t 1
                if lumber > 0 and trees > 0:

                    area2[y][x] = "#"
                else:
                    area2[y][x] = "."
    area = copy.deepcopy(area2)

woody = 0
lumbers = 0
for li in area2:
    for ab in li:
        if ab == "|":
            woody += 1
        if ab == "#":
            lumbers += 1


print(woody * lumbers)
