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

# Copyright 2017 Steven Merino
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
