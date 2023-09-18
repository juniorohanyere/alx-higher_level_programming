#!/usr/bin/python3

'''
    base - defines a base class function
'''

import json
import csv

class Base:
    '''
        Base - a base class function
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
            __init__ - class constructor

            Args:
                id (int): id is assumed to be an integer

            Return: return nothing
        '''

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            to_json_string - gets the json string representation of a list

            Args:
                list_dictionaries (list): a list of dictionaries

            Return: return the json string representation fo @list_dictionaries
        '''

        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            save_to_file - writes the JSON string representation of a list
                           object to a file

            Args:
                cls: the class name
                list_objs: the list objects

            Return: return nothing
        '''

        filename = cls.__name__ + ".json"
        new_string = []

        if list_objs is not None:
            for list_item in list_objs:
                list_item = list_item.to_dictionary()
                json_rep = json.loads(cls.to_json_string(list_item))
                new_string.append(json_rep)

        with open(filename, 'w') as file:
            json.dump(new_string, file)

    @staticmethod
    def from_json_string(json_string):
        '''
            from_json_string - retrieves a list of json string representation

            Args:
                json_string (list of dict): string representing a list of
                                            dictionaries

            Return: return an empty list if @json_string is None or empty
                    return @json_string otherwise
        '''

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            create - creates an instance with all attributes already set

            Args:
                cls: the class instance
                dictionary: double pointer to dictionary :)

            Return: return an instance with all attributes already set
        '''

        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Square":
            rect = Square(5)

        elif cls.__name__ == "Rectangle":
            rect = Rectangle(3, 8)

        rect.update(**dictionary)

        return (rect)

    @classmethod
    def load_from_file(cls):
        '''
            load_from_file - retrieves a list of all instances

            Args:
                cls: the class name

            Return: return the list of all instances
        '''

        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding="utf-8") as file:
                new_string = cls.from_json_string(file.read())

        except Exception:
            return []

        list_instances = []

        for list_instance in new_string:
            tmp_instance = cls.create(**list_instance)
            list_instances.append(tmp_instance)

        return (list_instances)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
            save_to_file_csv - serializes in csv

            Args:
                cls: the class name
                list_objs: list objects

            Return: return nothing
        '''

        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline='', encoding="utf-8") as file:
            wfile = csv.writer(file, delimiter=" ")

            if cls.__name__ == "Rectangle":
                for list_item in list_objs:
                    new_string = ""
                    list_item = list_item.to_dictionary()
                    new_string += (str(list_item["id"]) + "," +
                                   str(list_item["width"]) + "," +
                                   str(list_item["height"]) + "," +
                                   str(list_item["x"]) + "," +
                                   str(list_item["y"]))

                    wfile.writerow(new_string)

            if cls.__name__ == "Square":
                for list_item in list_objs:
                    new_string = ""
                    list_item = list_item.to_dictionary()
                    new_string += (str(list_item["id"]) + "," +
                               str(list_item["size"]) + "," +
                               str(list_item["x"]) + "," +
                               str(list_item["y"]))

                    wfile.writerow(new_string)

    @classmethod
    def load_from_file_csv(cls):
        '''
            load_from_file_csv - deserializes in csv

            Args:
                cls: the class name

            Return: return an empty list
        '''

        return []
