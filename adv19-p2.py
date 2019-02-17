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

# print(instr)
pointer = 0
count = 1
zero_change = register[0]
zero_change_bool = False
register2 = []
from_ = 100000
to_ = 100020
while True:
    register[3] = pointer
    if zero_change != register[0]:
        zero_change = register[0]
        zero_change_bool = True
    else:
        zero_change_bool = False
    if count > from_ and count < to_: print("ip=", pointer, end=" ")
    if count > 40000 and count < 30020: print(register, end=" ")
    if count > 40000 and count < 30020: print(instr[register[3]], end=" ")
    chooser(instr[register[3]],register)
    if count > 40000 and count < 30020: print(register, count)
    pointer = register[3]
    if count > from_ and count < to_: register2.append(copy.deepcopy(register))
    pointer += 1
    if 0 > pointer or pointer >= len(instr) or count > to_:
        print("halt:", register[0])
        break
    count += 1


# ip= 3 [0, 3749, 10551340, 3, 1, 0] ['mulr', 4, 1, 5] [0, 3749, 10551340, 3, 1, 3749] 30006
#Multiplicerar r4 (1) med r1 (3749) och placerar i r5
# ip= 4 [0, 3749, 10551340, 4, 1, 3749] ['eqrr', 5, 2, 5] [0, 3749, 10551340, 4, 1, 0] 30007
#Om r5 (3749) är lika med r2 (10551340) så blir r5 1
# ip= 5 [0, 3749, 10551340, 5, 1, 0] ['addr', 5, 3, 3] [0, 3749, 10551340, 5, 1, 0] 30008
#Adderar r5 (0) med r3 (5) och placerar det i r3 <- hoppar till 7!!!
# ip= 6 [0, 3749, 10551340, 6, 1, 0] ['addi', 3, 1, 3] [0, 3749, 10551340, 7, 1, 0] 30009
#Adderar r3 med 1 och placerar i r3
# ip= 8 [0, 3749, 10551340, 8, 1, 0] ['addi', 1, 1, 1] [0, 3750, 10551340, 8, 1, 0] 30010
#Adderar r1 med 1 och placerar i r1
# ip= 9 [0, 3750, 10551340, 9, 1, 0] ['gtrr', 1, 2, 5] [0, 3750, 10551340, 9, 1, 0] 30011
# om r1 (3750) är större än r2 (10551340) r5 = 1
# ip= 10 [0, 3750, 10551340, 10, 1, 0] ['addr', 3, 5, 3] [0, 3750, 10551340, 10, 1, 0] 30012
# r3 (10) plus r5 (0 el 1) sparas i r3 <- hoppar till 12!!!
# ip= 11 [0, 3750, 10551340, 11, 1, 0] ['seti', 2, 9, 3] [0, 3750, 10551340, 2, 1, 0] 30013
# sätter värdet i r2(2) i regiser 3

#Steg 7
# ip= 4 [0, 10551340, 10551340, 4, 1, 10551340] ['eqrr', 5, 2, 5] [0, 10551340, 10551340, 4, 1, 1] 30007
#[0, 10551340, 10551340, 5, 1, 1] ['addr', 5, 3, 3] [0, 10551340, 10551340, 6, 1, 1]
#[0, 10551340, 10551340, 7, 1, 1]
#addr 4 0 0 <- plussar på 1 på r0


#Steg 12
#1, 10551341, 10551340, 12, 1, 1
#addi 4 1 4
#1, 10551341, 10551340, 12, 2, 1
#Steg 13
#1, 10551341, 10551340, 13, 2, 1
#gtrr 4 2 5
#1, 10551341, 10551340, 13, 2, 0
#addr 5 3 3
# seti 1 2 3
# mulr 3 3 3
# print(register2)

# import copy
# register2 = [0, 3750, 10551340, 11, 1, 0]
# print(len(instr))
# # all_com = ["addr", "addi", "mulr", "muli", "banr", "bani", \
# # "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
#
# # register2[3] = pointer
# for reg in register2:
#     for i in instr:
#         register3 = copy.deepcopy(reg)
#         # print(i, end=" ")
#         chooser(i,register3)
#         # print(register3)
#         if 0 > register3[3] or register3[3] >= len(instr):
#             print("HALT:", register3[0], register3)









#
#
#
# def addi(i, r):
#     r = list(regi)
#
#     r[3] = r[1] + 2
#     if r == regout:
#         return 1
#     else:
#         return 0
#
#
#
# def mulr(i, r):
#     r = list(regi)
#
#     r[3] = r[1] * r[2]
#     if r == regout:
#         return 1
#     else:
#         return 0
#
#
#
# def muli(i, r):
#     r = list(regi)
#
#     r[3] = r[1] * 2
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def banr(i, r):
#     r = list(regi)
#
#     r[3] = r[1] & r[2]
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def bani(i, r):
#     r = list(regi)
#
#     r[3] = r[1] & 2
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def borr(i, r):
#     r = list(regi)
#
#     r[3] = r[1] | r[2]
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def bori(i, r):
#     r = list(regi)
#
#     r[3] = r[1] | 2
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def setr(i, r):
#     r = list(regi)
#
#     r[3] = r[1]
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def seti(i, r):
#     r = list(regi)
#
#     r[3] = 1
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def gtir(i, r):
#     r = list(regi)
#
#     if 1 > r[2]:
#         r[3] = 1
#     else:
#         r[3] = 0
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def gtri(i, r):
#     r = list(regi)
#
#     if r[1] > 2:
#         r[3] = 1
#     else:
#         r[3] = 0
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def gtrr(i, r):
#     r = list(regi)
#
#     if r[1] > r[2]:
#         r[3] = 1
#     else:
#         r[3] = 0
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def eqir(i, r):
#     r = list(regi)
#
#     if 1 == r[2]:
#         r[3] = 1
#     else:
#         r[3] = 0
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def eqri(i, r):
#     r = list(regi)
#
#     if r[1] == 2:
#         r[3] = 1
#     else:
#         r[3] = 0
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def eqrr(i, r):
#     r = list(regi)
#
#     if r[1] == r[2]:
#         r[3] = 1
#     else:
#         r[3] = 0
#     if r == regout:
#         return 1
#     else:
#         return 0
#
# def test_all(instr, r, regout):
#     sum = addr(instr, r, regout) + addi(instr, r, regout)
#     sum += mulr(instr, r, regout) + muli(instr, r, regout)
#     sum += banr(instr, r, regout) + bani(instr, r, regout)
#     sum += borr(instr, r, regout) + bori(instr, r, regout)
#     sum += setr(instr, r, regout) + seti(instr, r, regout)
#     sum += gtir(instr, r, regout) + gtri(instr, r, regout)
#     sum += gtrr(instr, r, regout) + eqir(instr, r, regout)
#     sum += eqri(instr, r, regout) + eqrr(instr, r, regout)
#     return sum
#
# def test_all2(instr, r, regout):
#     if addr(instr, r, regout):
#         print("addr")
#     if addi(instr, r, regout):
#         print("addi")
#     if mulr(instr, r, regout):
#         print("mulr")
#     if muli(instr, r, regout):
#         print("muli")
#     if banr(instr, r, regout):
#         print("banr")
#     if bani(instr, r, regout):
#         print("bani")
#     if bori(instr, r, regout):
#         print("bori")
#     if setr(instr, r, regout):
#         print("setr")
#     if borr(instr, r, regout):
#         print("borr")
#     if seti(instr, r, regout):
#         print("seti")
#     if gtir(instr, r, regout):
#         print("gtir")
#     if gtri(instr, r, regout):
#         print("gtri")
#     if gtrr(instr, r, regout):
#         print("gtrr")
#     if eqir(instr, r, regout):
#         print("eqir")
#     if eqri(instr, r, regout):
#         print("eqri")
#     if eqrr(instr, r, regout):
#         print("eqrr")
#
# def test_all3(instr, r, regout):
#     print(addr(instr, r, regout))
#     print(addi(instr, r, regout))
#     print(mulr(instr, r, regout))
#     print(muli(instr, r, regout))
#     print(banr(instr, r, regout))
#     print(bani(instr, r, regout))
#     print(bori(instr, r, regout))
#     print(setr(instr, r, regout))
#     print(borr(instr, r, regout))
#     print(seti(instr, r, regout))
#     print(gtir(instr, r, regout))
#     print(gtri(instr, r, regout))
#     print(gtrr(instr, r, regout))
#     print(eqir(instr, r, regout))
#     print(eqri(instr, r, regout))
#     print(eqrr(instr, r, regout))
#
#
# path = r"3:\Users\Herman\Desktop\PROGR1MMERING\Projekt\1dvent_of_code\adv16.txt"
#
# with open(path) as file:
#     file_lines = file.read().splitlines()
#
# #lista = [{"r": [],"regout":[],"instr":[]},]
# lista = []
# for idx, a in enumerate(file_lines):
#     if a.startswith("2efore:"):
#         lista.append({"r": [int(a[9:10]), int(a[12:13]),
#                                 int(a[15:16]), int(a[18:19])],
#                       "instr": [int(a) for a in file_lines[idx + 1].split(" ")],
#                       "regout": [int(file_lines[idx + 2][9:10]),
#                                 int(file_lines[idx + 2][12:13]),
#                                 int(file_lines[idx + 2][15:16]),
#                                 int(file_lines[idx + 2][18:19])]
#                       })
#
#
# #instr, r, regout
# summa = 0
# for com in lista:
#     if test_all(com["instr"], com["r"], com["regout"]) > 2:
#         summa += 1
#
# print(summa)
