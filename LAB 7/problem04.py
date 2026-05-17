# areas.py
import math
from typing import Union

def area_circle(radius: Union[int, float]) -> float:
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return math.pi * radius * radius

def area_rectangle(length: Union[int, float], width: Union[int, float]) -> float:
    if length < 0 or width < 0:
        raise ValueError("Length/width must be non-negative.")
    return length * width

def area_triangle(base: Union[int, float], height: Union[int, float]) -> float:
    if base < 0 or height < 0:
        raise ValueError("Base/height must be non-negative.")
    return 0.5 * base * height

# use_areas.py
import areas 

if __name__ == "__main__":
    print("Circle r=3:", areas.area_circle(3))
    print("Rectangle 4x5:", areas.area_rectangle(4,5))
    print("Triangle base=6 height=4:", areas.area_triangle(6,4))
