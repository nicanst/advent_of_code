import pprint

def addr(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] + regin[B]
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def addi(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] + B
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0



def mulr(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] * regin[B]
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0



def muli(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] * B
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def banr(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] & regin[B]
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def bani(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] & B
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def borr(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] | regin[B]
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def bori(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] | B
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def setr(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A]
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def seti(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = A
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def gtir(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    if A > regin[B]:
        regin[C] = 1
    else:
        regin[C] = 0
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def gtri(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    if regin[A] > B:
        regin[C] = 1
    else:
        regin[C] = 0
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def gtrr(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    if regin[A] > regin[B]:
        regin[C] = 1
    else:
        regin[C] = 0
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def eqir(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    if A == regin[B]:
        regin[C] = 1
    else:
        regin[C] = 0
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def eqri(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    if regin[A] == B:
        regin[C] = 1
    else:
        regin[C] = 0
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0

def eqrr(instr, regi, regout, out=False):
    regin = list(regi)
    op, A, B, C = instr
    if regin[A] == regin[B]:
        regin[C] = 1
    else:
        regin[C] = 0
    if out: return regin
    if regin == regout:
        return 1
    else:
        return 0



def test_all(instr, regin, regout):
    sum = addr(instr, regin, regout) + addi(instr, regin, regout)
    sum += mulr(instr, regin, regout) + muli(instr, regin, regout)
    sum += banr(instr, regin, regout) + bani(instr, regin, regout)
    sum += borr(instr, regin, regout) + bori(instr, regin, regout)
    sum += setr(instr, regin, regout) + seti(instr, regin, regout)
    sum += gtir(instr, regin, regout) + gtri(instr, regin, regout)
    sum += gtrr(instr, regin, regout) + eqir(instr, regin, regout)
    sum += eqri(instr, regin, regout) + eqrr(instr, regin, regout)
    return sum

def test_all2(instr, regin, regout):
    if addr(instr, regin, regout):
        print("addr")
    if addi(instr, regin, regout):
        print("addi")
    if mulr(instr, regin, regout):
        print("mulr")
    if muli(instr, regin, regout):
        print("muli")
    if banr(instr, regin, regout):
        print("banr")
    if bani(instr, regin, regout):
        print("bani")
    if bori(instr, regin, regout):
        print("bori")
    if setr(instr, regin, regout):
        print("setr")
    if borr(instr, regin, regout):
        print("borr")
    if seti(instr, regin, regout):
        print("seti")
    if gtir(instr, regin, regout):
        print("gtir")
    if gtri(instr, regin, regout):
        print("gtri")
    if gtrr(instr, regin, regout):
        print("gtrr")
    if eqir(instr, regin, regout):
        print("eqir")
    if eqri(instr, regin, regout):
        print("eqri")
    if eqrr(instr, regin, regout):
        print("eqrr")


def test_all3(instr, regin, regout):
    print(addr(instr, regin, regout))
    print(addi(instr, regin, regout))
    print(mulr(instr, regin, regout))
    print(muli(instr, regin, regout))
    print(banr(instr, regin, regout))
    print(bani(instr, regin, regout))
    print(bori(instr, regin, regout))
    print(setr(instr, regin, regout))
    print(borr(instr, regin, regout))
    print(seti(instr, regin, regout))
    print(gtir(instr, regin, regout))
    print(gtri(instr, regin, regout))
    print(gtrr(instr, regin, regout))
    print(eqir(instr, regin, regout))
    print(eqri(instr, regin, regout))
    print(eqrr(instr, regin, regout))

def test_all4(instr, regin, regout):
    if addr(instr, regin, regout):
        return "addr"
    if addi(instr, regin, regout):
        return "addi"
    if mulr(instr, regin, regout):
        return "mulr"
    if muli(instr, regin, regout):
        return "muli"
    if banr(instr, regin, regout):
        return "banr"
    if bani(instr, regin, regout):
        return "bani"
    if bori(instr, regin, regout):
        return "bori"
    if setr(instr, regin, regout):
        return "setr"
    if borr(instr, regin, regout):
        return "borr"
    if seti(instr, regin, regout):
        return "seti"
    if gtir(instr, regin, regout):
        return "gtir"
    if gtri(instr, regin, regout):
        return "gtri"
    if gtrr(instr, regin, regout):
        return "gtrr"
    if eqir(instr, regin, regout):
        return "eqir"
    if eqri(instr, regin, regout):
        return "eqri"
    if eqrr(instr, regin, regout):
        return "eqrr"

def test_all6(instr, regin, regout):
    com_lista = []
    if addr(instr, regin, regout):
        com_lista.append("addr")
    if addi(instr, regin, regout):
        com_lista.append("addi")
    if mulr(instr, regin, regout):
        com_lista.append("mulr")
    if muli(instr, regin, regout):
        com_lista.append("muli")
    if banr(instr, regin, regout):
        com_lista.append("banr")
    if bani(instr, regin, regout):
        com_lista.append("bani")
    if bori(instr, regin, regout):
        com_lista.append("bori")
    if setr(instr, regin, regout):
        com_lista.append("setr")
    if borr(instr, regin, regout):
        com_lista.append("borr")
    if seti(instr, regin, regout):
        com_lista.append("seti")
    if gtir(instr, regin, regout):
        com_lista.append("gtir")
    if gtri(instr, regin, regout):
        com_lista.append("gtri")
    if gtrr(instr, regin, regout):
        com_lista.append("gtrr")
    if eqir(instr, regin, regout):
        com_lista.append("eqir")
    if eqri(instr, regin, regout):
        com_lista.append("eqri")
    if eqrr(instr, regin, regout):
        com_lista.append("eqrr")

    return com_lista


def go_to_func(op, instr, regin, regout):
    if op == 1:
        return addr(instr, regin, regout, True)
    if op == 9:
        return addi(instr, regin, regout, True)
    if op == 0:
        return mulr(instr, regin, regout, True)
    if op == 4:
        return muli(instr, regin, regout, True)
    if op == 2:
        return banr(instr, regin, regout, True)
    if op == 13:
        return bani(instr, regin, regout, True)
    if op == 15:
        return bori(instr, regin, regout, True)
    if op == 5:
        return setr(instr, regin, regout, True)
    if op == 12:
        return borr(instr, regin, regout, True)
    if op == 14:
        return seti(instr, regin, regout, True)
    if op == 10:
        return gtir(instr, regin, regout, True)
    if op == 7:
        return gtri(instr, regin, regout, True)
    if op == 11:
        return gtrr(instr, regin, regout, True)
    if op == 3:
        return eqir(instr, regin, regout, True)
    if op == 6:
        return eqri(instr, regin, regout, True)
    if op == 8:
        return eqrr(instr, regin, regout, True)

path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv16.txt"

with open(path) as file:
    file_lines = file.read().splitlines()

#lista = [{"regin": [],"regout":[],"instr":[]},]
lista = []
for idx, a in enumerate(file_lines):
    if a.startswith("Before:"):
        lista.append({"regin": [int(a[9:10]), int(a[12:13]),
                                int(a[15:16]), int(a[18:19])],
                      "instr": [int(a) for a in file_lines[idx + 1].split(" ")],
                      "regout": [int(file_lines[idx + 2][9:10]),
                                int(file_lines[idx + 2][12:13]),
                                int(file_lines[idx + 2][15:16]),
                                int(file_lines[idx + 2][18:19])]
                      })


#instr, regin, regout
summa = 0
commands = {}
for com in lista:
    possible_commands = test_all6(com["instr"], com["regin"], com["regout"])
    op = com["instr"][0]
    if not op in commands:
        commands[op] = possible_commands
    else:
        temp_list = []
        for c in possible_commands:
            if c in commands[op]:
                temp_list.append(c)
        commands[op] = temp_list

fortsatt = True
while fortsatt:
    fortsatt = False
    for k,v in commands.items():
        if len(v) == 1:
            for k2,v2 in commands.items():
                if k != k2 and v[0] in commands[k2]:
                    commands[k2].remove(v[0])
                    fortsatt = True

# Prints the nicely formatted dictionary
pprint.pprint(commands)





path2 = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv16-2.txt"

with open(path2) as file2:
    file_lines2 = file2.read().splitlines()

testad = True
start = [1, 1, 3, 0]
regin = None
for line in file_lines2:
    if regin == None:
        regin = start
    instr = [int(a) for a in line.split(" ")]
    op = instr[0]
    regin = go_to_func(op, instr, regin, 0)

print(regin)
