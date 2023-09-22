#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

import logging
from pprint import pprint
import subprocess
from hydra import compose, initialize

# testing configurations
with initialize(version_base=None, config_path="../config"):
    cfg = compose(config_name="test")

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# logging
logging.basicConfig(
    format=FORMAT,
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)
logger.info("Starting test_me.py")


def run_command(command):
    """Run a command with poetry."""
    command_lst = ['poetry', 'run', *command.split()]
    return subprocess.run(command_lst, capture_output=True, text=True)


def test_commands():
    """Run pytest for testing your fixed code."""
    if not cfg.check_mode:
        return
    for name, command in cfg.tests.items():
        if not cfg.checks.get(name):
            continue
        result = run_command(command=command)
        code = result.returncode
        if code != 0:
            logger.error(result.stdout)
            logger.error(result.stderr)
            raise AssertionError(f"'{name}' failed, run 'poetry run {command}' in your terminal or check the log (run 'make test-report' in terminal) to check details.")
