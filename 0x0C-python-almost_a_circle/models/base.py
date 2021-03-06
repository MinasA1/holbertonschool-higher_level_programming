#!/usr/bin/python3
"""module base"""


import json


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string represantation"""
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON to file"""
        js = []
        for obj in list_objs:
            js.append(obj.to_dictionary())
        js = Base.to_json_string(js)
        with open("{:s}.json".format(cls.__name__), 'w') as jsf:
                jsf.write(js)

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance of attributes already set"""
        if cls.__name__ == 'Rectangle':
            from models.rectangle import Rectangle
            dummy = Rectangle(1, 1)
        if cls.__name__ == 'Square':
            from models.square import Square
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open("{:s}.json".format(cls.__name__)) as jsf:
                jsdicts = Base.from_json_string(jsf.read())
        except:
            return []
        objlist = []
        for element in jsdicts:
            objlist.append(cls.create(**element))
        return objlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes JSON to file csv"""
        js = []
        for obj in list_objs:
            js.append(obj.to_dictionary())
        js = Base.to_json_string(js)
        with open("{:s}.csv".format(cls.__name__), 'w') as jsf:
                jsf.write(js)

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances"""
        try:
            with open("{:s}.csv".format(cls.__name__)) as jsf:
                jsdicts = Base.from_json_string(jsf.read())
        except:
            return []
        objlist = []
        for element in jsdicts:
            objlist.append(cls.create(**element))
        return objlist

    @staticmethod
    def draw(list_rectangles, list_squares):
        """method to print turtle graphic"""
        import turtle
        for obj in list_rectangles:
            args = [int(i) for i in obj.split() if i.isdigit()]
            r = Rectangle(*args)
            turtle.pos(r.x, r.y)
            turtle.fd(r.width)
            turtle.rt(90)
            turtle.fd(r.height)
            turtle.rt(90)
            turtle.fd(r.width)
            turtle.rt(90)
            turtle.fd(r.height)
            turtle.clear()
        for obj in list_squares:
            args = [int(i) for i in obj.split()if i.isdigit()]
            s = Square(*args)
            for i in range(4):
               turtle. pos(s.x, s.y)
               turtle. fd(s.size)
               turtle. rt(90)
            turtle.clear()
        del r
        del s
