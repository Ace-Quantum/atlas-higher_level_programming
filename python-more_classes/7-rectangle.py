#!/usr/bin/python3
"""
this is some documentation
"""
class Rectangle:
    """
    this is more documentation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
             raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            ret_str = ""
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    if type(self.print_symbol) == list:
                        ret_str += "["
                        for k in range(0, len(self.print_symbol)):
                            ret_str += "'" + self.print_symbol[k] + "'"
                            if k != len(self.print_symbol) - 1:
                                ret_str += ","
                        ret_str += "]"
                    else:
                        ret_str += str(self.print_symbol)
                if i != self.__height - 1:
                    ret_str += "\n"
            return ret_str

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
