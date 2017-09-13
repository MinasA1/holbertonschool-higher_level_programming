#!/usr/bin/python3
"""module square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method"""
        return"[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                        self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """public method update"""
        func = {0: 'id', 1: 'size', 2: 'x', 3: 'y'}
        funclist = ['id', 'size', 'x', 'y']
        if args:
            for i, val in enumerate(args):
                if i in func:
                    setattr(self, func[i], val)
        else:
            for key, val in kwargs.items():
                if key in funclist:
                    setattr(self, key, val)

    def to_dictionary(self):
        """json represantation"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
