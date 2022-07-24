class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self) -> int:
        return self.length * self.width

    def __str__(self):
        return f"This rectangle is {self.length} by {self.width}!"


my_rectangle = Rectangle(10, 5)
print(my_rectangle.__str__())
