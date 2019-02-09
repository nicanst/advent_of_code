from collections import deque
def game(p, last_marble, printa = False):
    circle = deque([0])
    circle2 = deque([0])
    scores = [0 for _ in range(1, p + 2)]
    # print(scores)
    current = None
    players = p
    player = 1

    for marble in range(1, last_marble + 1):
        if len(circle) == 1:
            circle.append(marble)
        else:
            if marble % 23 == 0:
                for _ in range(7):
                    temp = circle.pop()
                    circle.appendleft(temp)
                scores[player] += circle.pop() + marble
                temp = circle.popleft()
                circle.append(temp)
            else:
                temp = circle.popleft()
                circle.append(temp)
                circle.append(marble)
        if printa: print(player, end=" | ")
        if player == None:
            player = 1
        elif player >= players:
            player = 1
        else:
            player += 1

        if printa:
            for idx, elem in enumerate(circle):
                if idx == current:
                    print(f"[{elem}]", end=", ")
                else:
                    print(elem, end=", ")
            print()
    print(f"Max: {max(scores)}")
#Game input: 477 players; last marble is worth 70851 points
# game(477, 70851)
# game(477, 70851*2)
# game(477, 70851*4)

# 374690
# 1365586
# 5123352
game(477, 70851*100)
