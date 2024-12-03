import pytest

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

def test_get_safe_reports():
    list_of_lists = day_2.split_input(inp)
    res_list_of_lists = day_2.get_safe_reports(list_of_lists)

    print(res_list_of_lists)
    assert isinstance(res_list_of_lists, list)
    for elem in res_list_of_lists:
        assert isinstance(elem, list)
    assert len(res_list_of_lists) == 2
    assert res_list_of_lists[0] == [7, 6, 4, 2, 1]
    assert res_list_of_lists[1] == [1, 3, 6, 7, 9]

testdata_increasing = [
    ([7, 6, 4, 2, 1], False, False),
    ([1, 3, 6, 7, 9], True, False),
    ([1, 2, 3, 4, 5], True, False),
    ([7, 6, 4, 2, 1], True, True),
    ([1, 3, 6, 7, 9], False, True),
    ([1, 0, -2, -3, -5], True, True),
]
@pytest.mark.parametrize("input_list, result, decreasing", testdata_increasing)
def test_check_increasing(input_list, result, decreasing):
    ret_value = day_2.check_order(input_list, decreasing)

    assert ret_value == result
