# with open(path) as f:
#     while True:
#         c = f.read(1)
#         if not c:
#             break
#         if li == []:
#             li.append(c)
#         elif c.upper() == li[-1].upper() and c != li[-1]:
#             li.pop()
#         else:
#             li.append(c)
# li.remove("\n")
# print(len(li))


path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv5.txt"
li = []
with open(path) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            li.append(c)
li.remove("\n")
# for a in li:
#     print(a, end="")

units = []
for ch in li:
    if ch.lower() not in units:
        units.append(ch.lower())
print(units)

smallest = 100000
for unit in units:
    li_copy = [v for v in li if v.lower() != unit.lower()]


    li2 = []
    for c in li_copy:
        if li2 == []:
            li2.append(c)
        elif c.upper() == li2[-1].upper() and c != li2[-1]:
            li2.pop()
        else:
            li2.append(c)
    # print(unit, li2, len(li2))
    if len(li2) < smallest:
        smallest = len(li2)
print(smallest)

#
