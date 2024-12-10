with open('input_1.txt', 'r') as file:
    inp_1 = file.read()
# print(inp_1)
with open('input_2.txt', 'r') as file:
    inp_2 = file.read()
# print(inp_2)

def create_order_tuple(order_list):
    list_of_tuple = []
    # print(repr(order_list))
    for line in order_list.strip().split("\n"):
        elem_of_line = line.strip().split("|")
        # print(elem_of_line)
        list_of_tuple.append((int(elem_of_line[0]),int(elem_of_line[1])))

    return list_of_tuple

def search_for_tuple(num, list_of_tuple):
    found_list = []
    for elem in list_of_tuple:
        if elem[0] == num:
            found_list.append(elem[1])
    return found_list

def check_order(order_list, list_to_be_checked):
    r_list = []
    l_of_t = create_order_tuple(order_list)
    for row in list_to_be_checked:
        for i, elem in enumerate(row):
            tmp_l = row.copy()
            del tmp_l[:i]
            # print(tmp_l)
            for s_elem in tmp_l:
                s_list = search_for_tuple(elem, l_of_t)
                # print(f"search list for {elem}: {s_list}")
                # print(f"Let's search for {s_elem}")
                if s_elem not in s_list:
                    s_r_list = search_for_tuple(s_elem, l_of_t)
                    if elem in s_r_list:
                        # print(f"this row is wrong: {row}")
                        if row not in r_list:
                            r_list.append(row)
    return r_list

def transform_list(list_to_transform):
    r_l = []
    for elem in list_to_transform.strip().split():
        tmp_l = [int(x) for x in elem.split(",")]
        r_l.append(tmp_l)
    return r_l

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

l_t_b_c = transform_list(inp_2)
print(l_t_b_c)
wrong_row_list = check_order(inp_1, l_t_b_c)
print(wrong_row_list)
sum_day_1 = 0
for e in l_t_b_c:
    if e not in wrong_row_list:
        sum_day_1 += findMiddle(e)
print(sum_day_1)

