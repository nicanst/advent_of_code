# Rack ID: x + 10
# Power level: ((Rack ID * Y) + (puzzle input)) * Rack ID
# Power level: Ta hundradelen av ovan - 5

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


def three_three_grid(top_left_coord, grid_serial_nr):
    top_x, top_y = top_left_coord
    pow_lev = 0
    if top_x < 299 and top_y < 299:
        for x in range(top_x, top_x + 3):
            for y in range(top_y, top_y + 3):
                # print(y)
                pow_lev += power_level((x, y), grid_serial_nr)
        return pow_lev
    else:
        return 0

hi_pow_lev = 0
for x in range(1, 301):
    for y in range(1, 301):
        temp = three_three_grid((x, y), 8772)
        if temp > hi_pow_lev:
            hi_pow_lev = temp
            hi_coord = (x, y)

print(hi_pow_lev, hi_coord)
