
# print(lista.pop(1))
# print(lista[1])
# for idx, elem in enumerate(lista):
#     print(f"[{idx}]", end=", ")
#
# #
def thing(c):
    lista = [_ for _ in range(25)]
    current = c
    print(current)
    if (current - 7) >= 0:
        current -= 7
        lista.pop(current)
    else:
        current = len(lista) + (current - 7)
        lista.pop(current)
        if current == len(lista):
            current = 0


    for idx, elem in enumerate(lista):
        if idx == current:
            print(f"[{elem}]", end=", ")
        else:
            print(elem, end=", ")
    print()

for idx in range(10):
    thing(idx)
