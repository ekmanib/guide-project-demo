#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

from src.doc_me import add_document

import subprocess

COMMANDS = {
    'interrogate': ["interrogate"],
    'sourcery': ["sourcery", "review", "src"],
    ''
}

def test_after_fixing_problems():
    assert add_document()


def test_cli_command():
    # cli = "sourcery review src"
    cli = "interrogate"
    result = subprocess.run([cli], capture_output=True, text=True)
    failure_message = f"CLI command failed with error code {result.returncode} and error message: {result.stderr}"
    assert result.returncode == 0, failure_message
