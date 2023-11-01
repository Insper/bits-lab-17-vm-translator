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
LCL = 1
ARG = 2
THIS = 3
THAT = 4
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
def test_pop_local():
    x = 4; y = 8; z = 13
    ram = {SP: 259, LCL: 32, 256: x, 257: y, 258: z}
    tst = {0: 257, 32:z, 34: y}
    assert vm_test(abs_path("test_assets/pop_local.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_pop_this():
    x = 4; y = 8; z = 13
    ram = {SP: 259, THIS: 1024, 256: x, 257: y, 258: z}
    tst = {0: 257, 1024:z, 1026: y}
    assert vm_test(abs_path("test_assets/pop_this.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_pop_that():
    x = 4; y = 8; z = 13
    ram = {SP: 259, THAT: 1024, 256: x, 257: y, 258: z}
    tst = {0: 257, 1024:z, 1026: y}
    assert vm_test(abs_path("test_assets/pop_that.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_pop_temp():
    x = 4; y = 8; z = 13
    ram = {SP: 259, 256: x, 257: y, 258: z}
    tst = {0: 257, TEMP[5]:z, TEMP[7]: y}
    assert vm_test(abs_path("test_assets/pop_temp.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_pop_pointer():
    x = 4; y = 8; z = 13
    ram = {SP: 259, 256: x, 257: y, 258: z}
    tst = {0: 257, THIS:z, THAT: y}
    assert vm_test(abs_path("test_assets/pop_pointer.vm"), ram, tst)
