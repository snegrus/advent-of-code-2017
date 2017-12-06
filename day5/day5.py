import sys
import numpy

ARGUMETNS = sys.argv
if len(ARGUMETNS) != 2:
    sys.exit("Usage: one argument needed, the name of the input file")

def solve_p1(instructions_list):
    idx = 0
    result = 0
    while idx >= 0 and idx < len(instructions_list):
        result += 1
        prev_idx = idx
        idx += instructions_list[idx]
        instructions_list[prev_idx] += 1
    return result


def solve_p2(instructions_list):
    idx = 0
    result = 0
    while idx >= 0 and idx < len(instructions_list):
        result += 1
        prev_idx = idx
        idx += instructions_list[idx]
        if instructions_list[prev_idx] >= 3:
            instructions_list[prev_idx] -= 1
        else:
            instructions_list[prev_idx] += 1
    return result


INPUT_FILE_NAME = sys.argv[1]
with open(INPUT_FILE_NAME, "r") as input_file:
    instructions_list = []
    for input_line in input_file:
        instructions_list.append(int(input_line))
    print solve_p2(instructions_list)
