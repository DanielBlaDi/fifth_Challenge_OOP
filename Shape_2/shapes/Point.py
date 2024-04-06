class Point:
  definition: str = "Abstract geometric entity representing a location in space."

  def __init__(self, x: float = 0, y: float = 0):
    self.__x = x
    self.__y = y

  def compute_distance(self, point) -> float:
    return round(
        ((self.__x - point.__x)**2 + (self.__y - point.__y)**2)**(0.5), 2)

  def magnitude(self):
    return round((self.__x**2 + self.__y**2)**(0.5), 2)

  def dot_product(self, point):
    return self.__x * point.__x + self.__y * point.__y

  def sum(self, i_point):
    return Point(self.__x + i_point.__x, self.__y + i_point.__y)

  def real_product(self, i_number: float):
    return Point(self.__x * i_number, self.__y * i_number)

  def get_x(self):
    return self.__x

  def get_y(self):
    return self.__y
