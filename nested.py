#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module docstring: One line description of what your program does.
"""
# __author__= "LEllingwood"

import sys

def prep_file(filename):
    """Opens file, reads it, splits the text on a new line"""
    with open(filename) as f:
        lines = f.read().split('\n')
    return lines        
    
def write_output():   
    with open('output.txt', 'w') as o:
        for line in lines:
            result = check_line(lines)
            print(result)
            o.write(result)


def check_line(line):
    open_char = ["(", "[", "{", "<", "(*"]
    closing_char = [")", "]", "}", ">", "*)"]
    stack = []
    count = 0
#    counts how far you are in theline before the unnesting happens.
    print line
    while line:
        token = line[0]
        if line.startswith('(*'):
            token = '(*'
        elif line.startswith('*)'):
            token = '*)'
        count = count + 1

        if token in open_char:
            stack.append(token)

        elif token in closing_char:
            closer_index = closing_char.index(token)
            # closer index is the index of the particular token.
            expected_opener = open_char[closer_index]
            # looks for the index of the corresponding opener.
            if expected_opener != stack.pop():
                # if the expected token doesn't match the last item in the stack, return no.
                return 'no' + str(count)   
        line = line[len(token):]
        print line
    if len(stack) > 0: 
        return 'no' + str(count+1)
    return "Yes"

def main(args):
    if len(sys.argv) != 2:
        sys.exit(1)
    lines = prep_file(sys.argv[1])   
    for line in lines: 
        print check_line(line)

if __name__ == '__main__':
    main(sys.argv)
