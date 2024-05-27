from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class GeometricShape(ABC):
    """
    Abstract class representing a geometric shape.
    """
    @abstractmethod
    def calculate_area(self):
        """
        Calculates the area of the geometric shape.
        """
        pass


class ShapeColor:
    """
    Class representing the color of a shape.
    """
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        """
        Gets the color of the shape.
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Sets the color of the shape.
        """
        self._color = value


class ShapeWithText:
    """
    Class representing a shape with text.
    """
    def __init__(self, text):
        self._text = text

    @property
    def text(self):
        """
        Gets the text of the shape.
        """
        return self._text

    @text.setter
    def text(self, value):
        """
        Sets the text of the shape.
        """
        self._text = value


class Rectangle(GeometricShape, ShapeWithText):
    """
    Class representing a rectangle.
    """
    def __init__(self, width, height, color, text):
        self._width = width
        self._height = height
        self._color = ShapeColor(color)
        self._text = ShapeWithText(text)

    def calculate_area(self):
        """
        Calculates the area of the rectangle.
        """
        return self._width * self._height

    def draw(self):
        """
        Draws the rectangle and fills it with the specified color.
        """
        plt.figure()
        plt.gca().add_patch(plt.Rectangle((0, 0), self._width, self._height, color=self._color.color))
        plt.axis('scaled')
        plt.axis('off')
        plt.text(self._width / 2, self._height / 2, self._text.text, ha='center', va='center')
        plt.show()

    def get_info(self):
        """
        Returns information about the rectangle.
        """
        return f"Rectangle, width: {self._width}, height: {self._height}, color: {self._color.color}, text: {self._text.text}"


def input_float(prompt):
    """
    Prompts the user to enter a float value.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_color_by_name(color_name):
    """
    Gets the color object based on its name.
    """
    color = mcolors.CSS4_COLORS.get(color_name)
    if color is None:
        raise ValueError("Invalid color name.")
    return color


def input_rectangle():
    """
    Prompts the user to enter the dimensions, color, and text of a rectangle.
    """
    width = input_float("Enter the width of the rectangle: ")
    height = input_float("Enter the height of the rectangle: ")
    color_name = input("Enter the color of the rectangle: ")
    text = input("Enter the text for the rectangle: ")

    try:
        color = get_color_by_name(color_name)
        return Rectangle(width, height, color, text)
    except ValueError as e:
        print("Error: {}".format(str(e)))
        return None


def save_to_file(rectangle, filename):
    """
    Saves the figure to a file.
    """
    plt.figure()
    plt.gca().add_patch(plt.Rectangle((0, 0), rectangle._width, rectangle._height, color=rectangle._color.color))
    plt.axis('scaled')
    plt.axis('off')
    plt.text(rectangle._width / 2, rectangle._height / 2, rectangle._text.text, ha='center', va='center')
    plt.savefig(filename)


def task4():
    """
    Main function for testing the program.
    """
    while True:
        try:
            rectangle = input_rectangle()
            if rectangle is None:
                continue

            print(rectangle.get_info())
            print("Area: {}".format(rectangle.calculate_area()))
            rectangle.draw()

            choice = input("Do you want to save the rectangle to a file? (y/n): ")
            if choice.lower() == "y":
                filename = input("Enter the filename: ")
                save_to_file(rectangle, filename)

        except Exception as e:
            print("An error occurred: {}".format(str(e)))

        choice = input("Do you want to enter another rectangle? (y/n): ")
        if choice.lower() != "y":
            break