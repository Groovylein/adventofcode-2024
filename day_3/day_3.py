import re

def mul(x: int, y: int) -> int:
    return x*y

def extract_instructions(instr):
    return re.findall(r"mul\(\d+,\d+\)", instr)

def caculate_correctly(instr):
    sum = 0
    l_of_operations = extract_instructions(instr)
    for elem in l_of_operations:
        s_result = re.search('mul\((\d+),(\d+)\)', elem)
        sum += mul(int(s_result.group(1)), int(s_result.group(2)))
    return sum

with open('input.txt', 'r') as file:
    inp = file.read()
# print(inp)

print(f"Part 1: {caculate_correctly(inp)}")
