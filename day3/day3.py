import sys
import numpy

ARGUMETNS = sys.argv
if len(ARGUMETNS) != 2:
    sys.exit("Usage: one argument needed, the name of the input file")

def line_to_number(line):
    return list(map(int, line.split()))[0]

def get_distance_to_center(target):
    if target == 1:
        return 0
    aux_target = target
    target -= 1
    dist_center = 1
    next_square = 8
    lg_edge = 3
    while next_square < target:
        target -= next_square
        next_square += 8
        lg_edge += 2
        dist_center += 1
    lastnr = lg_edge * lg_edge
    middles = [lastnr - dist_center]
    lastnr = middles[0]
    for i in range(3):
        lastnr -= dist_center * 2
        middles.append(lastnr)
    return min(list(map(lambda x: abs(x - aux_target), middles))) + dist_center


def print_table(table):
    for line in table:
        print line

def get_sum_around(table, x, y):
    ans = 0
    for idx in range(x - 1, x + 2):
        for jdx in range(y - 1, y + 2):
            ans += table[idx][jdx]
    return ans

def get_value_bigger(target):
    n = 11
    starty = startx = n / 2
    table = numpy.zeros((n, n), dtype=numpy.int)
    table[startx][starty] = 1
    current_value = 1
    lg_edge = 3

    while current_value <= target:
        starty += 1
        current_value = table[startx][starty] = get_sum_around(table, startx, starty)
        if current_value > target:
            return current_value

        for i in range(lg_edge - 2):
            startx -= 1
            current_value = table[startx][starty] = get_sum_around(
                table, startx, starty)
            if current_value > target:
                return current_value

        for i in range(lg_edge - 1):
            starty -= 1
            current_value = table[startx][starty] = get_sum_around(
                table, startx, starty)
            if current_value > target:
                return current_value

        for i in range(lg_edge - 1):
            startx += 1
            current_value = table[startx][starty] = get_sum_around(
                table, startx, starty)
            if current_value > target:
                return current_value

        for i in range(lg_edge - 1):
            starty += 1
            current_value = table[startx][starty] = get_sum_around(
                table, startx, starty)
            if current_value > target:
                return current_value

        lg_edge += 2


INPUT_FILE_NAME = sys.argv[1]
with open(INPUT_FILE_NAME, "r") as input_file:
    for input_line in input_file:
        if input_line[0] == '-':
            exit()
        input_number = line_to_number(input_line)
        print get_value_bigger(input_number)
