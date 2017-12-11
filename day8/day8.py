import sys
import numpy
import hashlib

ARGUMETNS = sys.argv
if len(ARGUMETNS) != 2:
    sys.exit("Usage: one argument needed, the name of the input file")

registers = {}


def test_condition(reg, operator, val):
    if operator == "<":
        return reg < val
    if operator == "<=":
        return reg <= val
    if operator == "==":
        return reg == val
    if operator == "!=":
        return reg != val
    if operator == ">":
        return reg > val
    if operator == ">=":
        return reg >= val

def add_register(reg):
    if reg not in registers:
        registers[reg] = 0


def execute_op(register, operation, op_value):
    reg_value = registers[register]
    if operation == "inc":
        reg_value += op_value
    else:
        reg_value -= op_value
    registers[register] = reg_value

#  0  1  2  3 4 5 6
#  b inc 5 if a > 1
def process_line(line_tokens):
    print line_tokens
    register = line_tokens[0]
    operation = line_tokens[1]
    op_value = int(line_tokens[2])
    cond_register = line_tokens[4]
    cond_op = line_tokens[5]
    cond_val = int(line_tokens[6])

    add_register(register)
    add_register(cond_register)

    if test_condition(registers[cond_register], cond_op, cond_val):
        execute_op(register, operation, op_value)

INPUT_FILE_NAME = sys.argv[1]
with open(INPUT_FILE_NAME, "r") as input_file:
    result = 0
    for input_line in input_file:
        process_line(input_line.split())
        result = max(result, max(registers.itervalues()))
    print result

