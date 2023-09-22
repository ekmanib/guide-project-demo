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


def _run_command(command: str, check_all: bool = True) -> None:
    """Run a command with poetry."""
    if not cfg.check_mode:
        return
    if not cfg.check_all or not check_all:
        command = command.replace('src', 'src/doc_me.py')
    commands = command.split()
    command_lst = ['poetry', 'run', *commands]
    result = subprocess.run(command_lst, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error(result.stdout)
        logger.error(result.stderr)
        raise AssertionError(f"'{commands[0]}' failed when run '{command}'.")


def test_interrogate():
    """Run pytest for testing your fixed code."""
    _run_command("interrogate")


def test_black():
    """Run pytest for testing your fixed code."""
    _run_command("black src --check")


def test_flake8():
    """Run pytest for testing your fixed code."""
    _run_command("flake8 src")


def test_isort():
    """Run pytest for testing your fixed code."""
    _run_command("isort src --check")


def test_mypy():
    """Run pytest for testing your fixed code."""
    _run_command("mypy src")


def test_bandit():
    """Run pytest for testing your fixed code."""
    _run_command("bandit src", False)


def test_pydocstyle():
    """Run pytest for testing your fixed code."""
    _run_command("pydocstyle src --convention=google")


def test_pylint():
    """Run pytest for testing your fixed code."""
    _run_command("pylint src --fail-under=9")


def test_pytest():
    """Run pytest for testing your fixed code."""
    _run_command("pytest --cov=src --cov-fail-under=95% --no-cov-on-fail")
