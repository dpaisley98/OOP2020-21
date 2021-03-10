# abstract class
from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def no_of_sides(self, e):
        num = e
        print("I have %d sides", num)


class Triangle(Polygon):
    def no_of_sides(self, e): # overriding abstract method
        print("I have 3 sides")


t = Triangle()
t.no_of_sides(3)


class Pentagon(Polygon):
    def no_of_sides(self, e): # overriding abstract method
        print("I have 5 sides")


p = Pentagon()
p.no_of_sides(5)