from shapes.figures.Triangle import Triangle

class Scalene(Triangle):
  def __init__(self, vertices: list):
    super().__init__(vertices)

  def compute_area(self):
    return super().compute_area()

  def compute_perimeter(self):
    return super().compute_perimeter()
