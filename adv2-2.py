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
    count = 0
    for code_match in txt_rows:
        for a in code:
            for b in code_match:
                if a != b:
                    count += 1:
                    if count > 1:
                        break
