import day_1


with open('test_input.txt', 'r') as file:
    inp = file.read()

def test_input_two_lists():
    
    list_1, list_2 = day_1.transform(inp)
    
    assert isinstance(list_1, list)
    assert isinstance(list_2, list)
    assert len(list_1) == 6
    assert len(list_2) == 6
    for elem in list_1:
        assert isinstance(elem, int)
    for elem in list_2:
        assert isinstance(elem, int)

def test_distance_of_elements():
    list_1, list_2 = day_1.transform(inp)
    res_list = day_1.distance_of_elem(list_1, list_2)

    assert isinstance(res_list, list)
    assert len(res_list) == 6
    assert res_list == [2 , 1 , 0 , 1 , 2 , 5]
