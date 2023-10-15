from typing import Tuple
from homework1.Stuff.point3d import Point3D
from homework1.Stuff.angle3d import Angle3D

class Flash:
    def __init__(self):
        self.location: Point3D
        self.angle: Angle3D
        self.color: Tuple[int, int, int]
        self.power: float

    def Rotate(self, angle: Angle3D):
        pass

    def Move(self, location: Point3D):
        pass