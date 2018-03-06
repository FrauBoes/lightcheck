# -*- coding: utf-8 -*-

"""Main module."""

import re
import lightcheck.utils as ut

class LightCheck:
    
    grid = None
    
    
    def __init__(self, N):
        
        # create 2-dimensional array with default value False
        self.grid = [[False]*N for _ in range(N)]
            

 
    # parse command and apply it to data structure
    def apply(self, cmd):
        
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        if pattern.match(cmd) is None:  # returns True if there is a match, otherwise None
            return
        else:
            instruction_parsed = ut.parseCommand(cmd)  # [instruction, column_coordinates, row_coordinates]
        
            if instruction_parsed[0] =='turn on':
                for row in range(instruction_parsed[1][0], instruction_parsed[1][1]+1):
                    for column in range(instruction_parsed[2][0], instruction_parsed[2][1]+1):
                        try:
                            self.grid[row][column] = True
                        except IndexError:
                            continue
                        
            elif instruction_parsed[0] =='turn off':
                for row in range(instruction_parsed[1][0], instruction_parsed[1][1]+1):
                    for column in range(instruction_parsed[2][0], instruction_parsed[2][1]+1):
                        try:
                            self.grid[row][column] = False
                        except IndexError:
                            continue            
            elif instruction_parsed[0] =='switch ':
                for row in range(instruction_parsed[1][0], instruction_parsed[1][1]+1):
                    for column in range(instruction_parsed[2][0], instruction_parsed[2][1]+1):
                        try:
                            self.grid[row][column] = not self.grid[row][column]
                        except IndexError:
                            continue
            
        return None
    
    
    
    
    
      
    def count(self):
        
        return None
        # placeholder, return count
        # count lights that are on
