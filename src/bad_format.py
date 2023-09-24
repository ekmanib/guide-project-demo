"""Python formatting example."""

# fix the import order here
import math

# a constant should be here
PI = 3.141592653589793

# Function to calculate factorial


def factorial(num):
    """Calculate factorial of n."""
    return 1 if num == 0 else num * factorial(num - 1)


class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x_val: int, y_val: int):
        """Initialize point object.

        Parameters
        ----------
        x_val : int
            x-coordinate of point.
        y_val : int
            y-coordinate of point.
        """
        self.x_val = x_val
        self.y_val = y_val

    def distance_from_origin(self) -> float:
        """Calculate distance from origin."""
        return math.sqrt(self.x_val**2 + self.y_val**2)

    def get_x(self):
        """Return x-coordinate of point."""
        return self.x_val

    def get_y(self):
        """Return y-coordinate of point."""
        return self.y_val


# Using global constant in function


def circumference_of_circle(radius):
    """Calculate circumference of circle."""
    return 2 * PI * radius


if __name__ == "__main__":
    # Variables
    X = 5

    # Output factorial
    print(f"Factorial of {X} is {factorial(X)}")

    # Create point object
    point = Point(3, 4)

    # Output distance from origin
    print(f"Distance of point from origin is {point.distance_from_origin()}")

    # Output circumference of circle
    print(
        f"Circumference of circle with radius {X} is {circumference_of_circle(X)}"
    )
