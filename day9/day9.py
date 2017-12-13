import sys
import re

ARGUMETNS = sys.argv
if len(ARGUMETNS) != 2:
    sys.exit("Usage: one argument needed, the name of the input file")

def normal_solution(line):
    result = 0
    depth = 0
    in_garbage = False
    idx = 0
    while idx < len(line):
        c = line[idx]
        if c == '!':
            idx += 2
            continue
        if not in_garbage:
            if c == '<':
                in_garbage = True
            elif c == '{':
                depth += 1
                # result += depth
            elif c == '}':
                depth -= 1
        else:
            if c == '>':
                in_garbage = False
            else:
                result += 1
        idx += 1
    print result


INPUT_FILE_NAME = sys.argv[1]
with open(INPUT_FILE_NAME, "r") as input_file:
    result = 0
    for input_line in input_file:
        input_line = input_line[:-1]
        normal_solution(input_line.strip(','))
    print result

