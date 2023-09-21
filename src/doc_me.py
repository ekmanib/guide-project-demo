#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

import .bad
import os



a_bad_name = 1
Another_bad_name = 'terrible'


class fix_and_DocMe:
    """
    DocMe in google style.
    """
    def __init__(self) -> None:
        pass

    def a_method(self, param1, param2):
        """
        """
        pass


def add_document():
        """The doc format of this function is bad..."""
        print("Hello, I can work, but the format is terrible.")


if __name__ == "__main__":
    add_document()
