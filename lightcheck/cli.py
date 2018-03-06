# -*- coding: utf-8 -*-

"""Console script for lightcheck."""

import sys
import click
import lightcheck.utils as ut
import lightcheck.lightcheck as lc

click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for lightcheck."""
    print("input", input)
    
    N, instructions = ut.parseFile(input)
    
    lights = lc.LightCheck(N)
     
    for instruction in instructions:
        lights.grid.apply(instruction)
    
    #print('# lights occupied: ', lights.grid.count())
    return 0


if __name__ == "__main__":
    sys.exit(main())
