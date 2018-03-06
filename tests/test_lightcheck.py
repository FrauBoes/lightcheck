#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for 'lightcheck' package."""

import sys
import pytest
from click.testing import CliRunner
from lightcheck import lightcheck as lc
from lightcheck import utils as ut
from lightcheck import cli

 
def test_read_file():
    """
    Assert that input is parsed
    
    1. Input from local file is parsed.
    2. Input from network address is parsed.
    3. All lines are parsed correctly from test file.
    """
    ifile = "./data/input_assign3.txt"
    N = ut.parseFile(ifile)
    assert N is not None
     
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt"
    N = ut.parseFile(ifile)
    assert N is not None
    
    ifile = "./data/test_data.txt"
    N, instructions = ut.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9', 'turn off 0,0 through 9,9', 'switch 0,0 through 9,9', 'turn off 0,0 through 9,9', 'turn on 2,2 through 7,7']


def test_create_light():
    """
    Assert that LightCheck instance is invoked.
    """
    lights = lc.LightCheck(0)
    assert lights is not None


def test_apply():
    """
    Assert that instructions are applied correctly.
    
    1. Operation for instruction 'turn on' is working correctly.
    2. Operation for instruction 'turn off' is working correctly.
    3. Operation for instruction 'switch ' is working correctly.
    4. + 5. No operations are executed for unknown instruction.
    6. Instruction that exceeds the grid's boundaries is only executed within the area of the grid.
    
    """
    lights = lc.LightCheck(2)
    lights.apply('turn on 0,0 through 1,1')
    assert lights.grid == [[True, True], [True, True]]
    lights.apply('turn off 0,0 through 1,1')
    assert lights.grid == [[False, False], [False, False]]
    lights.apply('switch 0,0 through 1,1')
    assert lights.grid == [[True, True], [True, True]]
    lights.apply('sitch 0,0 through 1,1')
    assert lights.grid == [[True, True], [True, True]]
    lights.apply('tur on 0,0 through 1,1')
    assert lights.grid == [[True, True], [True, True]]
    lights.apply('turn off 0,0 through 2,2')
    assert lights.grid == [[False, False], [False, False]]
    
    
def test_parse_command():
    """
    Assert that instructions are parsed correctly.
    """
    assert ut.parseCommand('turn off 660,55 through 986,197') == ['turn off', [660, 986], [55, 197]]
    assert ut.parseCommand('turn on 661,55 through 985,197') == ['turn on', [661, 985], [55, 197]]   
    assert ut.parseCommand('switch 322,558 through 977,958') == ['switch ', [322, 977], [558, 958]]
    
    
def test_count():
    """
    Assert that lights are counted correctly.
    """
    test_list = lc.LightCheck(3)
    assert test_list.count() == 0
    
# """Test the CLI."""
# runner = CliRunner()
# result = runner.invoke(cli.main)
# assert result.exit_code == 0
# assert 'lightcheck.cli.main' in result.output
# help_result = runner.invoke(cli.main, ['--help'])
# assert help_result.exit_code == 0
# assert '--help  Show this message and exit.' in help_result.output
