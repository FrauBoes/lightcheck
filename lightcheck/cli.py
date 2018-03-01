# -*- coding: utf-8 -*-

"""Console script for lightcheck."""

import click


@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for lightcheck."""
    print("input", input)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
