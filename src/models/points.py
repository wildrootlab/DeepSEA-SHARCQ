import typing as typ
import numpy as np

from point import Point


class Points:

    def __init__(self, points : typ.List[Point]) -> None:
        self.__points = points

    def to_numpy(self) -> 'np.Array':
        return np.array(self.points)

    def get_points(self):
        return self.__points