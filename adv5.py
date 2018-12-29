path = r"C:\Users\Herman\test_git\adv5.txt"

li = []


with open(path) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if li == []:
            li.append(c)
        elif c.upper() == li[-1].upper() and c != li[-1]:
            li.pop()
        else:
            li.append(c)
li.remove("\n")
print(len(li))
