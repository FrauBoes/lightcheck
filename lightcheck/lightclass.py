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
                    for light in range(instruction_parsed[2][0], instruction_parsed[2][1]+1):
                        try:
                            self.grid[row][light] = True
                        except IndexError:
                            continue
                        
            elif instruction_parsed[0] =='turn off':
                for row in range(instruction_parsed[1][0], instruction_parsed[1][1]+1):
                    for light in range(instruction_parsed[2][0], instruction_parsed[2][1]+1):
                        try:
                            self.grid[row][light] = False
                        except IndexError:
                            continue            
            elif instruction_parsed[0] =='switch ':
                for row in range(instruction_parsed[1][0], instruction_parsed[1][1]+1):
                    for light in range(instruction_parsed[2][0], instruction_parsed[2][1]+1):
                        try:
                            self.grid[row][light] = not self.grid[row][light]
                        except IndexError:
                            continue
            
        return None
    
    
    # count lights that are on
    def count(self):
        
        count = 0
        for row in self.grid:
            count += sum(row)  # compute the sum (only True values counted)
            
        return count  
