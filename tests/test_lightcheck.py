#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `lightcheck` package."""

import sys
import pytest
from click.testing import CliRunner
from lightcheck.utils import LightChecker
from lightcheck import utils as ut
from lightcheck import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
 
 
def test_command_line_interface():
    ifile = "./data/input_assign3.txt"
    N, instructions = ut.parseFile(ifile)
    assert N is not None
     
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    N, instructions = ut.parseFile(ifile)
    assert N is not None


def test_create_light():
    lights = LightChecker(0)
    assert lights is not None

def test_apply():
    lights = LightChecker(2)
    lights.apply('turn on 0,0 through 1,1')
    assert lights == [[True, True], [True, True]]
    lights.apply('turn off 0,0 through 1,1')
    assert lights == [[False, False], [False, False]]
    lights.apply('switch 0,0 through 1,1')
    assert lights == [[True, True], [True, True]]
    lights.apply('switch 0,0 through 2,2')
    assert lights == [[False, False], [False, False]]
    lights.apply('sitch 0,0 through 1,1')
    assert lights == [[False, False], [False, False]]
    lights.apply('tur on 0,0 through 1,1')
    assert lights == [[False, False], [False, False]]
    


    
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'lightcheck.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
