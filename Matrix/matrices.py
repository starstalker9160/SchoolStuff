from errors import *

class Matrix:
    m, n = 1, 1
    contents = []
    def __init__(self, contents: list = []):
        self.contents = contents
        # self._validate()

    def null(self, m: int, n: int):
        self.m = m
        self.n = n
        for i in range(m):
            self.contents.append([0]*n)
        print(self.contents)

    # def __add__():
    # def __sub__():
    # def __mul__():

    # def __eq__():

    # def transform(anticlockwise: bool = False):

    def _validate(self):
        self.m = len(self.contents)
        

a = Matrix().null(3, 4)