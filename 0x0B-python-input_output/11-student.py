#!/usr/bin/python3

'''
    11-student - defines a student class based on 10-student.py
'''


class Student:
    '''
        Student - a student class
    '''

    def __init__(self, first_name, last_name, age):
        '''
            __init__ - instatiation method

            Args:
                first_name (str): the first name of the student
                last_name (str): the last name of the student
                age (int): the age of the student

            Return: return nothing
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
            to_json - retrieves a dictionary representation of a Student
                      instance

            Args:
                attrs (list/str): attribute names (optional)

            Return: return the dictionary representation of the Student
                    instance
        '''

        if (isinstance(attrs, list) and
                all(isinstance(element, str) for element in attrs)):
            return ({i: getattr(self, i) for i in attrs if hasattr(self, i)})

        return (self.__dict__)

    def reload_from_json(self, json):
        '''
            reload_from_json - replaces all attributes of the Student
                               instance

            Args:
                json (dict): the key is the attribute name and the value is
                             the attribute

            Return: return nothing
        '''

        for i, j in json.items():
            setattr(self, i, j)
