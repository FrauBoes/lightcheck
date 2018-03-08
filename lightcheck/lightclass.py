# -*- coding: utf-8 -*-

"""Main module."""

import re
import lightcheck.utils as ut
import numpy as np

# class to represent object with attribute grid and methods to manipulate the lights on the grid
class LightCheck:
    
    def __init__(self, N):
        
        # create 2-dimensional numpy array with default value False
        self.grid = np.zeros((N,N),dtype=np.bool)
            
 
    # parse command and apply it to data structure
    def apply(self, cmd):
        
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        if pattern.match(cmd) is None:  # returns True if there is a match, otherwise None
            return
        else:
            instruction_parsed = ut.parseCommand(cmd)  # returns a list in the format [instruction, column_coordinates, row_coordinates]
        
        # set minimum and maximum coordinates for the instruction
        min_index_row = np.minimum(instruction_parsed[2][0],instruction_parsed[2][1])
        max_index_row = np.maximum(instruction_parsed[2][0],instruction_parsed[2][1])
        min_index_col = np.minimum(instruction_parsed[1][0],instruction_parsed[1][1])
        max_index_col = np.maximum(instruction_parsed[1][0],instruction_parsed[1][1])
        
        if instruction_parsed[0] == "turn on":
            self.grid[min_index_row:max_index_row+1,min_index_col:max_index_col+1] = True;  # numpy handles indexing out of range
        elif instruction_parsed[0] == "turn off":
            self.grid[min_index_row:max_index_row+1,min_index_col:max_index_col+1] = False;
        elif instruction_parsed[0] == "switch ":
            self.grid[min_index_row:max_index_row+1,min_index_col:max_index_col+1] = np.invert(self.grid[min_index_row:max_index_row+1,min_index_col:max_index_col+1]);
        
        return
    

    # count lights that are on
    def count(self):
        
        return np.sum(self.grid)  # compute the sum (only True values counted)
