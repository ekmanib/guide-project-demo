#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

import math
from numbers import Number

# NOT used, but it will trigger a `bandit` save issue
TOKEN = "1234567890"

# a constant should be here
PI = 3.141592653589793

# Constants should not be here
x = 5
y = 10


def area_of_circle(radius):
    return PI * math.pow(radius, 2)


class Rectangle:
    def __init__(self, width: Number, height: Number) -> None:
        self.width = width
        self.height = height

    def area(self) -> Number:
        return self.width * self.height


if __name__ == "__main__":
    print(f"Area of circle with radius {x} is {area_of_circle(x)}")
    rect = Rectangle(x, y)
    print(f"Area of rectangle with width {x} and height {y} is {rect.area()}")
