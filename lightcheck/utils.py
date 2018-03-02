'''
Created on 1 Mar 2018

@author: thelma
'''

from urllib.request import urlopen

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

class LightChecker:
    
    lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)]
        # placeholder
 
    def apply(self, cmd):
        if cmd is 'turn on':
            pass
        elif cmd is 'turn off':
            pass
        elif cmd is 'switch':
            pass
        # parse command and apply it to data structure
        return None
      
    def count(self):
        return None
        # placeholder, return count
        # count lights that are on
