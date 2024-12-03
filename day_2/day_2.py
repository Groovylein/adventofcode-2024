
def split_input(inp):
    l_of_l = []
    tmp_list = inp.strip().split("\n")
    for elem in tmp_list:
        tmp_list_2 = []
        for e in elem.split():
            tmp_list_2.append(int(e))
        l_of_l.append(tmp_list_2)
    return l_of_l

def get_safe_reports(l_of_l):
    safe_list = []
    for l in l_of_l:
        safe = False
        for i, elem in enumerate(l):
            if (i+1) <= (len(l)-1):
                diff = elem - l[i+1]
                if diff in range(-4, 0):
                    safe = check_order(l, decreasing=False)
                    if not safe:
                        safe = check_bad_level(l, decreasing=False)
                    break
                elif diff in range(1, 4):
                    safe = check_order(l, decreasing=True)
                    if not safe:
                        safe = check_bad_level(l, decreasing=True)
                    break
                else:
                    break
        if safe:
            safe_list.append(l)
    return safe_list

def check_bad_level(input_list, decreasing):
    safe = False
    for i in range(0, len(input_list)):
        tmp_list = input_list.copy()
        tmp_list.pop(i)
        safe = check_order(tmp_list, decreasing)
        if safe:
            return safe
    return safe

def check_order(input_list, decreasing):
    comp = True
    comp_list = sorted(input_list, reverse=decreasing)
    for i, elem in enumerate(input_list):
        if elem != comp_list[i]:
            comp = False
        else:
            if (i+1) <= (len(input_list)-1):
                diff = abs(elem - input_list[i+1])
                if diff > 3 or diff == 0:
                    comp = False
    return comp

with open('input.txt', 'r') as file:
    inp = file.read()
# print(inp)

list_of_lists = split_input(inp)
# print(list_of_lists)
safe_reports = get_safe_reports(list_of_lists)
# print(safe_reports)
c = [val for val in list_of_lists if val not in safe_reports]
print(c)
print(f"Part 2: {len(safe_reports)}")
