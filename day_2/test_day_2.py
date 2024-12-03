import day_2


with open('test_input.txt', 'r') as file:
    inp = file.read()

def test_input_split():
    list_of_lists = day_2.split_input(inp)

    assert isinstance(list_of_lists, list)
    for elem in list_of_lists:
        assert isinstance(elem, list)
        for sub_elem in elem:
            assert isinstance(sub_elem, int)

