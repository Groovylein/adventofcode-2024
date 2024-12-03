
def split_input(inp):
    l_of_l = []
    tmp_list = inp.strip().split("\n")
    for elem in tmp_list:
        l_of_l.append(elem.split())
    print(l_of_l)
    return l_of_l


with open('input.txt', 'r') as file:
    inp = file.read()
# print(inp)
