#!/usr/bin/python3

"""
Here's some documentation for a rectangle
"""

from models.base import Base

class Rectangle(Base):

    """
    And some more documentation
    """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = self.integer_validator("width", value)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = self.integer_validator("height", value)

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = self.integer_validator("x", value)

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = self.integer_validator("y", value)

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
        self.__x = self.integer_validator("x", x)
        self.__y = self.integer_validator("y", y)

    def area(self):

        """
        I forgot I need documentation here
        """

        return self.__width * self.__height
    
    def integer_validator(self, name, value):

        """
        here's some documentation
        """

        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0 and (name == "height" or name == "width"):
            raise ValueError(name + " must be > 0")
        elif value < 0:
            raise ValueError(name + " must be >= 0")
        return value

    def display(self):

        """
        There's some documentation
        """

        if self.__height == 0 or self.__width == 0:
            print("")
        else:
            ret_str = ""
            for i in range(0, self.__y):
                ret_str += "\n"
            for i in range(0, self.__height):
                for j in range(0, self.__x):
                    ret_str += " "
                for j in range(0, self.__width):
                    ret_str += "#"
                if i != self.__height - 1:
                    ret_str += "\n"
            print(ret_str)
            
    def __str__(self):

        """
        More documentation
        """

        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(
            self.id, self.x, self.y, self.__width, self.__height)