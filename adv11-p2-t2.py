#Fungerar dåligt, borde göras om


import pprint
# # Rack ID: x + 10
# # Power level: ((Rack ID * Y) + (puzzle input)) * Rack ID
# # Power level: Ta hundradelen av ovan - 5
#
def power_level(coord, grid_serial_nr):
    x, y = coord
    rack_id = x + 10
    pow_lev = rack_id * y
    pow_lev += grid_serial_nr
    pow_lev *= rack_id
    pow_lev_st = str(pow_lev)
    if len(pow_lev_st) < 3:
        return -5
    else:
        return int(pow_lev_st[-3]) - 5
#
#
# def three_three_grid(top_left_coord, grid_serial_nr):
#     top_x, top_y = top_left_coord
#     pow_lev = 0
#     if top_x < 299 and top_y < 299:
#         for x in range(top_x, top_x + 3):
#             for y in range(top_y, top_y + 3):
#                 # print(y)
#                 pow_lev += power_level((x, y), grid_serial_nr)
#         return pow_lev
#     else:
#         return 0
#
def any_size_grid(top_left_coord, square_size, grid):
    top_x, top_y = top_left_coord
    pow_lev = 0
    if (top_x + square_size) <= 301 and (top_y + square_size) <= 301:
        for x in range(top_x, top_x + square_size):
            for y in range(top_y, top_y + square_size):
                pow_lev += grid[(x,y)]
        return pow_lev
    else:
        return 0
#
hi_pow_lev = 0
next_ = 0
# for square_size in range(3, 300):
grid = {}

for x in range(1, 301):
    for y in range(1, 301):
        grid[(x,y)] = power_level((x, y), 8772)

# for square_size in range (1, 300):
maxi = 0
next_ = 0
for square_size in range(2, 301):
    for x in range(1, 301):
        for y in range(1, 301):
            temp = any_size_grid((x,y), square_size, grid)
            if maxi < temp:
                print(x,y,square_size)
                maxi = temp
            if next_ < square_size:
                print(square_size)
                next_ = square_size


# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(grid)
            # # for square in range(2, 50):
            # temp = any_size_grid((x, y), square_size, 18)
            # if hi_pow_lev < temp:
            #     hi_pow_lev = temp
            #     pos = (x,y)
            #     square_hi = square_size
            #     if next_ < square_size:
            #         next_ = square_size
            #         print(next_)
            #     print(pos, square_hi, hi_pow_lev)
