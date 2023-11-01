#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test, createDir
from VMTranslate import VMTranslate
import os.path
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
def test_push_constant():
    ram = {SP: 256,}
    tst = {SP: 258, 256:12, 257:143}
    assert vm_test(abs_path("test_assets/push_constant.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_push_local():
    x = 4; y = 8; z = 13
    ram = {SP: 256, LCL: 32, 32: x, 33: y, 34: z}
    tst = {SP: 258, 256:x, 257: z}
    assert vm_test(abs_path("test_assets/push_local.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_push_argument():
    x = 4; y = 8; z = 13
    ram = {SP: 256, ARG: 32, 32: x, 33: y, 34: z}
    tst = {SP: 258, 256:x, 257: z}
    assert vm_test(abs_path("test_assets/push_argument.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_push_this():
    x = 4; y = 8; z = 13
    ram = {SP: 256, THIS: 32, 32: x, 33: y, 34: z}
    tst = {SP: 258, 256:x, 257: z}
    assert vm_test(abs_path("test_assets/push_this.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_push_that():
    x = 4; y = 8; z = 13
    ram = {SP: 256, THAT: 32, 32: x, 33: y, 34: z}
    tst = {SP: 258, 256:x, 257: z}
    assert vm_test(abs_path("test_assets/push_that.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_push_temp():
    x = 4; y = 8; z = 13
    ram = {SP: 256, TEMP[5]:x, TEMP[6]: y, TEMP[7]: z}
    tst = {SP: 258, 256:x, 257: z}
    assert vm_test(abs_path("test_assets/push_temp.vm"), ram, tst)

@pytest.mark.telemetry_files(source("Code.py"))
def test_push_pointer():
    x = 4; y = 8; z = 13
    ram = {SP: 256, THIS:x, THAT: y}
    tst = {SP: 258, 256:x, 257: y}
    assert vm_test(abs_path("test_assets/push_pointer.vm"), ram, tst)
