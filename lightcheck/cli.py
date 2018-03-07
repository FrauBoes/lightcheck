# -*- coding: utf-8 -*-

"""Console script for lightcheck."""

import sys
import click
import lightcheck.lightclass as lc
import lightcheck.utils as ut


click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input):
    """Console script for lightcheck."""
    print("input", input)
    
    N, instructions = ut.parseFile(input)  # get size of grid and instructions
    
    lights = lc.LightCheck(N)  # create light grid
     
    for instruction in instructions:  # apply instructions
        lights.apply(instruction)
    
    print('# lights occupied: ', lights.count())  # print count of lights that are on
    return 0


if __name__ == "__main__":
    main()
