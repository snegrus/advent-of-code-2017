import sys
import numpy

ARGUMETNS = sys.argv
if len(ARGUMETNS) != 2:
    sys.exit("Usage: one argument needed, the name of the input file")

def is_passphrase_valid(passphrase):
    words = passphrase.split()
    words_set = set(words)
    return len(words) == len(words_set)

def is_passphrase_valid_anagrams(passphrase):
    words = map(lambda x: ''.join(sorted(x)), passphrase.split())
    words_set = set(words)
    return len(words) == len(words_set)

INPUT_FILE_NAME = sys.argv[1]
with open(INPUT_FILE_NAME, "r") as input_file:
    answer = 0
    for input_line in input_file:
        if input_line[0] == '-':
            exit()
        answer += is_passphrase_valid_anagrams(input_line)
    print answer
