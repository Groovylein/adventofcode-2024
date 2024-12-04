import day_3

with open('test_input.txt', 'r') as file:
    t_inp = file.read()
# print(inp)

def test_extract_instructions():
    list_instructions = day_3.extract_instructions(t_inp)

    assert isinstance(list_instructions, list)
    assert len(list_instructions) == 4
    assert list_instructions[0] == "mul(2,4)"

def test_caculate_correctly():
    i = day_3.caculate_correctly(t_inp)

    assert isinstance(i, int)
    assert i == 161

def test_get_first_occurence_of_dont():
    pass

def test_extract_instructions_enhanced():
    list_instructions = day_3.extract_instructions_enhanced(t_inp)

    assert isinstance(list_instructions, list)
    assert len(list_instructions) == 2
    assert list_instructions[0] == "mul(2,4)"
    assert list_instructions[0] == "mul(8,5)"

def test_caculate_correctly_enhanced():
    i = day_3.caculate_correctly_enhanced(t_inp)

    assert isinstance(i, int)
    assert i == 48
