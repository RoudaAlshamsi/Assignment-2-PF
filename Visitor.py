from enum import Enum
class VisitorCategory(Enum):
    ADULTS = "Adults between 18-60"
    CHILDREN = "Children below 18"
    TEACHER = "Teacher"
    STUDENT = "Student"
    SENIOR = "Senior above 60"

class Visitor:
    """Class to represent a ticket"""
    #constructor to initialize attributes
    def __init__(self, name, age, visitorCategory):
        self.name = name
        self.age = age
        self.visitorCategory = visitorCategory

    #setter and getter for name
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    # setter and getter for age
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    # setter and getter for visitorCategory
    def setVisitorCategory(self, visitorCategory):
        self.visitorCategory = visitorCategory

    def getVisitorCategory(self):
        return self.visitorCategory

    #method to check if the visitor is an adult
    def isAdult(self):
        return self.visitorCategory == VisitorCategory.ADULTS

    #method to check if the visitor is a child
    def isChild(self):
        return self.visitorCategory == VisitorCategory.CHILDREN

    #method to check if the visitor is a senior
    def isSenior(self):
        return self.visitorCategory == VisitorCategory.SENIOR