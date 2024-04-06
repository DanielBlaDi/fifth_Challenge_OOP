import math
from shapes.Line import Line


class Shape:

  def __init__(self, vertices: list):
    self.__vertices = vertices

    self.__edges = []
    for i in range(len(vertices) - 1):
      self.__edges.append(Line(vertices[i], vertices[i + 1]))
    if vertices[0] != vertices[-1]:
      self.__edges.append(Line(vertices[-1], vertices[0]))
      self.__vertices.append(vertices[0])


    self.__is_regular = True
    #compare lenghts
    for i in range(len(self.__edges) - 1):
      if self.__edges[i].length() != self.__edges[i + 1].length():
        self.__is_regular = False
        break

    angles = self.compute_inner_angles()
    for i in range(len(angles) - 1):
      if angles[i] != angles[i + 1]:
        self.__is_regular = False
        break

  def compute_area(self):
    sum = 0
    for i in range(len(self.__vertices) - 1):
      sum += self.__vertices[i].get_x() * self.__vertices[i + 1].get_y()
    sum += self.__vertices[-1].get_x() * self.__vertices[0].get_y()

    other_sum = 0
    for i in range(len(self.__vertices) - 1):
      sum += self.__vertices[i + 1].get_x() * self.__vertices[i].get_y()
    other_sum += (self.__vertices[0].get_x() * self.__vertices[-1].get_y())
    return math.fabs(sum - other_sum) / 2

  def compute_perimeter(self):
    perimeter = 0.0
    for line in self.__edges:
      perimeter += line.length()
    return perimeter

  def compute_inner_angles(self):
    angles = []
    for i in range(0, len(self.__edges) - 1):
      angle =self.__edges[i].reverse().compute_angle(self.__edges[i + 1])
      angles.append(angle)
    angles.append(self.__edges[0].compute_angle(self.__edges[-1].reverse()))
    return angles

  def is_regular(self):
    return self.__is_regular

  def get_vertices(self):
    return self.__vertices

  def get_edges(self):
    return self.__edges