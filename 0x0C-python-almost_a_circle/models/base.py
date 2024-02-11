#!/usr/bin/python3
""" Base Class """
import json
import csv
import turtle


class Base:
    """ define the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new instance of the object Base

        Args:
          id: User id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # to json string
    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON serialization of list_dictionaries.

        Args:
           list_dictionaries (list of dict): List of dictionary to convert.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")

        return (json.dumps(list_dictionaries))

    # save to a file
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file.

        Args:
          list_objs: list of instances who inherits of Base.
        """
        fileName = cls.__name__ + ".json"

        list_dict = []
        if list_objs is not None:
            list_dict = [o.to_dictionary() for o in list_objs]

        with open(fileName, mode='w', encoding="utf-8") as jsonFile:
            jsonFile.write(Base.to_json_string(list_dict))

    # from json string
    def from_json_string(json_string):
        """returns the list of the JSON string representation of json_string"""
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    # Create a new instance
    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        else:
            dummy = cls(10)

        dummy.update(**dictionary)

        return (dummy)

    # File to instances
    @classmethod
    def load_from_file(cls):
        """ that returns a list of instances """
        fileName = cls.__name__ + ".json"

        try:
            with open(fileName, mode='r', encoding="utf-8") as jsonFile:
                dict_list = Base.from_json_string(jsonFile.read())
                return ([cls.create(**d) for d in dict_list])

        except FileNotFoundError:
            return ([])

    # save to csv file
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save an instaces to a csv file """
        fileName = cls.__name__ + ".csv"
        with open(fileName, mode='w', encoding="utf-8") as csvFile:
            if list_objs is None or list_objs == []:
                csvFile.write("[]")

            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
                for obj in list_objs:
                    csvWriter.writerow(obj.to_dictionary())

    # from csv file
    @classmethod
    def load_from_file_csv(cls):
        """ Read an instance from a scv file """
        fileName = cls.__name__ + ".csv"
        try:
            with open(fileName, mode='r') as csvFile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                csvReader = csv.DictReader(csvFile, fieldnames=fieldnames)
                dict_list = [dict([k, int(v)] for k, v in row.items())
                             for row in csvReader]
                return ([cls.create(**d) for d in dict_list])

        except FileNotFoundError:
            return ([])

    # Draw instances
    def draw(list_rectangles, list_squares):
        """ opens a window and draws all the Rectangles and Squares """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#050a10")
        turt.pensize(5)
        turt.shape("arrow")

        window_width = turt.screen.window_width()
        window_height = turt.screen.window_height()
        x = -window_width / 2 + 10
        y = 0

        turt.up()
        turt.showturtle()
        turt.color("#0B67F5")
        for rect in list_rectangles:
            turt.goto(rect.x + x, rect.y + y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.right(90)
                turt.forward(rect.height)
                turt.right(90)
            turt.up()
            x += rect.width
            y += rect.height

        turt.hideturtle()

        turt.color("#F50B8F")
        x = 0
        y = 0
        for square in list_squares:
            turt.showturtle()
            turt.goto(square.x + x, square.y + y)
            turt.down()
            for _ in range(4):
                turt.forward(square.size)
                turt.right(90)
            turt.up()
            x += square.size
            y += square.size
        turt.hideturtle()

        turtle.exitonclick()
