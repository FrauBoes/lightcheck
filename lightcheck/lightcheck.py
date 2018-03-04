# -*- coding: utf-8 -*-

"""Main module."""

import re
from lightcheck.utils import *

class LightCheck:
    
    lights = None
    
    
    def __init__(self, N):
        
        # create 2-dimensional array with default value False
        self.lights = [[False]*N for _ in range(N)]

    # def __getitem__(self, key)
    
    # def __setitem__(self, key)
    
    # def __iter__(self)
    

 
    # parse command and apply it to data structure
    def apply(self, cmd):
        
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        if pattern.match(cmd) is None:  # returns True if there is a match, otherwise None
            return
        else:
            instruction_parsed = parseCommand(cmd)  # [instruction, column_coordinates, row_coordinates]
        
            if instruction_parsed[0] =='turn on':
                new_value = 'True'
                for row in range(instruction_parsed[1][0], instruction_parsed[1][1]+1):
                    for column in range(instruction_parsed[2][0], instruction_parsed[2][1]+1):
                        self[row][column] = new_value
            
            elif instruction_parsed[0] =='turn off':
                new_value = 'False'
                for row in range(instruction_parsed[1][0], instruction_parsed[1][1]+1):
                    for column in range(instruction_parsed[2][0], instruction_parsed[2][1]+1):
                        self[row][column] = new_value
                        
            elif instruction_parsed[0] =='switch ':
                for row in range(instruction_parsed[1][0], instruction_parsed[1][1]+1):
                    for column in range(instruction_parsed[2][0], instruction_parsed[2][1]+1):
                        self[row][column] = not self[row][column]
        
        return None
    
    
    
    
    
      
    def count(self):
        
        return None
        # placeholder, return count
        # count lights that are on
