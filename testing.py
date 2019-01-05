path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv1-short.txt"

with open(path, "r") as f:
    lines = f.read().splitlines()
    data = [int(line) for line in lines]

sums = [0] + data
print(sums)

test = " sadfa "
print(f"-{test.strip()}-")
