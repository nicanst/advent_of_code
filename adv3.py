path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv3.txt"

with open(path, "r") as f:
    txt = f.read().splitlines()
printa = True
string_lista = []
x_max = 0
y_max = 0

for a in range(1000):
    string_lista.append([])
for y in string_lista:
    for i in range(1000):
        y.append(0)


for a in txt:
    if printa:
        for idx, b in enumerate(a):
            if b == "@":
                snabela = idx
            if b == ":":
                kolon = idx
        x, y = a[snabela:kolon].strip("@ ").split(",")
        w, h = a[kolon:].strip(": ").split("x")
        x, y, w, h = (int(x), int(y), int(w), int(h))
        for row in range(y, (y + h)):
            for col in range(x, (x + w)):
                string_lista[row][col] += 1

count = 0
for idx in range(1000):
    for idx2 in range(1000):
        if string_lista[idx][idx2] > 1:
            count += 1

print(count)
