import sys

ARGUMETNS = sys.argv
if len(ARGUMETNS) != 2:
    sys.exit("Usage: one argument needed, the name of the input file")

def line_to_list_int(line):
    line = line.split()
    return list(map(int, line))

def get_max_min(line):
    return max(line), min(line)

def get_r_division(line):
    for idx, value in enumerate(line):
        for idy in range(0, idx):
            if value % line[idy] == 0:
                return value / line[idy]
            if line[idy] % value == 0:
                return line[idy] / value


INPUT_FILE_NAME = sys.argv[1]
with open(INPUT_FILE_NAME, "r") as input_file:
    answer = 0
    for input_line in input_file:
        if input_line[0] == '-':
            break
        list_as_ints = line_to_list_int(input_line)
        line_ans = get_r_division(list_as_ints)
        answer += line_ans
    print answer
