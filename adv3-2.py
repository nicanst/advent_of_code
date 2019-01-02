path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv3.txt"

with open(path, "r") as f:
    lines = f.read().splitlines()

claim_dict = {}
for li in lines:
    claim, temp = li.split("@")
    claim = int(claim.strip("#"))
    x_y, temp2 = temp.split(":")
    x,y = x_y.split(",")
    x = int(x)
    y = int(y)
    wi, he = temp2.split("x")
    he = int(he)
    wi = int(wi)
    #print(x,y,he,wi,claim)
    claim_dict[claim] = [x,y,he,wi]

area = [[] for _ in range(1000)]
for id_ in range(1000):
    area[id_] = ["." for _ in range(1000)]

area_small = [[] for _ in range(10)]
for id_ in range(10):
    area_small[id_] = ["." for _ in range(10)]



for k, v in claim_dict.items():
    x1, y1, he, wi = v
    for x in range(x1, x1 + wi):
        for y in range(y1, y1 + he):
            if area[y][x] == ".":
                area[y][x] = k
            else:
                area[y][x] = "X"

for k, v in claim_dict.items():
    x1, y1, he, wi = v
    passed = True
    for x in range(x1, x1 + wi):
        for y in range(y1, y1 + he):
            if area[y][x] != k:
                passed = False
    if passed:
        print(k)



# for a in area:
#     for b in a:
#         print(b, end="")
#     print()
