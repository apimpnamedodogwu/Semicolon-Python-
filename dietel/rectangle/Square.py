from dietel.rectangle.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __str__(self):
        return f"This square is {self.length} by {self.width}!"


square = Square(4)
print(square.area())
print(square.__str__())