# -*- coding: utf-8 -*-

"""Console script for lightcheck."""

import click
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for lightcheck."""
    print("input", input)
    
    N, instructions = parseFile(input)
    
    lightChecker = LightChecker(N)
    
    for instruction in instructions:
        lightChecker.apply(instruction)
        
    print('# lights occupied: ', lightChecker.countOccupied())
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
