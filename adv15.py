


class Player(object):
    """docstring forPlayer."""
    id = 0
    def __init__(self, type_, x, y, place_in_queue, board):
        self.type = type_
        self.x = x
        self.y = y
        Player.id += 1
        self.id = Player.id
        self.place_in_queue = place_in_queue
        self.in_range = self.pos_in_range(board)

    def pos_in_range(self, board):
        pass


class Board(object):
    """docstring for test."""
    def __init__(self, path):
        with open(path) as file:
            file_lines = file.read().splitlines()
        self.clean_layout = []
        self.current_layout = []
        for idx, line in enumerate(file_lines):
            self.clean_layout.append([])
            self.current_layout.append([])
            for ch in line:
                self.current_layout[idx].append(ch)
                if ch == "G" or ch == "E":
                    self.clean_layout[idx].append(".")
                else:
                    self.clean_layout[idx].append(ch)

    def print_layout(self, clean = False, return_string = False):
        if clean or clean == "clean":
            layout = self.clean_layout
        else:
            layout = self.current_layout
        string_ = ""
        for line in layout:
            for ch in line:
                string_ += ch
            string_ += "\n"
        if return_string:
            return string_
        else:
            print(string_)

    def find_player_in_layout(self):
        player_list = ()
        place_in_queue = 0
        for y, line in enumerate(self.current_layout):
            for x, ch in enumerate(line):
                if ch == "G" or ch == "E":
                    place_in_queue += 1
                    type_ = ch
                    player_list.append((type_, x, y))


    def __str__(self):
        return self.print_layout(False, True)




path = r"C:\Users\Herman\Desktop\PROGRAMMERING\Projekt\Advent_of_code\adv15-short.txt"
b = Board(path)
print(b)
b.print_layout(1)
