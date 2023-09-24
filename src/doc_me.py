#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/
"""Constants and functions for calculating areas of shapes."""

import math
from typing import Union

# NOT used, but it will trigger a `bandit` save issue


# a constant should be here
PI = 3.141592653589793


def area_of_circle(radius):
    """Return the area of a circle with the given radius.

    Parameters
    ----------
    radius: float
        Radius of circle.
    """
    return PI * math.pow(radius, 2)


class Rectangle:
    """Class Rectangle holds information and methods for a rectangle."""

    def __init__(
        self, width: Union[int, float], height: Union[int, float]
    ) -> None:
        """Initialize a rectangle object.

        Parameters:
        -----------
        width : float
            width of rectangle.
        height : float
            height of rectangle.

        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the area of the rectangle.

        Parameters:
        -----------
        None
        """
        return self.width * self.height

    def get_height(self):
        """Return the height of the rectangle."""
        return self.height

    def get_width(self):
        """Return the width of the rectangle."""
        return self.width


if __name__ == "__main__":
    # Define constants
    X = 5
    Y = 10

    # Print the area of a circle
    print(f"Area of circle with radius {X} is {area_of_circle(X)}")

    # Initialize a rectangle object and print its area
    rect = Rectangle(X, Y)
    print(f"Area of rectangle with width {X} and height {Y} is {rect.area()}")
