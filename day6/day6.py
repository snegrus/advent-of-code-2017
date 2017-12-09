import sys
import numpy
import hashlib

ARGUMETNS = sys.argv
if len(ARGUMETNS) != 2:
    sys.exit("Usage: one argument needed, the name of the input file")

def line_to_number(line):
    return list(map(int, line.split()))

def get_hash_value(config):
    return hashlib.sha1(str(config)).hexdigest()

def execute_cycle(banks, pos):
    value = banks[pos]
    banks[pos] = 0
    pos += 1
    pos %= len(banks)
    sure_add = value / len(banks)
    remainder = value % len(banks)
    banks = [x + sure_add for x in banks]
    while remainder:
        banks[pos] += 1
        pos += 1
        pos %= len(banks)
        remainder -= 1
    return banks

def get_max_pos(banks):
    return banks.index(max(banks))

def solve_p1(banks):
    # seen_configs = set()
    seen_configs = {}
    while True:
        hash_value = get_hash_value(banks)
        if hash_value in seen_configs:
            return len(seen_configs) - seen_configs[hash_value]
        seen_configs[hash_value] = len(seen_configs)
        pos = get_max_pos(banks)
        banks = execute_cycle(banks, pos)


INPUT_FILE_NAME = sys.argv[1]
with open(INPUT_FILE_NAME, "r") as input_file:
    for input_line in input_file:
        print solve_p1(line_to_number(input_line))

