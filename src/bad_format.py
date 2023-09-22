# no header!

# fix the import order here
from doc_me import PI
import math


# Function to calculate factorial
def factorial(n):
 if n==0:
  return 1
 else:
  return n * factorial(n-1)

# Class to represent a point in 2D space
class Point:
 def __init__(self,x: int,y: int):
  self.x=x
  self.y=y
 def distance_from_origin(self) -> str:
  return math.sqrt(self.x**2+self.y**2)

# Using global constant in function
def circumference_of_circle(radius):
 return 2 * PI * radius

if __name__ == '__main__':
 # Variables
 n = 5
 
 # Output factorial
 print(f"Factorial of {n} is {factorial(n)}")
 
 # Create point object
 point = Point(3,4)
 
 # Output distance from origin
 print(f"Distance of point from origin is {point.distance_from_origin()}")
 
 # Output circumference of circle
 print(f"Circumference of circle with radius {n} is {circumference_of_circle(n)}")
