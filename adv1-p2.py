path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv1.txt"

with open(path, "r") as f:
    txt_rows = f.read().splitlines()

lista = []
for a in txt_rows:
    lista.append(int(a))

found = False
pointer = 0
freq = 0
avbrott = 1000000
earlier_freq = {0}
rounds = 0
while not found and avbrott > 0:
    rounds += 1
    if pointer == len(lista):
        pointer = 0
    freq = freq + lista[pointer]
    pointer += 1
    if freq in earlier_freq:
        found = True
        print(freq, rounds)
    else:
        earlier_freq.add(freq)
    avbrott -= 1
