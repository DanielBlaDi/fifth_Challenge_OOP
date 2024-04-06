from shapes.Point import Point
from shapes.Shape import Shape


class Rectangle(Shape):

  def __init__(self, i_center: Point, i_width: float, i_height: float):
    vertices = [
        Point(i_center.get_x() - i_width / 2,
              i_center.get_y() - i_height / 2),
        Point(i_center.get_x() + i_width / 2,
              i_center.get_y() - i_height / 2),
        Point(i_center.get_x() + i_width / 2,
              i_center.get_y() + i_height / 2),
        Point(i_center.get_x() - i_width / 2,
              i_center.get_y() + i_height / 2)
    ]
    super().__init__(vertices)

  def compute_area(self):
    side1_length = self.get_edges()[0].length()
    side2_length = self.get_edges()[1].length()
    return side1_length * side2_length

  def compute_perimeter(self):
    perimeter = 0
    for line in self.get_edges():
      perimeter += line.length()
    return perimeter

  def compute_inner_angles(self):
    return [90, 90, 90, 90]
