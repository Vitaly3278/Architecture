from homework1.ModelElements.polygon import Polygon
from homework1.ModelElements.texture import Texture
from homework1.Stuff.point3d import Point3D

from typing import List


class PolygonalModel:
    def __init__(self, textures: List[Texture]):
        self.textures = textures
        self.polygons: List[Polygon] = []
        self.points: List[Point3D] = []
        self.polygons.append(Polygon(self.points))