from shapes.Point import Point
from shapes.figures.Rectangle import Rectangle


class Square(Rectangle):

  def __init__(self, i_center: Point, i_size: float):
    super().__init__(i_center, i_size, i_size)

  def compute_area(self):
    side_length = self.get_edges()[0].length()
    return side_length * side_length

  def compute_perimeter(self):
    side_length = self.get_edges()[0].length()
    return 4 * side_length

  def compute_inner_angles(self):
    return [90, 90, 90, 90]
