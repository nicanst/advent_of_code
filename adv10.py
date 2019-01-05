path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv10.txt"

with open(path) as f:
    lines = f.read().splitlines()

points = {}
for idx, line in enumerate(lines):
    points[idx] = {
                    "x": int(line[10:16]),
                    "y": int(line[18:24]),
                    "velo_x": int(line[36:38]),
                    "velo_y": int(line[40:42]),
                  }
# print(points)

ett = True
count_sec = 0
for sec in range(1000000):
    count_sec += 1
    y_min = 10000
    y_max = 0
    x_min = 1000
    x_max = 0
    for idx, val in points.items():
        points[idx]["x"] = val["x"] + val["velo_x"]
        points[idx]["y"] = val["y"] + val["velo_y"]
        # print(val["y"])
        if val["y"] < y_min:
            y_min = val["y"]
        if val["y"] > y_max:
            y_max = val["y"]
        if val["x"] < x_min:
            x_min = val["x"]
        if val["x"] > x_max:
            x_max = val["x"]
    # print((y_max - y_min))
    if (y_max - y_min) < 10 and (y_max - y_min) > 0:
        print("SEKUND:", sec + 1)
        if ett:

            sky = [["." for _ in range(150)] for _ in range(20)]
            middle_y = int(1 * (y_min + ((y_max - y_min) / 2)))
            middle_x = int(1 * (x_min + ((x_max - x_min) / 2)))
            # print(y_max, y_min, y_max - y_min)
            for idx, val in points.items():
                sky[val["y"]-y_min][val["x"]-x_min] = "#"
            for li in sky:
                print(*li, sep="")







# li = []
# for line in lines:
#     li.append((int(r[10:12]), int(r[14:16])))
