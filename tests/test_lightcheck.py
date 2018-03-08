#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for 'lightcheck' package."""

import sys
import pytest
import numpy as np
from click.testing import CliRunner
import lightcheck.lightclass as lc
import lightcheck.utils as ut


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
    lights = lc.LightCheck(3)
    test_grid = np.array([[False, False, False], [False, False, False], [False, False, False]])
    np.testing.assert_array_equal(lights.grid, test_grid)


def test_apply():
    """
    Assert that instructions are applied correctly.
    
    1. Operation for instruction 'turn on' is working correctly.
    2. Operation for instruction 'turn off' is working correctly.
    3. Operation for instruction 'switch ' is working correctly.
    4. No operations are executed for unknown instruction.
    5. Instruction that exceeds the grid's boundaries is only executed within the area of the grid.
    6. Instruction can refer to coordinates from lower to higher or higher to lower.
    
    """
    lights = lc.LightCheck(2)
    
    test_grid = np.array([[True, True], [True, True]])
    lights.apply('turn on 0,0 through 1,1')
    np.testing.assert_array_equal(lights.grid, test_grid)
    
    test_grid = np.array([[False, False], [False, False]])
    lights.apply('turn off 0,0 through 1,1')
    np.testing.assert_array_equal(lights.grid, test_grid)
    
    test_grid = np.array([[True, True], [True, True]])
    lights.apply('switch 0,0 through 1,1')
    np.testing.assert_array_equal(lights.grid, test_grid)
    
    lights.apply('switc 0,0 through 1,1')
    np.testing.assert_array_equal(lights.grid, test_grid)
    
    test_grid = np.array([[True, False], [True, True]])
    lights.apply('switch 1,0 through 2,0')
    np.testing.assert_array_equal(lights.grid, test_grid)
    
    test_grid = np.array([[False, True], [True, True]])
    lights.apply('switch 1,0 through 0,0')
    np.testing.assert_array_equal(lights.grid, test_grid)
        
    
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
    
