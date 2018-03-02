'''
Created on 1 Mar 2018

@author: thelma
'''

from urllib.request import urlopen

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