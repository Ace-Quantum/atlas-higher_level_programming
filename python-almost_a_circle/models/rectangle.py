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
            raise ValueError(name + " must be > than 0.")
        elif value < 0:
            raise ValueError(name + " must be >= 0")
        return value