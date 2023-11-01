#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test, createDir
from VMTranslate import VMTranslate
from bits import vm_test
import os.path
import pytest
import yaml

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)


SP = 0
STACK = 256
TEMP = {0: 5, 1: 6, 2: 7, 3:8, 4:9, 5:10, 6:11, 7:12}
TRUE = -1
FALSE = False

def abs_path(file):
    dir_test = os.path.dirname(__file__)
    return os.path.join(dir_test, file)

def vm_to_nasm(vm, nasm):
    createDir(nasm)
    fNasm = open(nasm, "w")
    v = VMTranslate(vm, fNasm)
    v.run()

def vm_test(vm, ram, test, time=10000):
    nasm = os.path.join("nasm", vm + ".nasm")
    vm_to_nasm(vm, nasm)
    return nasm_test(nasm, ram, test, time)

@pytest.mark.telemetry_files(source("Code.py"))
def test_goto_false():
    x = 4; y = 5
    ram = {0: 256, TEMP[0]: x, TEMP[1]: y}
    tst = {0: 256, TEMP[2]: 1}
    assert vm_test(abs_path("test_assets/ifgoto.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_goto_true():
    x = 4; y = 5
    ram = {0: 256, TEMP[0]: x, TEMP[1]: x}
    tst = {0: 256, TEMP[2]: 2}
    assert vm_test(abs_path("test_assets/ifgoto.vm"), ram, tst)
