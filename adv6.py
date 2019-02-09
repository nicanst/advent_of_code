path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv6-short.txt"

# def around(x, y, xmax = 10, ymax = 10):
#     list_ = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
#     list_ = [c for c in list_ if c[0] >= 0 and c[1] >= 0]
#     list_ = [c for c in list_ if c[0] <= xmax and c[1] <= ymax]
#     return list_
#
# def test_around(x, y, grid):
#     around2 = around(x, y)
#     letter = '.'
#     for coord in around2:
#         x, y = coord
#         if grid[y][x] != '.':
#             if letter != '.':
#                 letter = 'x'
#             else:
#                 letter = grid[y][x]
#     return letter
#
#
# def get_grid(coords):
#     xmax = 0
#     ymax = 0
#     for key, coord in coords.items():
#         if coord["x"] > xmax:
#             xmax = coord["x"] + 2
#         if coord["y"] > ymax:
#             ymax = coord["y"] + 2
#     grid = [["." for _ in range(xmax)] for _ in range(ymax)]
#     for key, coord in coords.items():
#         grid[coord["y"]][coord["x"]] = key
#     return grid
#     # for row in grid:
#     #     for col in row:
#     #         print(col, end="")
#     #     print()


with open(path) as f:
    lines = f.read().splitlines()

coord = {}
coord2 = {}
for idx, line in enumerate(lines):
    x, y = map(int, line.split(", "))
    coord[idx] = {"x": x, "y": y}
    coord2[idx] = (x, y)
# grid = get_grid(coord)

print(coord, coord2)

# # for _ in range(5):
# for y, row in enumerate(grid):
#     for x, cont in enumerate(row):
#         if cont == ".":
#             grid[y][x] = test_around(x,y,grid)
#
# for a in grid:
#     for b in a:
#         print(b, end="")
#     print()

# xmax = 0
# xmin = 100
# for x2 in xs:
#     if xmax < x2:
#         xmax = x2
#     if xmin > x2:
#         xmin = x2
#
# ymax = 0
# ymin = 100
# for y2 in ys:
#     if ymax < y2:
#         ymax = y2
#     if ymin > y2:
#         ymin = y2
#
# for idx in range(len(xs)):
#     print(xs[idx])
