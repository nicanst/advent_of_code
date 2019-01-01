p = []
p.append(["#","#","#","#","#","#","#","#","#"])
p.append(["#","X",".",".",".",".",".",".","#"])
p.append(["#",".",".",".",".",".",".",".","#"])
p.append(["#",".",".",".",".",".",".",".","#"])
p.append(["#",".",".",".","#",".",".",".","#"])
p.append(["#",".",".",".",".",".",".",".","#"])
p.append(["#",".",".",".",".",".",".",".","#"])
p.append(["#",".",".",".",".",".",".",".","#"])
p.append(["#","#","#","#","#","#","#","#","#"])

def ways(p, x, y):
    lista = []
    y_max = len(p)
    x_max = len(p[0])
    if x < x_max and y < y_max:
        if (y + 1) < y_max and p[y + 1][x] == ".":
            lista.append((x,y+1))
        if y != 0 and p[y - 1][x] == ".":
            lista.append((x,y-1))
        if (x + 1) < x_max and p[y][x + 1] == ".":
            lista.append((x+1,y))
        if x != 0 and p[y][x - 1] == ".":
            lista.append((x-1,y))
    return(lista)

x1 = 1
y1 = 1
x2 = 4
y2 = 4

p2 = list(p)
print(ways(p2,7,8))

p2[y2 + 1][x2 + 0] = 1
p2[y2 - 1][x2 + 0] = 1
p2[y2 + 0][x2 + 1] = 1
p2[y2 + 0][x2 - 1] = 1
