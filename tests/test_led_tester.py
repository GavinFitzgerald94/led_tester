#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import sys
sys.path.append('.')

import pytest
import re

from click.testing import CliRunner

from led_tester import led_tester
from led_tester import cli
from led_tester import utils
from led_tester import *

@pytest.fixture

def test_command_line_interface():
    """Test the CLI."""
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None

def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7\n']
    
def test_instructions_parsing_turn_on():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    on_pat = re.compile(".*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    on = on_pat.match(instructions[0])
    assert on.group(1) == "turn on"
    assert on.group(2) == "0"
    assert on.group(3) == "0"
    assert on.group(4) == "9"
    assert on.group(5) == "9"
    
def test_instructions_parsing_turn_off():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    off_pat = re.compile(".*(turn off)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    off = off_pat.match(instructions[1])
    assert off.group(1) == "turn off"
    assert off.group(2) == "0"
    assert off.group(3) == "0"
    assert off.group(4) == "9"
    assert off.group(5) == "9"

def test_instructions_parsing_switch():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    switch_pat = re.compile(".*(switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    switch = switch_pat.match(instructions[2])
    assert switch.group(1) == "switch"
    assert switch.group(2) == "0"
    assert switch.group(3) == "0"
    assert switch.group(4) == "9"
    assert switch.group(5) == "9"
    
def test_instructions_parsing_turn_on_22_77():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    on_pat = re.compile(".*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    on = on_pat.match(instructions[4])
    assert on.group(1) == "turn on"
    assert on.group(2) == "2"
    assert on.group(3) == "2"
    assert on.group(4) == "7"
    assert on.group(5) == "7"

def test_count():
    ledTester = led_tester.LEDTester(10)
    ledTester.apply("turn on 0,0 through 9,9")
    assert ledTester.count() == 100
    
def test_commands_outside_grid_space():
    ledTester = led_tester.LEDTester(10)
    ledTester.apply("turn on 0,0 through 20,20")
    assert ledTester.count() == 100