# -*- coding: utf-8 -*-

"""Console script for lightcheck."""

import sys
import click
click.disable_unicode_literals_warning = True

from utils import parseFile, LightChecker

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for lightcheck."""
    print("input", input)
    
    N, instructions = parseFile(input)
    
    lights = LightChecker(N)
#     
#     for instruction in instructions:
#         lights.apply(instruction)
#         
#     print('# lights occupied: ', lights.count())
#     return 0


if __name__ == "__main__":
    sys.exit(main())
