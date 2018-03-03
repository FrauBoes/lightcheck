'''
Created on 1 Mar 2018

@author: thelma
'''

from urllib.request import urlopen
import re

# parse input from url or local file
def parseFile(input):
    
    # read from url
    if input.startswith('http'):
        N, instructions = None, []
        f = urlopen(input)
        
        with urlopen(input) as f:
            N = int(f.readline())
            for line in f.readlines():
                # cast byte type to string and strip '\n' from each line
                instructions.append(line.decode('utf-8').rstrip('\n'))
        return N, instructions
        
    # read from disk    
    else:
        N, instructions = None, []
        
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line.rstrip('\n'))  # strip '\n' from each line
        return N, instructions
    
    return

def parseCommand(cmd):
        instruction = re.findall("([a-zA-Z]+\s([a-zA-z]+)?)", cmd) [0][0]
        coordinates = re.findall("[+-]?\d+", cmd)
        row_coordinates = [int(coordinates[0]), int(coordinates[2])]
        column_coordinates = [int(coordinates[1]), int(coordinates[3])]
        
        return [instruction, row_coordinates, column_coordinates]

class LightChecker:
    
    lights = None
    
    def __init__(self, N):
        
        # create 2-dimensional array with default value False
        self.lights = [[False]*N for _ in range(N)]

    #for instruction in instructions:
    #    lights.apply(instruction)
 
 
    def apply(self, cmd):
        
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        if pattern.match(cmd) is None:  # returns True if there is a match, otherwise None
            return
        else:
            instruction_parsed = parseCommand(cmd)  # [instruction, start_coordinates, end_coordinates]
        
        
        if cmd.startswith('turn on'):
            pass
        elif cmd.startswith('turn off'):
            pass
        elif cmd.startswith('switch'):
            pass
        # parse command and apply it to data structure
        return None
    
    
    
    
    
      
    def count(self):
        
        return None
        # placeholder, return count
        # count lights that are on
