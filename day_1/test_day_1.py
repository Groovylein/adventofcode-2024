import day_1


with open('./input.txt', 'r') as file:
    inp = file.read()

def test_input_two_lists():
    
    list_1, list_2 = day_1.transform(inp)
    
    assert isinstance(list_1, list)
    assert isinstance(list_2, list)w
    assert len(list_1) == 6
    assert len(list_2) == 6
