path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv1.txt"

with open(path, "r") as f:
    txt_rows = f.read().splitlines()

tal_list_m = [0,]
tal_list_p = [0,]
tal = 0
olika = True
while olika:
    for t in txt_rows:
        if t.startswith("-"):
            tal -= int(t[1:])
        elif t.startswith("+"):
            tal += int(t[1:])
        if tal > 0:
            if tal in tal_list_p:
                print(tal)
                olika = False
                break
            else:
                tal_list_p.append(tal)
        elif tal < 0:
            if tal in tal_list_m:
                print(tal)
                olika = False
                break
            else:
                tal_list_m.append(tal)
        else:
            print(tal)
            olika = False
            break
