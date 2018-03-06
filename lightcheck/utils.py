'''
Created on 1 Mar 2018

@author: thelma
'''

from urllib.request import urlopen
import re

# parse input from url or local file
def parseFile(inp):
    
    # read from url
    if inp.startswith('http'):
        N, instructions = None, []
        f = urlopen(inp)
        
        with urlopen(inp) as f:
            N = int(f.readline())
            for line in f.readlines():
                # cast byte type to string and strip '\n' from each line
                instructions.append(line.decode('utf-8').rstrip('\n'))
        return N, instructions
        
    # read from disk    
    else:
        N, instructions = None, []
        
        with open(inp, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line.rstrip('\n'))  # strip '\n' from each line
        return N, instructions
    
    return


def parseCommand(cmd):
    instruction = re.findall("([a-zA-Z]+\s([a-zA-z]+)?)", cmd) [0][0]
    coordinates = re.findall("[+-]?\d+", cmd)
    column_coordinates = [int(coordinates[0]), int(coordinates[2])]
    row_coordinates = [int(coordinates[1]), int(coordinates[3])]
        
    return [instruction, column_coordinates, row_coordinates]