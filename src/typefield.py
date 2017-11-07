#! /usr/bin/python3.6

# Descriptors class for binding types to attributes
class Type:
    def __set_name__(self, owner, name):
        self.name = name

    def __init__(self, typefield):
        self.type = typefield

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise ValueError("Expecting {0} in variable '{1}'', got: {2}".format(self.type, self.name, type(value)))
        instance.__dict__[self.name] = value


if __name__ == "__main__":
    class TestClass:
        name = TypeField(str)
        def __init__(self, name):
            self.name = name

    test = TestClass(5)
