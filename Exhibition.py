from Item import Item
from Tour import Tour

#Importing Item class for Inheritance
class Exhibition:
    """Class to represent an exhibition"""
    #constructor to initialize attributes
    def __init__(self, durationOfTime, location):
        self.durationOfTime = durationOfTime
        self.location = location
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    #setter and getter for durationOfTime
    def setDurationOfTime(self, durationOfTime):
        self.durationOfTime = durationOfTime

    def getDurationOfTime(self):
        return self.durationOfTime

    #setter and getter for location
    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    #the following methods show the aggregation relationship
    #method to print item details
    def addItem(self, item):
        # Use the Item class
        if isinstance(item, Item):
            self.items.append(item)
        else:
            raise ValueError("Only instances of Item class can be added to the exhibition.")

    #method to remove an item from an exhibition
    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in the exhibition.")

    #method to print all items in the exhibition
    def printItems(self):
        print("Items in the exhibition:")
        for item in self.items:
            print(item.getTitle())

        #method to add a tour to the exhibition (this shows composition relationship)
        def addTour(self, tour):
            if isinstance(tour, Tour):
                self.tours.append(tour)
            else:
                raise ValueError("Only instances of Tour class can be added to the exhibition.")