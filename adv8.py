path = r"C:\Users\Herman\test_git\adv8-short.txt"


with open(path) as f:
    txt = f.read().splitlines()

ls = txt[0].split(" ")

nodestack = []
datastack = []
data = []
#node data
#2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
data_count = 0
while ls:
    item = ls.pop(0)
    if nodestack == []:
        nodestack.append(item)
    elif len(datastack) < len(nodestack):
        datastack.append(item)
    if data_count > 0:
        data.append(item)
        data_count -= 1
    if len(datastack) == len(nodestack):
        if nodestack[-1] == 0:
            data_count = datastack[-1]
