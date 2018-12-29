path = r"C:\Users\Herman\test_git\adv2.txt"

with open(path, "r") as f:
    txt_rows = f.read().splitlines()

def count_letters(letter, code_string):
    count = 0
    for a in code_string:
        if a == letter:
            count += 1
        if count > 3:
            break
    return count

#
two = 0
three = 0
c = True
for code in txt_rows:
    two_f = False
    three_f = False
    for idx, a in enumerate(code):
        count = count_letters(a, code)
        if count == 2:
            print("2:", a, code)
            two_f = True
        if count == 3:
            print("3:", a, code)
            three_f = True
        if two_f and three_f:
            break
    if two_f:
        two += 1
    if three_f:
        three += 1

print(two, three)
print(two * three)
