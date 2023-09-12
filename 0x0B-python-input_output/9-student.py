#!/usr/bin/python3

'''
    9-student - defines a student class
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

    def to_json(self):
        '''
            to_json - retrieves a dictionary representation of a Student
                      instance

            Return: return the dictionary representation of the Student
                    instance
        '''

        return (self.__dict__)
