#!/usr/bin/python3
"""module square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """__str__ method"""
        str = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return str.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, value):
        """size setter"""
        super().update(width=value)
        super().update(height=value)

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
