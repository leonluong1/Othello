# Leon Luong 69139013 Lab sec. 9

import math


def frac_to_point(frac_x: float, frac_y: float) -> 'Point':
    "Returns a point using fractional coordinates."
    return Point(frac_x, frac_y)
    

def pixel_to_point(pixel_x: float, pixel_y: float, width: float, height: float) -> 'Point':
    "Returns a point using fractional points."
    point_x = pixel_x/width
    point_y = pixel_y/height
    return Point(point_x, point_y)




    
class Point:
    
    def __init__(self, frac_x: float, frac_y: float):
        "Takes fractional coordinates and creates the Point object"
        self._frac_x = frac_x
        self._frac_y = frac_y


    def frac(self) -> (float, float):
        "Returns fractional coordinates."
        return (self._frac_x, self._frac_y)
    

    def pixel(self, width: float, height: float) -> (float, float):
        "Returns pixel coordinates."
        pixel_x = int(self._frac_x * width)
        pixel_y = int(self._frac_y * height)
        return (pixel_x, pixel_y)


    def point_to_frac_distance(self, point: 'Point') -> float:
        """
        Returns the distance (in fractions) from the inital point object
        to the given point object.
        """
        return math.sqrt(((self.frac_x - point._frac_x)**2)+((self._frac_y - point._frac_y)**2))

