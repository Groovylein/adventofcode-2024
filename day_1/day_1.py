def transform(inp):
    l_1 = []
    l_2 = []
    l_inp = inp.strip().split()
    for i in range(0, (len(l_inp)-1), 2):
        l_1.append(int(l_inp[i]))
        l_2.append(int(l_inp[i + 1]))
    return l_1, l_2

def distance_of_elem(list_1, list_2):
    ret_list = []
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)
    for i in range(0, len(list_1)):
        ret_list.append(abs(sorted_list_1[i]-sorted_list_2[i]))
    return ret_list

with open('input.txt', 'r') as file:
    inp = file.read()
list_1, list_2 = transform(inp)
dist_list = distance_of_elem(list_1, list_2)
sum = 0
for elem in dist_list:
    sum += elem
print(sum)
