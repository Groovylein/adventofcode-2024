
def transform(inp):
    l_1 = []
    l_2 = []
    l_inp = inp.strip().split()
    for i in range(0, (len(l_inp)-1), 2):
        l_1.append(l_inp[i])
        l_2.append(l_inp[i + 1])
    return l_1, l_2


with open('./input.txt', 'r') as file:
    inp = file.read()
print(inp)
