def game(p, last_marble):
    circle = [0]
    scores = [0 for _ in range(p + 1)]
    current = None
    players = p
    player = 1
    for marble in range(1, last_marble):
        if len(circle) == 1:
            circle.append(marble)
            current = 1
        else:
            if marble % 23 == 0:
                if (current - 7) >= 0:
                    current -= 7
                    scores[player] += circle.pop(current)
                    scores[player] += marble
                else:
                    current = len(circle) + (current - 7)
                    scores[player] += circle.pop(current)
                    scores[player] += marble
                    if current == len(circle):
                        current = 0
            else:
                if current + 2 == len(circle):
                    circle.append(marble)
                    current = len(circle) - 1
                elif current + 2 > len(circle):
                    circle.insert(1, marble)
                    current = 1
                else:
                    circle.insert(current + 2, marble)
                    current += 2
        # print(player, end=" | ")
        if player == None:
            player = 1
        elif player >= players:
            player = 1
        else:
            player += 1

        # for idx, elem in enumerate(circle):
        #     if idx == current:
        #         print(f"[{elem}]", end=", ")
        #     else:
        #         print(elem, end=", ")
    print(max(scores))
#Game input: 477 players; last marble is worth 70851 points
game(477,70851*100)
# game(477, 70851)
# game(477, 70851*2)
# game(477, 70851*4)

# 374690
# 1365586
# 5123352

# print(1365586 / 374690)
# print(5123352 / 1365586)
