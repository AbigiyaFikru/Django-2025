class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Create rectangle and print area
rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.width * rect.height}")