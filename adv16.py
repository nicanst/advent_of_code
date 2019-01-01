def addr(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] + regin[B]
    if regin == regout:
        return 1
    else:
        return 0

def addi(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] + B
    if regin == regout:
        return 1
    else:
        return 0



def mulr(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] * regin[B]
    if regin == regout:
        return 1
    else:
        return 0



def muli(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] * B
    if regin == regout:
        return 1
    else:
        return 0

def banr(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] & regin[B]
    if regin == regout:
        return 1
    else:
        return 0

def bani(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] & B
    if regin == regout:
        return 1
    else:
        return 0

def borr(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] | regin[B]
    if regin == regout:
        return 1
    else:
        return 0

def bori(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A] | B
    if regin == regout:
        return 1
    else:
        return 0

def setr(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = regin[A]
    if regin == regout:
        return 1
    else:
        return 0

def seti(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    regin[C] = A
    if regin == regout:
        return 1
    else:
        return 0

def gtir(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    if A > regin[B]:
        regin[C] = 1
    else:
        regin[C] = 0
    if regin == regout:
        return 1
    else:
        return 0

def gtri(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    if regin[A] > B:
        regin[C] = 1
    else:
        regin[C] = 0
    if regin == regout:
        return 1
    else:
        return 0

def gtrr(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    if regin[A] > regin[B]:
        regin[C] = 1
    else:
        regin[C] = 0
    if regin == regout:
        return 1
    else:
        return 0

def eqir(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    if A == regin[B]:
        regin[C] = 1
    else:
        regin[C] = 0
    if regin == regout:
        return 1
    else:
        return 0

def eqri(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    if regin[A] == B:
        regin[C] = 1
    else:
        regin[C] = 0
    if regin == regout:
        return 1
    else:
        return 0

def eqrr(instr, regi, regout):
    regin = list(regi)
    op, A, B, C = instr
    if regin[A] == regin[B]:
        regin[C] = 1
    else:
        regin[C] = 0
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
for com in lista:
    if test_all(com["instr"], com["regin"], com["regout"]) > 2:
        summa += 1

print(summa)
