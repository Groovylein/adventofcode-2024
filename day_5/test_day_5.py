import pytest
import day_5

with open('test_input_1.txt', 'r') as file:
    inp_1 = file.read()
with open('test_input_2.txt', 'r') as file:
    inp_2 = file.read()

def test_create_order_tuple():
    ret_list = day_5.create_order_tuple(inp_1)

    assert isinstance(ret_list, list)
    for elem in ret_list:
        assert isinstance(elem, tuple)


testdata = [
    (47, [53, 13, 61, 29]),
    (97, [13,61,47,29,53,75]),
    (75, [29,53,47,61,13]),
]
@pytest.mark.parametrize("search_num, expected", testdata)
def test_search_for_tuple(search_num, expected):
    list_of_tuple = day_5.create_order_tuple(inp_1)
    ret_list = day_5.search_for_tuple(search_num, list_of_tuple)

    assert isinstance(ret_list, list)
    for elem in ret_list:
        assert isinstance(elem, int)
    assert ret_list == expected
