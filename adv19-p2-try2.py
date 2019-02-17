import copy
#setr/seti can function as absolute jumps, addr/addi can function as relative jumps
def addr(i, r, ip = None):
    r[i[3]] = r[i[1]] + r[i[2]]
    return r

def addi(i, r, ip = None):
    r[i[3]] = r[i[1]] + i[2]
    return r

def mulr(i, r, ip = None):
    r[i[3]] = r[i[1]] * r[i[2]]
    return r

def muli(i, r):
    r[i[3]] = r[i[1]] * i[2]
    return r

def banr(i, r, ip = None):
    r[i[3]] = r[i[1]] & r[i[2]]
    return r

def bani(i, r, ip = None):
    r[i[3]] = r[i[1]] & i[2]
    return r

def borr(i, r, ip = None):
    r[i[3]] = r[i[1]] | r[i[2]]
    return r

def bori(i, r, ip = None):
    r[i[3]] = r[i[1]] | i[2]
    return r

#setr/seti can function as absolute jumps, addr/addi can function as relative jumps
def setr(i, r, ip = None):
    r[i[3]] = r[i[1]]
    return r

def seti(i, r, ip = None):
    r[i[3]] = i[1]
    return r

def gtir(i, r, ip = None):
    r[i[3]] = int(i[1] > r[i[2]])
    return r

def gtri(i, r, ip = None):
    r[i[3]] = int(r[i[1]] > i[2])
    return r

def gtrr(i, r, ip = None):
    r[i[3]] = int(r[i[1]] > r[i[2]])
    return r

def eqir(i, r, ip = None):
    r[i[3]] = int(i[1] == r[i[2]])
    return r

def eqri(i, r, ip = None):
    r[i[3]] = int(r[i[1]] == i[2])
    return r

def eqrr(i, r, ip = None):
    r[i[3]] = int(r[i[1]] == r[i[2]])
    return r

def chooser(i, r, ip = 0):
    if i[0] == "addr": return addr(i, r)
    if i[0] == "addi": return addi(i, r)
    if i[0] == "mulr": return mulr(i, r)
    if i[0] == "muli": return muli(i, r)
    if i[0] == "banr": return banr(i, r)
    if i[0] == "bani": return bani(i, r)
    if i[0] == "borr": return borr(i, r)
    if i[0] == "bori": return bori(i, r)
    if i[0] == "setr": return setr(i, r)
    if i[0] == "seti": return seti(i, r)
    if i[0] == "gtir": return gtir(i, r)
    if i[0] == "gtri": return gtri(i, r)
    if i[0] == "gtrr": return gtrr(i, r)
    if i[0] == "eqir": return eqir(i, r)
    if i[0] == "eqri": return eqri(i, r)
    if i[0] == "eqrr": return eqrr(i, r)

path = r"c:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv19.txt"
with open(path) as file:
    lines = file.read().splitlines()

#register
register = [1, 0, 0, 0, 0, 0]
#[0, 3749, 10551340, 3, 1, 0]

#instructions
instr = []
for line in lines:
    temp_ = []
    if not line.startswith("#"):
        temp_ = line.split(" ")
        temp_[1] = int(temp_[1])
        temp_[2] = int(temp_[2])
        temp_[3] = int(temp_[3])
        instr.append(temp_)

pointer = 0
from_ = 5000
to_ = 5020
count = 1
while True:
    register[3] = pointer
    if count > from_ and count < to_: print("ip=", pointer, end=" ")
    if count > from_ and count < to_: print(register, end=" ")
    if count > from_ and count < to_: print(instr[register[3]], end=" ")
    chooser(instr[register[3]],register)
    if count > from_ and count < to_: print(register, count)
    pointer = register[3]
    pointer += 1
    if 0 > pointer or pointer >= len(instr) or count > to_:
        print("halt:", register[0], count)
        break
    count += 1
