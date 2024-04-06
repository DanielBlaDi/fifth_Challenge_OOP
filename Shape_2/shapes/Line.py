from shapes.Point import Point
import math


class Line:
  definition: str = "It's a join between two points"

  def __init__(self, start_point: Point, end_point: Point):
    self.__start_point = start_point
    self.__end_point = end_point

  def length(self):
    return self.__start_point.compute_distance(self.__end_point)

  def get_starting_point(self):
    return self.__start_point

  def get_ending_point(self):
    return self.__end_point

  def to_vector(self):
    return self.__end_point.sum(self.__start_point.real_product(-1))

  def compute_angle(self, i_line):
    self_vector = self.to_vector()
    i_vector = i_line.to_vector()

    magnitude_product = (self_vector.magnitude() * i_vector.magnitude())
    cos = self_vector.dot_product(i_vector) / magnitude_product

    return round(math.degrees(math.acos(cos)), 3)

  def reverse(self):
    return Line(self.__end_point, self.__start_point)
