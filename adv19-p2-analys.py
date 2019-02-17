Programmet plussar på 1 på register1 och när den nått 10551340 börjar den om igen
Programmet plussar på 1 på register4 när register1 nått högsta punkt
Om multiplikationen register1 * register 4 är lika med 10551340 så plussas talet i
register4 ihop med talet i register0 och läggs sedan i register0
Med andra ord så letar programmet fram de heltal som gånger varandra blir 10551340
och adderar ihop dem. Kan göras om till denna kodsnutt:

sum = []
for tal1 in range(1, 10551340 + 1):
    if 10551340 % tal1 == 0:
            sum.append(tal1)
print(sum)
sum2 = 0
for a in sum:
    sum2 += a
print(sum2)


# ip= 3 [0, 624, 10551340, 3, 1, 0] ['mulr', 4, 1, 5] [0, 624, 10551340, 3, 1, 624] 5006
#Multiplicerar r4 (1) med r1 (624) och placerar i r5
# ip= 4 [0, 624, 10551340, 4, 1, 624] ['eqrr', 5, 2, 5] [0, 624, 10551340, 4, 1, 0] 5007
#Om r5 (624) är lika med r2 (10551340) så blir r5 1
# ip= 5 [0, 624, 10551340, 5, 1, 0] ['addr', 5, 3, 3] [0, 624, 10551340, 5, 1, 0] 5008
#Adderar r5 (0 eller 1) med r3 (5) och placerar det i r3 <- hoppar till 7!!!
# ip= 6 [0, 624, 10551340, 6, 1, 0] ['addi', 3, 1, 3] [0, 624, 10551340, 7, 1, 0] 5009
#Adderar r3 med 1 och placerar i r3 <- går till 8
# ip= 8 [0, 624, 10551340, 8, 1, 0] ['addi', 1, 1, 1] [0, 625, 10551340, 8, 1, 0] 5010
#Adderar r1 med 1 och placerar i r1 - ökar r1 med 1
# ip= 9 [0, 625, 10551340, 9, 1, 0] ['gtrr', 1, 2, 5] [0, 625, 10551340, 9, 1, 0] 5011
# om r1 (10551340) är större än r2 (10551340) r5 = 1
# ip= 10 [0, 625, 10551340, 10, 1, 0] ['addr', 3, 5, 3] [0, 625, 10551340, 10, 1, 0] 5012
# r3 (10) plus r5 (0 el 1) sparas i r3 <- hoppar till 12!!!
# ip= 11 [0, 625, 10551340, 11, 1, 0] ['seti', 2, 9, 3] [0, 625, 10551340, 2, 1, 0] 5013
# sätter värdet i r2(2) i regiser 3 - hoppar tillbaka till 2

#Steg 7
# ip= 4 [0, 10551340, 10551340, 4, 1, 10551340] ['eqrr', 5, 2, 5] [0, 10551340, 10551340, 4, 1, 1] 30007
#[0, 10551340, 10551340, 5, 1, 1] ['addr', 5, 3, 3] [0, 10551340, 10551340, 6, 1, 1]
#[0, 10551340, 10551340, 7, 1, 1]
#addr 4 0 0 <- adderar register 4 och register 0 och lägger det i 0

#Steg 12
addi (add immediate) stores into register C the result of adding register A and value B.
addi 4 1 4
[0, 625, 10551340, 12, 1, 0]
r4 plussas på 1

steg 13
gtrr (greater-than register/register) sets register C to 1 if
register A is greater than register B. Otherwise, register C is set to 0.
gtrr 4 2 5
[0, 625, 10551340, 12, 1, 0]
om r4 är större än r2 sätts r5 till 1

Steg 14
addr 5 3 3
addr (add register) stores into register C the result of adding register A and register B.
adderar 1 eller 0 till steg

steg 15
seti (set immediate) stores value A into register C. (Input B is ignored.)
seti 1 2 3
går till steg 2

Steg 2
seti 1 0 1
Sätter r1 till 1


steg 16
mulr 3 3 3
halt...


#
