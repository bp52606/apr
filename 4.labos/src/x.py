#!/usr/bin/env python3.10

class X:

    dots = list()

    def __init__(self, dots: list()):
        self.dots = dots

    def __getitem__(self, item):
        return self.dots[item]

    def __setitem__(self, key, value):
        self.dots[key] = value

    def __add__(self, other):
        suma = X([])
        for i,j in enumerate(self.dots):
            suma[i] = self.dots[i]+other[i]
        return suma

    def __mul__(self, other):
        suma = X([])
        for i,j in enumerate(self.dots):
            suma[i] = self.dots[i]*other[i]
        return suma

    def __iadd__(self, other):
        suma = X([])
        for i, j in enumerate(self.dots):
            suma[i] = self.dots[i] + other
        return suma

    def __imul__(self, other):
        suma = X([])
        for i,j in enumerate(self.dots):
            suma[i] = self.dots[i]*other
        return suma

    def __sub__(self, other):
        suma = X([])
        for i,j in enumerate(self.dots):
            suma[i] = self.dots[i]-other[i]
        return suma

    def __isub__(self, other):
        suma = X([])
        for i,j in enumerate(self.dots):
            suma[i] = self.dots[i]-other
        return suma

    def __rsub__(self, other):
        suma = X([])
        for i,j in enumerate(self.dots):
            suma[i] = other - self.dots[i]
        return suma

    def __len__(self):
        return len(self.dots)

    def __copy__(self):
        return (self.dots).copy()

