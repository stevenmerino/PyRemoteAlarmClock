#! /usr/bin/python3

# Class that can be used to require certain data types in a class. See PEP 487: Descriptor Protocol Enhancements

class TypeField:
    def __init__(self, typefield):
        self.type = typefield

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise ValueError('expecting {self.type} in var "{self.name}", got: {type(value)}')
        instance.__dict__[self.name] = value

    # this is the new initializer:
    def __set_name__(self, owner, name):
        self.name = name
