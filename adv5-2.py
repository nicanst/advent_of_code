path = r"C:\Users\Herman\test_git\ad5-short.txt"
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
        units.append(ch)
print(units)

for unit in units:
    li_copy = list(li)
    li_copy.remove(unit)
    li_copy.remove(unit.upper())



#
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
