#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/
"""Python code for testing doc_me.py."""

from src.doc_me import *


def test_area_of_circle():
    """Test area of circle."""
    assert area_of_circle(1) == 3.141592653589793


def test_Rectangle():
    """Test Rectangle class."""
    r = Rectangle(2, 3)
    assert r.area() == 6
