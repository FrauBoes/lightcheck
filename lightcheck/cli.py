# -*- coding: utf-8 -*-

"""Console script for lightcheck."""

import sys
import click
from lightcheck import lightcheck as lc
from lightcheck import utils as ut

click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(inp=None):
    """Console script for lightcheck."""
    print("input", inp)
    
    N, instructions = ut.parseFile(inp)  # get size of grid and instructions
    
    lights = lc.LightCheck(N)  # create light grid
     
    for instruction in instructions:  # apply instructions
        lights.grid.apply(instruction)
    
    print('# lights occupied: ', lights.grid.count())  # print count of lights that are on
    return 0


if __name__ == "__main__":
    sys.exit(main())
