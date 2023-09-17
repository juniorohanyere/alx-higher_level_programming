#!/usr/bin/python3

'''
    square - defines a square class that inherits from a rectangle class
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Square - a square class that inherits from a rectangle

        Args:
            Rectangle; the parent to inherit from
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
            __init__ - class constructor

            Args:
                size (int): the size of the square
                x (int): the horizontal offset of the square
                y (int): the vertical offset of the square
                id (int): the id of the square (optional)

            Return: return nothing
        '''

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
            size - retrieves the value of the size of a square

            Return: return the size of the square
        '''

        return (self.width)

    @size.setter
    def size(self, value):
        '''
            size - assigns a value to the size of a square

            Args:
                value (int): the value to assign

            Return: return nothing
        '''

        self.width = value
        self.height = value

    def __str__(self):
        '''
            __str__ - overrides original str method

            Return: return a formatted str
        '''

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        '''
            update - updates the attribute of a square

            Args:
                args: list of non-keyworded arguments
                kwargs: list of keyworded arguments

            Return: return nothing
        '''
        if len(args):
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]

            except IndexError:
                pass

        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''
            to_dictionary - gets the dictionary representation of a square

            Return: return the dictionary representation of the square
        '''

        return {"id":self.id, "size": self.size, "x": self.x, "y": self.y}
