import sys

ARGUMETNS = sys.argv
if len(ARGUMETNS) != 2:
    sys.exit("Usage: one argument needed, the name of the input file")

def solve_day_1(line, step):
    result = 0
    line_length = len(line)
    for idx, dig in enumerate(line):
        if dig == line[(idx + step) % line_length]:
            result += int(dig)
    return result


INPUT_FILE_NAME = sys.argv[1]
with open(INPUT_FILE_NAME, "r") as input_file:
    for input_line in input_file:
        if input_line[0] == '-':
            print input_line
            continue
        processed_line = input_line[:-1]
        print solve_day_1(processed_line, len(processed_line) / 2)
