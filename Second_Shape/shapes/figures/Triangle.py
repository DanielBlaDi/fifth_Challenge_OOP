from shapes.Shape import Shape


class Triangle(Shape):
  def __init__(self, vertices: list):
      super().__init__(vertices)

  def compute_area(self):
      side1_lenght1=self.get_edges()[0].length()
      side2_lenght2=self.get_edges()[1].length()
      side3_lenght3=self.get_edges()[2].length()
      s=(side1_lenght1+side2_lenght2+side3_lenght3)/2
      area=(s*(s-side1_lenght1)*(s-side2_lenght2)*(s-side3_lenght3)**0.5)
      return area

  def compute_perimeter(self):
      perimeter = 0
      for line in self.get_edges():
          perimeter += line.length()
      return perimeter
