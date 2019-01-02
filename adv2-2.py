path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv2.txt"

with open(path, "r") as f:
    lines = f.read().splitlines()

start_idx = 0
for this_idx, this_li in enumerate(lines):
    for comp_idx, comp_li in enumerate(lines):
        mismatch_count = 0
        if this_idx < comp_idx:
            for this_ch_idx, this_ch in enumerate(this_li):
                if this_ch != comp_li[this_ch_idx]:
                    mismatch_count += 1
        if mismatch_count == 1:
            for this_ch_idx, this_ch in enumerate(this_li):
                if this_ch == comp_li[this_ch_idx]:
                    print(this_ch, end="")
            break
